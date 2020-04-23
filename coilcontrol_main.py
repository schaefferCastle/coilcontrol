# Copyright (c) 2020, A.Tom <thomas.astner@univie.ac.at>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -------------------------------------------------------------------------------
#  Control a Aim TTi PL-P Series DC Power Supplies - Perform Current Ramps
# -------------------------------------------------------------------------------

import sys
from os import environ
from random import randint
import time
import traceback
import threading
import numpy as np
import matplotlib.pyplot as plt

import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import *

from dcps import AimTTiPLP

# from NewPlotGUI import Ui_MainWindow
from coilGUIpy import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Set up multi-threading
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads started" % self.threadpool.maxThreadCount())

        # Plot update timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(25)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.hour = list(range(500))
        self.temperature = [randint(0, 2) for _ in range(500)]
        self.temperature2 = [randint(0, 2) for _ in range(500)]

        # PLOT Window 1
        self.plot_1.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0), width=3, syle=pg.QtCore.Qt.DashLine)
        self.plot_1.setTitle("<span style=\"color:blue;font-size:30px\">Voltage</span>")
        self.plot_1.setLabel('left', 'Temperature (°C)', color='red')
        self.plot_1.setLabel('bottom', 'Hour (H)', color='blue')
        self.plot_1.addLegend()
        self.plot_1.showGrid(x=True, y=True)
        self.my_line_ref = self.plot(self.hour, self.temperature, name='Sensor 1', pen=pen)

        # PlOT in Window 2
        self.plot_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0), width=3, syle=pg.QtCore.Qt.DashLine)
        self.plot_2.setTitle("<span style=\"color:blue;font-size:30px\">Current</span>")
        self.plot_2.setLabel('left', 'Temperature (°C)', color='red')
        self.plot_2.setLabel('bottom', 'Hour (H)', color='blue')
        self.plot_2.addLegend()
        self.plot_2.showGrid(x=True, y=True)
        self.my_line_ref2 = self.plot_2.plot(self.hour, self.temperature2, name='Sensor 2', pen=pen)
        self.plot_2.setYRange(0, 5)

        # Signals and stuff
        self.connected = False
        self.checkBox_connect.stateChanged.connect(self.device_connect)

        # Channel 1 mode selection
        self.modevariable = False  # false = current, true = voltage
        self.radio_cc1.toggled.connect(lambda: self.modechoose(self.radio_cc1))
        self.radio_cv1.toggled.connect(lambda: self.modechoose(self.radio_cv1))

        # State Vars
        self.outputvar = False
        self.automaticstatevar = False
        self.autostatvar = False
        self.rampinprogress = False

        self.checkBox_output.stateChanged.connect(lambda: self.chkstate(self.checkBox_output))
        self.pushButton_setval.clicked.connect(lambda: self.clickevents(self.pushButton_setval))
        self.checkBox_automaticcontrol.stateChanged.connect(lambda: self.clickevents(self.checkBox_automaticcontrol))

        # Channel increment set
        self.pushButton_setincr.clicked.connect(lambda: self.clickevents(self.pushButton_setincr))
        self.pushButton_addincr.clicked.connect(lambda: self.clickevents(self.pushButton_addincr))
        self.pushButton_subincr.clicked.connect(lambda: self.clickevents(self.pushButton_subincr))

        # Auto Ramp
        # self.ramptimer = QtCore.QTimer()
        # self.ramptimer.timeout.connect(self.rampcurrent)
        self.pushButton_startramp.clicked.connect(lambda: self.clickevents(self.pushButton_startramp))
        self.smoothDwell = 100
        self.ramppoints = []

        self.pushButton_showtrajectorie.clicked.connect(lambda: self.clickevents(self.pushButton_showtrajectorie))
        self.pushButton_smoothrampstart.clicked.connect(lambda: self.clickevents(self.pushButton_smoothrampstart))

        self.pushButton_linrampshowtrajectory.clicked.connect(lambda:
                                                              self.clickevents(self.pushButton_linrampshowtrajectory))
        self.pushButton_linrampstart.clicked.connect(lambda: self.clickevents(self.pushButton_linrampstart))

    def clickevents(self, b):
        if b.objectName() == 'pushButton_setval':
            print('Set button clicked!')
            if self.radio_cc1.isChecked() == True:
                print('Current is set!')
                self.supply.setCurrent(self.doubleSpinBox_setval.value(), channel=2)
            if self.radio_cv1.isChecked() == True:
                print('Voltage is set!')
                self.supply.setVoltage(self.doubleSpinBox_setval.value(), channel=2)
        if b.objectName() == 'pushButton_setincr':
            if self.radio_currinc.isChecked() == True:
                print('Setting new current increment')
                self.supply.setCurrentDelta(self.doubleSpinBox_setincr.value(), channel=2)
            if self.radio_voltinc.isChecked() == True:
                print('Setting new voltage increment')
                self.supply.setVoltageDelta(self.doubleSpinBox_setincr.value(), channel=2)
        if b.objectName() == 'pushButton_addincr':
            if self.radio_currinc.isChecked() == True:
                print('Adding current increment to output')
                self.supply.incCurrentByDelta(channel=2)
            if self.radio_voltinc.isChecked() == True:
                print('Adding voltage increment to output')
                self.supply.incVoltageByDelta(channel=2)
        if b.objectName() == 'pushButton_subincr':
            if self.radio_currinc.isChecked() == True:
                print('Subtracting current increment to output')
                self.supply.decCurrentByDelta(channel=2)
            if self.radio_voltinc.isChecked() == True:
                print('Subtracting voltage increment to output')
                self.supply.decVoltageByDelta(channel=2)
        if b.objectName() == 'checkBox_automaticcontrol':
            if b.isChecked() == True:
                print('Automatic control activated!')
            if b.isChecked() == False:
                self.autostatvar = False
                print('Automatic control deactivated!')
                print('Timer stopped!')
        if b.objectName() == 'pushButton_startramp':
            print('Starting the ramp!')
            if not self.rampinprogress:
                self.rampinprogress = True
                # worker = Worker(self.rampcurrent(delta=self.doubleSpinBox_autoincr.value(),
                #                                  target=self.doubleSpinBox_target.value(),
                #                                  waittime=self.spinBox_dwell.value()/1000, statvar=self.autostatvar))
                # worker.signals.finished.connect(self.thread_complete)
                # self.timer.stop()
                t = threading.Thread(target=self.rampcurrent, args=(self.doubleSpinBox_autoincr.value(),
                                                                    self.doubleSpinBox_target.value(),
                                                                    self.spinBox_dwell.value() / 1000,
                                                                    self.autostatvar))
                t.start()
                # self.threadpool.start(worker)
            else:
                print('You can not start a second ramp thread!')
        if b.objectName() == 'pushButton_showtrajectorie':
            result = self.calcTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            # print(self.ramppoints)
        if b.objectName() == 'pushButton_smoothrampstart':
            print('Starting smooth ramp!')
            result = self.calcTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            t = threading.Thread(target=self.rampcurrentlist)
            t.start()
        if b.objectName() == 'pushButton_linrampshowtrajectory':
            result = self.calcLinTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
        if b.objectName() == 'pushButton_linrampstart':
            result = self.calcLinTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            t = threading.Thread(target=self.rampcurrentlist)
            t.start()

    def chkstate(self, b):
        if b.objectName() == 'checkBox_output':
            if b.isChecked() == True:
                print('Setting output ON')
                self.supply.outputOn(channel=2)
            if b.isChecked() == False:
                self.supply.outputOff(channel=2)
                print('Setting output OFF')

    def device_connect(self, state):
        if state == QtCore.Qt.Checked:
            self.connectPs()
            self.connected = True
            self.label_deviceName.setText(self.supply.idn())
            self.checkBox_output.setEnabled(True)
            self.groupBox_deviceControl.setEnabled(True)
        else:
            self.checkBox_output.setChecked(False)
            self.disconnectPs()
            self.connected = False
            self.checkBox_output.setEnabled(False)

    def rampcurrent(self, delta, target, waittime, statvar):
        self.rampinprogress = True
        current = self.supply.queryCurrent(channel=2)
        # self.timer.stop()
        if statvar is False:
            print('Deciding direction of ramp...')
            statvar = True
            self.supply.setCurrentDelta(delta, channel=2)
            rampdirection = current - target
            if rampdirection > 0:
                print('Ramping down!')
            elif rampdirection < 0:
                print('Ramping up!')
            else:
                print('Ramp direction is zero!')

        if rampdirection < 0:
            while current < target:
                self.supply.incCurrentByDelta(channel=2)
                time.sleep(waittime)
                if current > target:
                    print('Current larger than target, breaking!')
                    break
                current = self.supply.queryCurrent(channel=2)
                # print(current)
        if rampdirection > 0:
            while current > target:
                self.supply.decCurrentByDelta(channel=2)
                time.sleep(waittime)
                if current < target:
                    print('Current smaller than target, breaking!')
                    break
                current = self.supply.queryCurrent(channel=2)
                # print(current)
        print('Reached target vlue!')
        self.rampinprogress = False
        return 1

    def rampcurrentlist(self):
        print('Smooth current ramp starting!')
        for i in self.ramppoints:
            print(i)
            self.supply.setCurrent(i, channel=2, wait=0)
            time.sleep(self.smoothDwell)
            print(i)

    def thread_complete(self):
        print('Thread completed!')
        self.timer.start()
        # reset state variables as the thread completed!
        self.automaticstatevar = False

    def update_plot_data(self):
        self.hour = self.hour[1:]
        self.hour.append(self.hour[-1] + 1)

        self.temperature = self.temperature[1:]
        self.temperature2 = self.temperature2[1:]
        if self.connected and not self.rampinprogress:
            a = self.supply.measureCurrent(channel=2)
            b = self.supply.measureVoltage(channel=2)
            self.temperature.append(b)
            self.temperature2.append(a)
            self.lcd2_volt.display(b)
            self.lcd2_curr.display(a)
        else:
            self.temperature.append(randint(0, 2))
            self.temperature2.append(randint(0, 2))

        self.my_line_ref.setData(self.hour, self.temperature)
        self.my_line_ref2.setData(self.hour, self.temperature2)

    def plot(self, hour, temperature, **kwargs):
        my_line_ref = self.plot_1.plot(hour, temperature, **kwargs)
        return my_line_ref

    def closeEvent(self, event):
        if self.connected:
            print('Device still connected, disconnecting!')
            self.disconnectPs()
            self.connected = False

        print('Ending software - byeeee')

    def connectPs(self):
        self.address = self.lineEdit_resource.text()
        print("Connecting to", self.address)
        self.resource = environ.get('aimtti', self.address)
        self.supply = AimTTiPLP(self.resource)
        self.supply.open()
        # self.supply.outputOnAll()

    def disconnectPs(self):
        self.supply.outputOffAll()
        self.supply.setLocal()
        self.supply.close()
        print("Disconnecting from", self.address)
        self.label_deviceName.setText('<connected to>')

    def modechoose(self, b):
        if b.text() == "Current" and b.isChecked():
            self.modevariable = False
            print('Current branch', self.modevariable)

        if b.text() == "Voltage" and b.isChecked():
            self.modevariable = True
            print('voltage branch', self.modevariable)

    def calcTrajectorie(self):
        print('Calculating current trajectorie!')
        if self.checkBox_connect.isChecked() == True:
            currentnow = self.supply.measureCurrent(channel=2)
        else:
            currentnow = 0.

        target = self.doubleSpinBox_smoothtarget.value()
        y3 = abs(currentnow - target)
        rate = self.doubleSpinBox_smoothrate.value() / 60.
        dwell = self.spinBox_smoothdwell.value() / 1000.

        x3 = y3 / rate  # ramp time
        reso = x3 / dwell
        # print('Ramp contains {} points'.format(reso))

        x = np.linspace(0, x3, int(reso))
        y = np.piecewise(x, [x < x3 / 3, (x3 / 3 <= x) * (x < 2 * x3 / 3), (2 * x3 / 3 <= x) * (x <= x3)],
                         [lambda x: (9 * np.square(x) * y3) / (4 * x3 ** 2),
                          lambda x: -(y3 / 4) + (3 * x * y3) / (2 * x3),
                          lambda x: -((5 * y3) / 4) - (9 * np.square(x) * y3) /
                                    (4 * x3 ** 2) + (9 * x * y3) / (2 * x3)])
        y = y.round(decimals=3)

        if target < currentnow:
            print('Ramp is down!')
            yy = np.flip(y) + target
        if target > currentnow:
            print('Ramp is up!')
            yy = y + currentnow

        plt.ion()
        plt.plot(x, yy)

        return dwell, yy

    def calcLinTrajectorie(self):
        print('Calculating current trajectorie!')
        if self.checkBox_connect.isChecked() == True:
            print('Meausring current!')
            currentnow = self.supply.measureCurrent(channel=2)
        else:
            currentnow = 0.

        target = self.doubleSpinBox_lintarget.value()
        y3 = abs(currentnow - target)
        rate = self.doubleSpinBox_linrate.value() / 60.
        dwell = self.spinBox_lindwell.value() / 1000.

        x3 = y3 / rate  # ramp time
        reso = x3 / dwell

        x = np.linspace(0, x3, int(reso))
        y = rate * x
        y = y.round(decimals=3)

        if target < currentnow:
            print('Ramp is down!')
            yy = np.flip(y) + target
        if target > currentnow:
            print('Ramp is up!')
            yy = y + currentnow
        if target == currentnow:
            print('Target current already set?')
            yy = y

        plt.ion()
        plt.plot(x, yy)

        return dwell, yy


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            self.fn
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        # else:
        #     self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    # result = pyqtSignal(int)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
