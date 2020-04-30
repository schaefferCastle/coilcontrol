# Copyright (c) 2020, A.tom <thomas.astner@univie.ac.at>
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
import time
import threading
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from dcps import AimTTiPLP
from coilGUIpy import Ui_MainWindow
from commserver import Server


# TODO: Progress bar for ramp?!

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Create Server
        self.server = Server()
        self.server.sessionOpened()
        self.server.signals.msg.connect(self.serverevents)

        # State Vars
        self.outputvar = False
        self.automaticstatevar = False
        self.autostatvar = False
        self.rampinprogress = False
        self.channel = 1
        self.outputstats = [False, False, False]
        self.lcd = False

        # Plot update timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)

        self.hour = list(range(1000))
        self.temperature = [0 for _ in range(1000)]
        self.temperature2 = [0 for _ in range(1000)]

        # PLOT Window 1
        self.plot_1.setBackground('w')
        pen = pg.mkPen(color=(0, 0.4470 * 255, 0.7410 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
        self.plot_1.setTitle("<span style=\"color:black;font-size:15px\">Voltage</span>")
        self.plot_1.setLabel('left', 'Voltage (V)', color='grey')
        self.plot_1.setLabel('bottom', 'Time (a.u.)', color='grey')
        self.plot_1.addLegend()
        self.plot_1.showGrid(x=True, y=True)
        self.my_line_ref = self.plot(self.hour, self.temperature, name='Channel', pen=pen)

        # PlOT in Window 2
        self.plot_2.setBackground('w')
        pen = pg.mkPen(color=(0.8500 * 255, 0.3250 * 255, 0.0980 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
        self.plot_2.setTitle("<span style=\"color:black;font-size:15px\">Current</span>")
        self.plot_2.setLabel('left', 'Current (A)', color='grey')
        self.plot_2.setLabel('bottom', 'Time (a.u.)', color='grey')
        self.plot_2.addLegend()
        self.plot_2.showGrid(x=True, y=True)
        self.my_line_ref2 = self.plot_2.plot(self.hour, self.temperature2, name='Channel', pen=pen)
        self.plot_2.setYRange(0, 3)

        # Plot in Window 3 - Trajectory
        self.plot_3.setBackground('w')
        pen = pg.mkPen(color=(0.8500 * 255, 0.3250 * 255, 0.0980 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
        self.plot_3.setTitle("<span style=\"color:black;font-size:15px\">Current Trajectory</span>")
        self.plot_3.setLabel('left', 'Current (A)', color='grey')
        self.plot_3.setLabel('bottom', 'Time (s)', color='grey')
        self.plot_3.addLegend()
        self.plot_3.showGrid(x=True, y=True)
        # self.my_line_ref3 = self.plot_3.plot(self.hour, self.temperature2, name='Channel', pen=pen)
        # self.plot_3.setYRange(0, 5)

        # Connect to PS
        self.connected = False
        self.checkBox_connect.stateChanged.connect(self.device_connect)

        # Channel mode selection
        self.modevariable = False  # false = current, true = voltage
        self.radio_cc1.toggled.connect(lambda: self.modechoose(self.radio_cc1))
        self.radio_cv1.toggled.connect(lambda: self.modechoose(self.radio_cv1))
        self.checkBox_output.stateChanged.connect(lambda: self.chkstate(self.checkBox_output))
        self.pushButton_setval.clicked.connect(lambda: self.clickevents(self.pushButton_setval))
        self.checkBox_automaticcontrol.stateChanged.connect(lambda: self.clickevents(self.checkBox_automaticcontrol))
        self.comboBox_channel.activated[str].connect(lambda: self.clickevents(self.comboBox_channel))

        # Channel increment set
        self.pushButton_setincr.clicked.connect(lambda: self.clickevents(self.pushButton_setincr))
        self.pushButton_addincr.clicked.connect(lambda: self.clickevents(self.pushButton_addincr))
        self.pushButton_subincr.clicked.connect(lambda: self.clickevents(self.pushButton_subincr))

        # Auto Ramp
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
                self.supply.setCurrent(self.doubleSpinBox_setval.value(), channel=self.channel)
            if self.radio_cv1.isChecked() == True:
                print('Voltage is set!')
                self.supply.setVoltage(self.doubleSpinBox_setval.value(), channel=self.channel)
        if b.objectName() == 'pushButton_setincr':
            if self.radio_currinc.isChecked() == True:
                print('Setting new current increment')
                self.supply.setCurrentDelta(self.doubleSpinBox_setincr.value(), channel=self.channel)
            if self.radio_voltinc.isChecked() == True:
                print('Setting new voltage increment')
                self.supply.setVoltageDelta(self.doubleSpinBox_setincr.value(), channel=self.channel)
        if b.objectName() == 'pushButton_addincr':
            if self.radio_currinc.isChecked() == True:
                print('Adding current increment to output')
                self.supply.incCurrentByDelta(channel=self.channel)
            if self.radio_voltinc.isChecked() == True:
                print('Adding voltage increment to output')
                self.supply.incVoltageByDelta(channel=self.channel)
        if b.objectName() == 'pushButton_subincr':
            if self.radio_currinc.isChecked() == True:
                print('Subtracting current increment to output')
                self.supply.decCurrentByDelta(channel=self.channel)
            if self.radio_voltinc.isChecked() == True:
                print('Subtracting voltage increment to output')
                self.supply.decVoltageByDelta(channel=self.channel)
        if b.objectName() == 'checkBox_automaticcontrol':
            if b.isChecked() == True:
                self.tabWidget_autocontrol.setEnabled(True)
                self.groupBox_channelcontrol.setEnabled(False)
            if b.isChecked() == False:
                self.autostatvar = False
                self.tabWidget_autocontrol.setEnabled(False)
                self.groupBox_channelcontrol.setEnabled(True)
        if b.objectName() == 'pushButton_startramp':
            print('Starting the ramp!')
            if not self.rampinprogress:
                self.rampinprogress = True
                t = threading.Thread(target=self.rampcurrent, args=(self.doubleSpinBox_autoincr.value(),
                                                                    self.doubleSpinBox_target.value(),
                                                                    self.spinBox_dwell.value() / 1000,
                                                                    self.autostatvar))
                t.start()
            else:
                print('You can not start a second ramp thread!')
        if b.objectName() == 'pushButton_showtrajectorie':
            result = self.calcTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            x = result[2]
            self.plot_3.clear()
            pen = pg.mkPen(color=(0.8500 * 255, 0.3250 * 255, 0.0980 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
            self.my_line_ref3 = self.plot_3.plot(x, self.ramppoints, name='Smooth Edge Ramp', pen=pen)
            # print(self.ramppoints)
        if b.objectName() == 'pushButton_smoothrampstart':
            print('Starting smooth ramp!')
            result = self.calcTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            x = result[2]
            self.plot_3.clear()
            pen = pg.mkPen(color=(0.8500 * 255, 0.3250 * 255, 0.0980 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
            self.my_line_ref3 = self.plot_3.plot(x, self.ramppoints, name='Smooth Edge Ramp', pen=pen)
            t = threading.Thread(target=self.rampcurrentlist)
            t.start()
        if b.objectName() == 'pushButton_linrampshowtrajectory':
            result = self.calcLinTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            x = result[2]
            self.plot_3.clear()
            pen = pg.mkPen(color=(0.8500 * 255, 0.3250 * 255, 0.0980 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
            self.my_line_ref3 = self.plot_3.plot(x, self.ramppoints, name='Linear Ramp', pen=pen)
        if b.objectName() == 'pushButton_linrampstart':
            result = self.calcLinTrajectorie()
            self.ramppoints = result[1]
            self.smoothDwell = result[0]
            x = result[2]
            self.plot_3.clear()
            pen = pg.mkPen(color=(0.8500 * 255, 0.3250 * 255, 0.0980 * 255), width=3, syle=pg.QtCore.Qt.DashLine)
            self.my_line_ref3 = self.plot_3.plot(x, self.ramppoints, name='Linear Ramp', pen=pen)
            t = threading.Thread(target=self.rampcurrentlist)
            t.start()
        if b.objectName() == 'comboBox_channel':
            self.updatelcd()
            if b.currentIndex() == 0:
                self.channel = 1
                if self.outputstats[0]:
                    self.checkBox_output.setChecked(True)
                else:
                    self.checkBox_output.setChecked(False)
            if b.currentIndex() == 1:
                self.channel = 2
                if self.outputstats[1]:
                    self.checkBox_output.setChecked(True)
                else:
                    self.checkBox_output.setChecked(False)
            if b.currentIndex() == 2:
                self.channel = 3
                if self.outputstats[2]:
                    self.checkBox_output.setChecked(True)
                else:
                    self.checkBox_output.setChecked(False)

    def serverevents(self, s):
        value_1 = []
        value_2 = []
        print('main window catch')
        print(s)
        # decode message by scheme
        if s.find(':') != -1:
            s, value_1 = s.split(':')
            # data,value_1,value_2=data.split(',')
            if value_1.find(',') != -1:
                value_1, value_2 = value_1.split(',')

        if s:
            self.callrespond(s, value_1, value_2)

    def callrespond(self, s, value_1, value_2):

        if s == 'get_volt':
            voltvals = [self.lcd1_volt.value(), self.lcd2_volt.value(), self.lcd3_volt.value()]
            value_1 = int(value_1)
            reply = str(voltvals[value_1 - 1])
            self.server.sendeasy(reply)

        elif s == 'get_curr':
            currvals = [self.lcd1_curr.value(), self.lcd2_curr.value(), self.lcd3_curr.value()]
            value_1 = int(value_1)
            reply = str(currvals[value_1 - 1])
            self.server.sendeasy(reply)

        elif s == 'set_channel':
            value_1 = int(value_1)
            self.comboBox_channel.setCurrentIndex(value_1 - 1)
            self.clickevents(self.comboBox_channel)
            s = 'Done!'
            self.server.sendeasy(s)

        elif s == 'set_output':
            value_1 = int(value_1)
            value_2 = int(value_2)
            if value_2 == 1:
                self.supply.outputOn(channel=value_1)
                self.server.sendeasy('Done! ON')
            elif value_2 == 0:
                self.supply.outputOff(channel=value_1)
                self.server.sendeasy('Done! OFF')
            else:
                print('wrong command')

        else:
            s = 'Wrong-Command!'
            self.server.sendeasy(s)

    def chkstate(self, b):
        if b.objectName() == 'checkBox_output':
            if b.isChecked() == True:
                print('Setting output ON')
                self.supply.outputOn(channel=self.channel)
            if b.isChecked() == False:
                self.supply.outputOff(channel=self.channel)
                print('Setting output OFF')

    def device_connect(self, state):
        if state == QtCore.Qt.Checked:
            # TODO: catch timeout and retry connecting
            self.connectPs()
            self.connected = True
            self.label_deviceName.setText(self.supply.idn())
            self.checkBox_output.setEnabled(True)
            self.groupBox_channelcontrol.setEnabled(True)
            self.timer.start()
            self.groupBox_automaticcurrentramp.setEnabled(True)
            self.updatelcd()
            # dirty hack if channel 1 is already on
            if self.outputstats[0]:
                self.checkBox_output.setChecked(True)
        else:
            self.lcd = False
            self.checkBox_output.setChecked(False)
            self.disconnectPs()
            self.connected = False
            self.checkBox_output.setEnabled(False)
            self.timer.stop()
            self.groupBox_automaticcurrentramp.setEnabled(False)
            self.groupBox_channelcontrol.setEnabled(False)

    def rampcurrent(self, delta, target, waittime, statvar):
        self.rampinprogress = True
        current = self.supply.queryCurrent(channel=self.channel)
        # self.timer.stop()
        if statvar is False:
            print('Deciding direction of ramp...')
            statvar = True
            self.supply.setCurrentDelta(delta, channel=self.channel)
            rampdirection = current - target
            if rampdirection > 0:
                print('Ramping down!')
            elif rampdirection < 0:
                print('Ramping up!')
            else:
                print('Ramp direction is zero!')

        if rampdirection < 0:
            while current < target:
                self.supply.incCurrentByDelta(channel=self.channel)
                time.sleep(waittime)
                if current > target:
                    print('Current larger than target, breaking!')
                    break
                current = self.supply.queryCurrent(channel=self.channel)
                # print(current)
        if rampdirection > 0:
            while current > target:
                self.supply.decCurrentByDelta(channel=self.channel)
                time.sleep(waittime)
                if current < target:
                    print('Current smaller than target, breaking!')
                    break
                current = self.supply.queryCurrent(channel=self.channel)
                # print(current)
        print('Reached target vlue!')
        self.rampinprogress = False
        return 1

    def rampcurrentlist(self):
        print('Smooth current ramp starting!')
        for i in self.ramppoints:
            # print(i)
            self.supply.setCurrent(i, channel=self.channel, wait=0)
            time.sleep(self.smoothDwell)
            # print(i)
        print('Finished ramp!')

    def update_plot_data(self):
        self.hour = self.hour[1:]
        self.hour.append(self.hour[-1] + 1)

        self.temperature = self.temperature[1:]
        self.temperature2 = self.temperature2[1:]
        if self.connected and not self.rampinprogress:
            a = self.supply.measureCurrent(channel=self.channel)
            b = self.supply.measureVoltage(channel=self.channel)
            self.temperature.append(b)
            self.temperature2.append(a)
            if self.channel == 1:
                self.lcd1_volt.display(b)
                self.lcd1_curr.display(a)
            if self.channel == 2:
                self.lcd2_volt.display(b)
                self.lcd2_curr.display(a)
            if self.channel == 3:
                self.lcd3_volt.display(b)
                self.lcd3_curr.display(a)
        else:
            self.temperature.append(0)
            self.temperature2.append(0)

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

    def disconnectPs(self):
        # self.supply.outputOffAll()
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
            currentnow = self.supply.measureCurrent(channel=self.channel)
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
        if np.round(target, decimals=3) == np.round(currentnow, decimals=3):
            print('Already at target!')
            yy = y

        timeplot = np.linspace(0, dwell * len(x), len(x))
        # plt.ion()
        # plt.plot(timeplot, yy)
        return dwell, yy, timeplot

    def calcLinTrajectorie(self):
        print('Calculating current trajectory!')
        if self.checkBox_connect.isChecked() == True:
            # print('Meausring current!')
            currentnow = self.supply.measureCurrent(channel=self.channel)
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
            # print('Ramp is down!')
            yy = np.flip(y) + target
        if target > currentnow:
            # print('Ramp is up!')
            yy = y + currentnow
        if target == currentnow:
            # print('Target current already set?')
            yy = y

        # plt.ion()
        # plt.plot(x, yy)
        timeplot = np.linspace(0, dwell * len(x), len(x))

        return dwell, yy, timeplot

    def updatelcd(self):
        for i in range(3):
            curr = self.supply.measureCurrent(channel=(i + 1))
            volt = self.supply.measureVoltage(channel=(i + 1))
            self.outputstats[i] = self.supply.isOutputOn(channel=(i + 1))
            if i == 0:
                self.lcd1_curr.display(curr)
                self.lcd1_volt.display(volt)
                status = "CH1 - {}".format(self.outputstats[0])
                self.label_chan1.setText(status)
            if i == 1:
                self.lcd2_curr.display(curr)
                self.lcd2_volt.display(volt)
                status = "CH2 - {}".format(self.outputstats[1])
                self.label_chan2.setText(status)
            if i == 2:
                self.lcd3_curr.display(curr)
                self.lcd3_volt.display(curr)
                status = "CH3 - {}".format(self.outputstats[2])
                self.label_chan3.setText(status)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
