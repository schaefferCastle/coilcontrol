# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coilGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_resource = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_resource.setObjectName("lineEdit_resource")
        self.horizontalLayout_2.addWidget(self.lineEdit_resource)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_deviceName = QtWidgets.QLabel(self.groupBox)
        self.label_deviceName.setObjectName("label_deviceName")
        self.verticalLayout_4.addWidget(self.label_deviceName)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_connect = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_connect.setObjectName("checkBox_connect")
        self.horizontalLayout_3.addWidget(self.checkBox_connect)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.label_status = QtWidgets.QLabel(self.groupBox)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_3.addWidget(self.label_status)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_6.addWidget(self.lcdNumber)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_5.addWidget(self.lcdNumber_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lcd2_volt = QtWidgets.QLCDNumber(self.groupBox_5)
        self.lcd2_volt.setObjectName("lcd2_volt")
        self.verticalLayout_7.addWidget(self.lcd2_volt)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.lcd2_curr = QtWidgets.QLCDNumber(self.groupBox_5)
        self.lcd2_curr.setObjectName("lcd2_curr")
        self.verticalLayout_8.addWidget(self.lcd2_curr)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.horizontalLayout_7.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.groupBox_6)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_9.addWidget(self.lcdNumber_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.groupBox_6)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.verticalLayout_10.addWidget(self.lcdNumber_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.horizontalLayout_7.addWidget(self.groupBox_6)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_deviceControl = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_deviceControl.setEnabled(False)
        self.groupBox_deviceControl.setObjectName("groupBox_deviceControl")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_deviceControl)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_output = QtWidgets.QCheckBox(self.groupBox_deviceControl)
        self.checkBox_output.setEnabled(False)
        self.checkBox_output.setObjectName("checkBox_output")
        self.horizontalLayout_9.addWidget(self.checkBox_output)
        self.checkBox_automaticcontrol = QtWidgets.QCheckBox(self.groupBox_deviceControl)
        self.checkBox_automaticcontrol.setObjectName("checkBox_automaticcontrol")
        self.horizontalLayout_9.addWidget(self.checkBox_automaticcontrol)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_deviceControl)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.radio_cc1 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radio_cc1.setObjectName("radio_cc1")
        self.horizontalLayout_11.addWidget(self.radio_cc1)
        self.radio_cv1 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radio_cv1.setObjectName("radio_cv1")
        self.horizontalLayout_11.addWidget(self.radio_cv1)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.doubleSpinBox_setval = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_setval.setMaximum(35.0)
        self.doubleSpinBox_setval.setSingleStep(0.01)
        self.doubleSpinBox_setval.setObjectName("doubleSpinBox_setval")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_setval)
        self.pushButton_setval = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_setval.setObjectName("pushButton_setval")
        self.horizontalLayout_12.addWidget(self.pushButton_setval)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_14)
        self.horizontalLayout_8.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_deviceControl)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radio_currinc = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_currinc.setChecked(True)
        self.radio_currinc.setObjectName("radio_currinc")
        self.horizontalLayout_16.addWidget(self.radio_currinc)
        self.radio_voltinc = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_voltinc.setObjectName("radio_voltinc")
        self.horizontalLayout_16.addWidget(self.radio_voltinc)
        self.verticalLayout_15.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.doubleSpinBox_setincr = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_setincr.setMaximum(35.0)
        self.doubleSpinBox_setincr.setSingleStep(0.01)
        self.doubleSpinBox_setincr.setObjectName("doubleSpinBox_setincr")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_setincr)
        self.pushButton_setincr = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_setincr.setObjectName("pushButton_setincr")
        self.horizontalLayout_14.addWidget(self.pushButton_setincr)
        self.verticalLayout_15.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_subincr = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_subincr.setObjectName("pushButton_subincr")
        self.horizontalLayout_15.addWidget(self.pushButton_subincr)
        self.pushButton_addincr = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_addincr.setObjectName("pushButton_addincr")
        self.horizontalLayout_15.addWidget(self.pushButton_addincr)
        self.verticalLayout_15.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_8.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_deviceControl)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout.setObjectName("gridLayout")
        self.radio_linramp = QtWidgets.QRadioButton(self.groupBox_9)
        self.radio_linramp.setEnabled(False)
        self.radio_linramp.setChecked(True)
        self.radio_linramp.setObjectName("radio_linramp")
        self.gridLayout.addWidget(self.radio_linramp, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.doubleSpinBox_target = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_target.setObjectName("doubleSpinBox_target")
        self.horizontalLayout_17.addWidget(self.doubleSpinBox_target)
        self.label_9 = QtWidgets.QLabel(self.groupBox_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_17.addWidget(self.label_9)
        self.gridLayout.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.spinBox_dwell = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_dwell.setMaximum(1000)
        self.spinBox_dwell.setObjectName("spinBox_dwell")
        self.horizontalLayout_18.addWidget(self.spinBox_dwell)
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_18, 1, 1, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.doubleSpinBox_autoincr = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_autoincr.setObjectName("doubleSpinBox_autoincr")
        self.horizontalLayout_19.addWidget(self.doubleSpinBox_autoincr)
        self.label_8 = QtWidgets.QLabel(self.groupBox_9)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_19.addWidget(self.label_8)
        self.gridLayout.addLayout(self.horizontalLayout_19, 2, 0, 1, 1)
        self.pushButton_startramp = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_startramp.setObjectName("pushButton_startramp")
        self.gridLayout.addWidget(self.pushButton_startramp, 2, 1, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_9)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        self.verticalLayout_3.addWidget(self.groupBox_deviceControl)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plot_1 = PlotWidget(self.widget_3)
        self.plot_1.setObjectName("plot_1")
        self.verticalLayout_2.addWidget(self.plot_1)
        self.plot_2 = PlotWidget(self.widget_3)
        self.plot_2.setObjectName("plot_2")
        self.verticalLayout_2.addWidget(self.plot_2)
        self.plot_3 = PlotWidget(self.widget_3)
        self.plot_3.setObjectName("plot_3")
        self.verticalLayout_2.addWidget(self.plot_3)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Device Connection"))
        self.label.setText(_translate("MainWindow", "Resource Name"))
        self.lineEdit_resource.setText(_translate("MainWindow", "TCPIP0::169.254.70.222::9221::SOCKET"))
        self.label_deviceName.setText(_translate("MainWindow", "<connected to>"))
        self.checkBox_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_status.setText(_translate("MainWindow", "Status"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Device Status"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Channel 1"))
        self.label_2.setText(_translate("MainWindow", "Voltage"))
        self.label_3.setText(_translate("MainWindow", "Current"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Channel 2"))
        self.label_4.setText(_translate("MainWindow", "Voltage"))
        self.label_5.setText(_translate("MainWindow", "Current"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Channel 3"))
        self.label_6.setText(_translate("MainWindow", "Voltage"))
        self.label_7.setText(_translate("MainWindow", "Current"))
        self.groupBox_deviceControl.setTitle(_translate("MainWindow", "Device Control"))
        self.checkBox_output.setText(_translate("MainWindow", "Output ON/OFF"))
        self.checkBox_automaticcontrol.setText(_translate("MainWindow", "Automatic Control"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Channel 1"))
        self.radio_cc1.setText(_translate("MainWindow", "Current"))
        self.radio_cv1.setText(_translate("MainWindow", "Voltage"))
        self.pushButton_setval.setText(_translate("MainWindow", "Set"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Increment"))
        self.radio_currinc.setText(_translate("MainWindow", "Current"))
        self.radio_voltinc.setText(_translate("MainWindow", "Voltage"))
        self.pushButton_setincr.setText(_translate("MainWindow", "Set"))
        self.pushButton_subincr.setText(_translate("MainWindow", "decrement (-)"))
        self.pushButton_addincr.setText(_translate("MainWindow", "increment (+)"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Automatic Current Ramp"))
        self.radio_linramp.setText(_translate("MainWindow", "Linear Ramp"))
        self.label_9.setText(_translate("MainWindow", "Target"))
        self.label_10.setText(_translate("MainWindow", "Dwell "))
        self.label_8.setText(_translate("MainWindow", "Increment"))
        self.pushButton_startramp.setText(_translate("MainWindow", "Ramp"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

