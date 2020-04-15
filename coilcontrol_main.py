import sys
from os import environ
from random import randint

import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRunnable

from dcps import AimTTiPLP

# from NewPlotGUI import Ui_MainWindow
from coilGUIpy import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Plot update timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.hour = list(range(100))
        self.temperature = [randint(0, 2) for _ in range(100)]
        self.temperature2 = [randint(0, 2) for _ in range(100)]

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

        # Signals and stuff
        self.pushButton.clicked.connect(self.on_click)
        self.connected = False
        self.checkBox_connect.stateChanged.connect(self.device_connect)

        # Channel 1 mode selection
        self.modevariable = False  # false = current, true = voltage
        self.radio_cc1.toggled.connect(lambda: self.modechoose(self.radio_cc1))
        self.radio_cv1.toggled.connect(lambda: self.modechoose(self.radio_cv1))

        # State Vars
        self.outputvar = False
        self.automaticstatevar = False
        self.rampdirection = 0

        self.checkBox_output.stateChanged.connect(lambda: self.chkstate(self.checkBox_output))
        self.pushButton_setval.clicked.connect(lambda: self.clickevents(self.pushButton_setval))
        self.checkBox_automaticcontrol.stateChanged.connect(lambda: self.clickevents(self.checkBox_automaticcontrol))

        # Channel increment set
        self.pushButton_setincr.clicked.connect(lambda: self.clickevents(self.pushButton_setincr))
        self.pushButton_addincr.clicked.connect(lambda: self.clickevents(self.pushButton_addincr))
        self.pushButton_subincr.clicked.connect(lambda: self.clickevents(self.pushButton_subincr))

        # Auto Ramp
        self.ramptimer = QtCore.QTimer()
        self.ramptimer.timeout.connect(self.rampcurrent)
        self.pushButton_startramp.clicked.connect(lambda: self.clickevents(self.pushButton_startramp))

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
                self.ramptimer.setInterval(self.spinBox_dwell.value())
            if b.isChecked() == False:
                # self.ramptimer.stop()
                self.automaticstatevar = False
                print('Automatic control deactivated!')
                print('Timer stopped!')
        if b.objectName() == 'pushButton_startramp':
            print('Starting the ramp!')
            self.ramptimer.start()

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

    def rampcurrent(self):
        current = self.supply.measureCurrent(channel=2)
        if self.automaticstatevar is False and self.rampdirection == 0:
            self.automaticstatevar = True
            self.supply.setCurrentDelta(self.doubleSpinBox_autoincr.value(), channel=2)
            self.rampdirection = current - self.doubleSpinBox_target.value()
            if self.rampdirection > 0:
                print('Ramping down!')
            elif self.rampdirection < 0:
                print('Ramping up!')
            else:
                print('Ramp direction is zero!')

        if self.rampdirection < 0:
            if current < self.doubleSpinBox_target.value():
                self.supply.incCurrentByDelta(channel=2)
            elif current >= 0.99 * self.doubleSpinBox_target.value():
                print('Reached target current value! Stopping ramp!')
                self.ramptimer.stop()
                self.automaticstatevar = False
                self.rampdirection = 0
        if self.rampdirection > 0:
            if current > self.doubleSpinBox_target.value():
                self.supply.decCurrentByDelta(channel=2)
            elif current <= 0.99 * self.doubleSpinBox_target.value():
                print('Reached target current value! Stopping ramp!')
                self.ramptimer.stop()
                self.automaticstatevar = False
                self.rampdirection = 0

    def update_plot_data(self):
        self.hour = self.hour[1:]
        self.hour.append(self.hour[-1] + 1)

        self.temperature = self.temperature[1:]
        self.temperature2 = self.temperature2[1:]
        if self.connected:
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

    def on_click(self):
        print('Button clicked!')
        a = self.supply.queryCurrentDelta(channel=2)
        self.label_status.setText(str(a))

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


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.arg = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        print('Rampthread Started')
        self.fn(*self.args, **self.kwarts)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
