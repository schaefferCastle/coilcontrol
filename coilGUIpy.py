# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coilGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 652)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/Current-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_connect = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_connect.sizePolicy().hasHeightForWidth())
        self.checkBox_connect.setSizePolicy(sizePolicy)
        self.checkBox_connect.setObjectName("checkBox_connect")
        self.gridLayout_2.addWidget(self.checkBox_connect, 1, 0, 1, 1)
        self.lineEdit_resource = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_resource.sizePolicy().hasHeightForWidth())
        self.lineEdit_resource.setSizePolicy(sizePolicy)
        self.lineEdit_resource.setObjectName("lineEdit_resource")
        self.gridLayout_2.addWidget(self.lineEdit_resource, 0, 1, 1, 2)
        self.label_deviceName = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_deviceName.sizePolicy().hasHeightForWidth())
        self.label_deviceName.setSizePolicy(sizePolicy)
        self.label_deviceName.setObjectName("label_deviceName")
        self.gridLayout_2.addWidget(self.label_deviceName, 1, 1, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_lcd = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_lcd.sizePolicy().hasHeightForWidth())
        self.groupBox_lcd.setSizePolicy(sizePolicy)
        self.groupBox_lcd.setObjectName("groupBox_lcd")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_lcd)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 1, 1, 1, 1)
        self.lcd1_volt = QtWidgets.QLCDNumber(self.groupBox_lcd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd1_volt.sizePolicy().hasHeightForWidth())
        self.lcd1_volt.setSizePolicy(sizePolicy)
        self.lcd1_volt.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd1_volt.setObjectName("lcd1_volt")
        self.gridLayout_8.addWidget(self.lcd1_volt, 2, 1, 3, 1)
        self.lcd3_volt = QtWidgets.QLCDNumber(self.groupBox_lcd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd3_volt.sizePolicy().hasHeightForWidth())
        self.lcd3_volt.setSizePolicy(sizePolicy)
        self.lcd3_volt.setSmallDecimalPoint(False)
        self.lcd3_volt.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd3_volt.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd3_volt.setObjectName("lcd3_volt")
        self.gridLayout_8.addWidget(self.lcd3_volt, 2, 5, 3, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 1, 4, 1, 1)
        self.lcd3_curr = QtWidgets.QLCDNumber(self.groupBox_lcd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd3_curr.sizePolicy().hasHeightForWidth())
        self.lcd3_curr.setSizePolicy(sizePolicy)
        self.lcd3_curr.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd3_curr.setObjectName("lcd3_curr")
        self.gridLayout_8.addWidget(self.lcd3_curr, 2, 4, 3, 1)
        self.lcd1_curr = QtWidgets.QLCDNumber(self.groupBox_lcd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd1_curr.sizePolicy().hasHeightForWidth())
        self.lcd1_curr.setSizePolicy(sizePolicy)
        self.lcd1_curr.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd1_curr.setObjectName("lcd1_curr")
        self.gridLayout_8.addWidget(self.lcd1_curr, 2, 0, 3, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 3, 1, 1)
        self.lcd2_curr = QtWidgets.QLCDNumber(self.groupBox_lcd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd2_curr.sizePolicy().hasHeightForWidth())
        self.lcd2_curr.setSizePolicy(sizePolicy)
        self.lcd2_curr.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd2_curr.setObjectName("lcd2_curr")
        self.gridLayout_8.addWidget(self.lcd2_curr, 2, 2, 3, 1)
        self.lcd2_volt = QtWidgets.QLCDNumber(self.groupBox_lcd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd2_volt.sizePolicy().hasHeightForWidth())
        self.lcd2_volt.setSizePolicy(sizePolicy)
        self.lcd2_volt.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd2_volt.setObjectName("lcd2_volt")
        self.gridLayout_8.addWidget(self.lcd2_volt, 2, 3, 3, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_chan1 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_chan1.setObjectName("label_chan1")
        self.gridLayout_8.addWidget(self.label_chan1, 0, 0, 1, 1)
        self.label_chan2 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_chan2.setObjectName("label_chan2")
        self.gridLayout_8.addWidget(self.label_chan2, 0, 2, 1, 1)
        self.label_chan3 = QtWidgets.QLabel(self.groupBox_lcd)
        self.label_chan3.setObjectName("label_chan3")
        self.gridLayout_8.addWidget(self.label_chan3, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_lcd)
        self.groupBox_channelcontrol = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_channelcontrol.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_channelcontrol.sizePolicy().hasHeightForWidth())
        self.groupBox_channelcontrol.setSizePolicy(sizePolicy)
        self.groupBox_channelcontrol.setObjectName("groupBox_channelcontrol")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_channelcontrol)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.comboBox_channel = QtWidgets.QComboBox(self.groupBox_channelcontrol)
        self.comboBox_channel.setObjectName("comboBox_channel")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_channel, 0, 2, 1, 1)
        self.checkBox_output = QtWidgets.QCheckBox(self.groupBox_channelcontrol)
        self.checkBox_output.setEnabled(False)
        self.checkBox_output.setObjectName("checkBox_output")
        self.gridLayout_7.addWidget(self.checkBox_output, 0, 1, 1, 1)
        self.groupBox_outputcontrol = QtWidgets.QGroupBox(self.groupBox_channelcontrol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_outputcontrol.sizePolicy().hasHeightForWidth())
        self.groupBox_outputcontrol.setSizePolicy(sizePolicy)
        self.groupBox_outputcontrol.setObjectName("groupBox_outputcontrol")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_outputcontrol)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.doubleSpinBox_setval = QtWidgets.QDoubleSpinBox(self.groupBox_outputcontrol)
        self.doubleSpinBox_setval.setMaximum(35.0)
        self.doubleSpinBox_setval.setSingleStep(0.01)
        self.doubleSpinBox_setval.setObjectName("doubleSpinBox_setval")
        self.gridLayout_5.addWidget(self.doubleSpinBox_setval, 1, 0, 1, 1)
        self.radio_cv1 = QtWidgets.QRadioButton(self.groupBox_outputcontrol)
        self.radio_cv1.setObjectName("radio_cv1")
        self.gridLayout_5.addWidget(self.radio_cv1, 0, 1, 1, 1)
        self.pushButton_setval = QtWidgets.QPushButton(self.groupBox_outputcontrol)
        self.pushButton_setval.setObjectName("pushButton_setval")
        self.gridLayout_5.addWidget(self.pushButton_setval, 1, 1, 1, 1)
        self.radio_cc1 = QtWidgets.QRadioButton(self.groupBox_outputcontrol)
        self.radio_cc1.setObjectName("radio_cc1")
        self.gridLayout_5.addWidget(self.radio_cc1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_outputcontrol, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.groupBox_incrementcontrol = QtWidgets.QGroupBox(self.groupBox_channelcontrol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_incrementcontrol.sizePolicy().hasHeightForWidth())
        self.groupBox_incrementcontrol.setSizePolicy(sizePolicy)
        self.groupBox_incrementcontrol.setObjectName("groupBox_incrementcontrol")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_incrementcontrol)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.doubleSpinBox_setincr = QtWidgets.QDoubleSpinBox(self.groupBox_incrementcontrol)
        self.doubleSpinBox_setincr.setMaximum(35.0)
        self.doubleSpinBox_setincr.setSingleStep(0.01)
        self.doubleSpinBox_setincr.setObjectName("doubleSpinBox_setincr")
        self.gridLayout_6.addWidget(self.doubleSpinBox_setincr, 2, 0, 1, 1)
        self.pushButton_setincr = QtWidgets.QPushButton(self.groupBox_incrementcontrol)
        self.pushButton_setincr.setObjectName("pushButton_setincr")
        self.gridLayout_6.addWidget(self.pushButton_setincr, 2, 1, 1, 1)
        self.pushButton_addincr = QtWidgets.QPushButton(self.groupBox_incrementcontrol)
        self.pushButton_addincr.setObjectName("pushButton_addincr")
        self.gridLayout_6.addWidget(self.pushButton_addincr, 3, 1, 1, 1)
        self.pushButton_subincr = QtWidgets.QPushButton(self.groupBox_incrementcontrol)
        self.pushButton_subincr.setObjectName("pushButton_subincr")
        self.gridLayout_6.addWidget(self.pushButton_subincr, 3, 0, 1, 1)
        self.radio_currinc = QtWidgets.QRadioButton(self.groupBox_incrementcontrol)
        self.radio_currinc.setChecked(True)
        self.radio_currinc.setObjectName("radio_currinc")
        self.gridLayout_6.addWidget(self.radio_currinc, 0, 0, 1, 1)
        self.radio_voltinc = QtWidgets.QRadioButton(self.groupBox_incrementcontrol)
        self.radio_voltinc.setObjectName("radio_voltinc")
        self.gridLayout_6.addWidget(self.radio_voltinc, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_incrementcontrol, 1, 2, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.groupBox_channelcontrol)
        self.groupBox_automaticcurrentramp = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_automaticcurrentramp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_automaticcurrentramp.sizePolicy().hasHeightForWidth())
        self.groupBox_automaticcurrentramp.setSizePolicy(sizePolicy)
        self.groupBox_automaticcurrentramp.setObjectName("groupBox_automaticcurrentramp")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_automaticcurrentramp)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_automaticcontrol = QtWidgets.QCheckBox(self.groupBox_automaticcurrentramp)
        self.checkBox_automaticcontrol.setEnabled(True)
        self.checkBox_automaticcontrol.setObjectName("checkBox_automaticcontrol")
        self.verticalLayout_4.addWidget(self.checkBox_automaticcontrol)
        self.tabWidget_autocontrol = QtWidgets.QTabWidget(self.groupBox_automaticcurrentramp)
        self.tabWidget_autocontrol.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_autocontrol.sizePolicy().hasHeightForWidth())
        self.tabWidget_autocontrol.setSizePolicy(sizePolicy)
        self.tabWidget_autocontrol.setObjectName("tabWidget_autocontrol")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_target = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_target.setDecimals(3)
        self.doubleSpinBox_target.setSingleStep(0.01)
        self.doubleSpinBox_target.setProperty("value", 0.3)
        self.doubleSpinBox_target.setObjectName("doubleSpinBox_target")
        self.gridLayout.addWidget(self.doubleSpinBox_target, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.doubleSpinBox_autoincr = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_autoincr.setDecimals(3)
        self.doubleSpinBox_autoincr.setSingleStep(0.01)
        self.doubleSpinBox_autoincr.setProperty("value", 0.001)
        self.doubleSpinBox_autoincr.setObjectName("doubleSpinBox_autoincr")
        self.gridLayout.addWidget(self.doubleSpinBox_autoincr, 1, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.spinBox_dwell = QtWidgets.QSpinBox(self.tab)
        self.spinBox_dwell.setMaximum(1000)
        self.spinBox_dwell.setProperty("value", 200)
        self.spinBox_dwell.setObjectName("spinBox_dwell")
        self.gridLayout.addWidget(self.spinBox_dwell, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 2)
        self.pushButton_startramp = QtWidgets.QPushButton(self.tab)
        self.pushButton_startramp.setObjectName("pushButton_startramp")
        self.gridLayout.addWidget(self.pushButton_startramp, 3, 0, 1, 3)
        self.tabWidget_autocontrol.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_smoothtarget = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_smoothtarget.setMaximum(5.0)
        self.doubleSpinBox_smoothtarget.setSingleStep(0.01)
        self.doubleSpinBox_smoothtarget.setProperty("value", 1.0)
        self.doubleSpinBox_smoothtarget.setObjectName("doubleSpinBox_smoothtarget")
        self.gridLayout_3.addWidget(self.doubleSpinBox_smoothtarget, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)
        self.doubleSpinBox_smoothrate = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_smoothrate.setDecimals(3)
        self.doubleSpinBox_smoothrate.setMinimum(0.001)
        self.doubleSpinBox_smoothrate.setMaximum(100.0)
        self.doubleSpinBox_smoothrate.setProperty("value", 1.0)
        self.doubleSpinBox_smoothrate.setObjectName("doubleSpinBox_smoothrate")
        self.gridLayout_3.addWidget(self.doubleSpinBox_smoothrate, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.spinBox_smoothdwell = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_smoothdwell.setMinimum(1)
        self.spinBox_smoothdwell.setMaximum(1000)
        self.spinBox_smoothdwell.setProperty("value", 100)
        self.spinBox_smoothdwell.setObjectName("spinBox_smoothdwell")
        self.gridLayout_3.addWidget(self.spinBox_smoothdwell, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)
        self.pushButton_smoothrampstart = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_smoothrampstart.setObjectName("pushButton_smoothrampstart")
        self.gridLayout_3.addWidget(self.pushButton_smoothrampstart, 3, 0, 1, 1)
        self.pushButton_showtrajectorie = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_showtrajectorie.setObjectName("pushButton_showtrajectorie")
        self.gridLayout_3.addWidget(self.pushButton_showtrajectorie, 3, 1, 1, 1)
        self.tabWidget_autocontrol.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 1, 2, 1, 1)
        self.spinBox_lindwell = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_lindwell.setMinimum(1)
        self.spinBox_lindwell.setMaximum(1000)
        self.spinBox_lindwell.setProperty("value", 10)
        self.spinBox_lindwell.setObjectName("spinBox_lindwell")
        self.gridLayout_4.addWidget(self.spinBox_lindwell, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 2, 1, 1)
        self.pushButton_linrampstart = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_linrampstart.setObjectName("pushButton_linrampstart")
        self.gridLayout_4.addWidget(self.pushButton_linrampstart, 4, 0, 1, 1)
        self.pushButton_linrampshowtrajectory = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_linrampshowtrajectory.setObjectName("pushButton_linrampshowtrajectory")
        self.gridLayout_4.addWidget(self.pushButton_linrampshowtrajectory, 4, 2, 1, 1)
        self.doubleSpinBox_lintarget = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_lintarget.setDecimals(3)
        self.doubleSpinBox_lintarget.setProperty("value", 1.0)
        self.doubleSpinBox_lintarget.setObjectName("doubleSpinBox_lintarget")
        self.gridLayout_4.addWidget(self.doubleSpinBox_lintarget, 0, 0, 1, 1)
        self.doubleSpinBox_linrate = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_linrate.setDecimals(3)
        self.doubleSpinBox_linrate.setProperty("value", 1.0)
        self.doubleSpinBox_linrate.setObjectName("doubleSpinBox_linrate")
        self.gridLayout_4.addWidget(self.doubleSpinBox_linrate, 1, 0, 1, 1)
        self.tabWidget_autocontrol.addTab(self.tab_3, "")
        self.verticalLayout_4.addWidget(self.tabWidget_autocontrol)
        self.verticalLayout_3.addWidget(self.groupBox_automaticcurrentramp)
        self.horizontalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plot_1 = PlotWidget(self.widget_3)
        self.plot_1.setMinimumSize(QtCore.QSize(300, 0))
        self.plot_1.setObjectName("plot_1")
        self.verticalLayout_2.addWidget(self.plot_1)
        self.plot_2 = PlotWidget(self.widget_3)
        self.plot_2.setObjectName("plot_2")
        self.verticalLayout_2.addWidget(self.plot_2)
        self.plot_3 = PlotWidget(self.widget_3)
        self.plot_3.setEnabled(True)
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
        self.tabWidget_autocontrol.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Curernt Control by A.tom"))
        self.groupBox.setTitle(_translate("MainWindow", "Device Connection"))
        self.label.setText(_translate("MainWindow", "Resource Name"))
        self.checkBox_connect.setText(_translate("MainWindow", "Connect"))
        self.lineEdit_resource.setText(_translate("MainWindow", "TCPIP0::169.254.70.222::9221::SOCKET"))
        self.label_deviceName.setText(_translate("MainWindow", "<connected to>"))
        self.groupBox_lcd.setTitle(_translate("MainWindow", "Device Status - Measured Values!"))
        self.label_2.setText(_translate("MainWindow", "Voltage"))
        self.label_6.setText(_translate("MainWindow", "Voltage"))
        self.label_3.setText(_translate("MainWindow", "Current"))
        self.label_4.setText(_translate("MainWindow", "Voltage"))
        self.label_7.setText(_translate("MainWindow", "Current"))
        self.label_5.setText(_translate("MainWindow", "Current"))
        self.label_chan1.setText(_translate("MainWindow", "CH1"))
        self.label_chan2.setText(_translate("MainWindow", "CH2"))
        self.label_chan3.setText(_translate("MainWindow", "CH3"))
        self.groupBox_channelcontrol.setTitle(_translate("MainWindow", "Channel Control"))
        self.comboBox_channel.setCurrentText(_translate("MainWindow", "Channel 1"))
        self.comboBox_channel.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.comboBox_channel.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.comboBox_channel.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.checkBox_output.setText(_translate("MainWindow", "Output ON/OFF"))
        self.groupBox_outputcontrol.setTitle(_translate("MainWindow", "Output Control"))
        self.radio_cv1.setText(_translate("MainWindow", "Voltage"))
        self.pushButton_setval.setText(_translate("MainWindow", "Set"))
        self.radio_cc1.setText(_translate("MainWindow", "Current"))
        self.groupBox_incrementcontrol.setTitle(_translate("MainWindow", "Incremental Control"))
        self.pushButton_setincr.setText(_translate("MainWindow", "Set step"))
        self.pushButton_addincr.setText(_translate("MainWindow", "increment (+)"))
        self.pushButton_subincr.setText(_translate("MainWindow", "decrement (-)"))
        self.radio_currinc.setText(_translate("MainWindow", "Current"))
        self.radio_voltinc.setText(_translate("MainWindow", "Voltage"))
        self.groupBox_automaticcurrentramp.setTitle(_translate("MainWindow", "Automatic Current Ramp"))
        self.checkBox_automaticcontrol.setText(_translate("MainWindow", "Automatic Control"))
        self.label_9.setText(_translate("MainWindow", "Target (A)"))
        self.label_8.setText(_translate("MainWindow", "Inc. (A)"))
        self.label_10.setText(_translate("MainWindow", "Dwell (ms)"))
        self.pushButton_startramp.setText(_translate("MainWindow", "Ramp"))
        self.tabWidget_autocontrol.setTabText(self.tabWidget_autocontrol.indexOf(self.tab), _translate("MainWindow", "Increment"))
        self.label_11.setText(_translate("MainWindow", "Target Current (A)"))
        self.label_12.setText(_translate("MainWindow", "Rate (A/min)"))
        self.label_13.setText(_translate("MainWindow", "Dwell (ms)"))
        self.pushButton_smoothrampstart.setText(_translate("MainWindow", "Start Ramp"))
        self.pushButton_showtrajectorie.setText(_translate("MainWindow", "Preview Trajectory"))
        self.tabWidget_autocontrol.setTabText(self.tabWidget_autocontrol.indexOf(self.tab_2), _translate("MainWindow", "Smooth  Edge Lin"))
        self.label_14.setText(_translate("MainWindow", "Target Current (A)"))
        self.label_15.setText(_translate("MainWindow", "Rate (A/min)"))
        self.label_16.setText(_translate("MainWindow", "Dwell (ms)"))
        self.pushButton_linrampstart.setText(_translate("MainWindow", "Start Ramp"))
        self.pushButton_linrampshowtrajectory.setText(_translate("MainWindow", "Preview Trajectory"))
        self.tabWidget_autocontrol.setTabText(self.tabWidget_autocontrol.indexOf(self.tab_3), _translate("MainWindow", "Lin"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
