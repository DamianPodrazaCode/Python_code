# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 707)
        self.aScan = QAction(MainWindow)
        self.aScan.setObjectName(u"aScan")
        self.aScan.setMenuRole(QAction.MenuRole.NoRole)
        self.aPortInfo = QAction(MainWindow)
        self.aPortInfo.setObjectName(u"aPortInfo")
        self.aPortInfo.setMenuRole(QAction.MenuRole.NoRole)
        self.aHelp = QAction(MainWindow)
        self.aHelp.setObjectName(u"aHelp")
        self.aHelp.setMenuRole(QAction.MenuRole.NoRole)
        self.aAbout = QAction(MainWindow)
        self.aAbout.setObjectName(u"aAbout")
        self.aAbout.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gbConnect = QGroupBox(self.centralwidget)
        self.gbConnect.setObjectName(u"gbConnect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbConnect.sizePolicy().hasHeightForWidth())
        self.gbConnect.setSizePolicy(sizePolicy)
        self.gbConnect.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gbConnect.setFlat(True)
        self.gbConnect.setCheckable(False)
        self.lyConnect = QGridLayout(self.gbConnect)
        self.lyConnect.setObjectName(u"lyConnect")
        self.lyConnect.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbSerial = QComboBox(self.gbConnect)
        self.cbSerial.addItem("")
        self.cbSerial.setObjectName(u"cbSerial")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbSerial.sizePolicy().hasHeightForWidth())
        self.cbSerial.setSizePolicy(sizePolicy1)
        self.cbSerial.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.cbSerial)

        self.pbConnect = QPushButton(self.gbConnect)
        self.pbConnect.setObjectName(u"pbConnect")

        self.horizontalLayout.addWidget(self.pbConnect)

        self.line = QFrame(self.gbConnect)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.lBaudRaste = QLabel(self.gbConnect)
        self.lBaudRaste.setObjectName(u"lBaudRaste")

        self.horizontalLayout.addWidget(self.lBaudRaste)

        self.leBaudRate = QLineEdit(self.gbConnect)
        self.leBaudRate.setObjectName(u"leBaudRate")
        sizePolicy1.setHeightForWidth(self.leBaudRate.sizePolicy().hasHeightForWidth())
        self.leBaudRate.setSizePolicy(sizePolicy1)
        self.leBaudRate.setMaximumSize(QSize(80, 16777215))
        self.leBaudRate.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.horizontalLayout.addWidget(self.leBaudRate)

        self.cbBaudRate = QComboBox(self.gbConnect)
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.addItem("")
        self.cbBaudRate.setObjectName(u"cbBaudRate")
        sizePolicy1.setHeightForWidth(self.cbBaudRate.sizePolicy().hasHeightForWidth())
        self.cbBaudRate.setSizePolicy(sizePolicy1)
        self.cbBaudRate.setMinimumSize(QSize(70, 0))
        self.cbBaudRate.setAutoFillBackground(False)
        self.cbBaudRate.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.cbBaudRate.setEditable(False)

        self.horizontalLayout.addWidget(self.cbBaudRate)

        self.line_2 = QFrame(self.gbConnect)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.lDataBits = QLabel(self.gbConnect)
        self.lDataBits.setObjectName(u"lDataBits")

        self.horizontalLayout.addWidget(self.lDataBits)

        self.cbDataBits = QComboBox(self.gbConnect)
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.setObjectName(u"cbDataBits")

        self.horizontalLayout.addWidget(self.cbDataBits)

        self.line_3 = QFrame(self.gbConnect)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.lParity = QLabel(self.gbConnect)
        self.lParity.setObjectName(u"lParity")

        self.horizontalLayout.addWidget(self.lParity)

        self.cbParity = QComboBox(self.gbConnect)
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.setObjectName(u"cbParity")

        self.horizontalLayout.addWidget(self.cbParity)

        self.line_4 = QFrame(self.gbConnect)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.lStopBits = QLabel(self.gbConnect)
        self.lStopBits.setObjectName(u"lStopBits")

        self.horizontalLayout.addWidget(self.lStopBits)

        self.cbStopBits = QComboBox(self.gbConnect)
        self.cbStopBits.addItem("")
        self.cbStopBits.addItem("")
        self.cbStopBits.addItem("")
        self.cbStopBits.setObjectName(u"cbStopBits")

        self.horizontalLayout.addWidget(self.cbStopBits)

        self.line_5 = QFrame(self.gbConnect)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.lFlowControl = QLabel(self.gbConnect)
        self.lFlowControl.setObjectName(u"lFlowControl")

        self.horizontalLayout.addWidget(self.lFlowControl)

        self.cbFlowControl = QComboBox(self.gbConnect)
        self.cbFlowControl.addItem("")
        self.cbFlowControl.addItem("")
        self.cbFlowControl.addItem("")
        self.cbFlowControl.setObjectName(u"cbFlowControl")

        self.horizontalLayout.addWidget(self.cbFlowControl)


        self.lyConnect.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lyConnect.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.gbConnect)

        self.gbWrite = QGroupBox(self.centralwidget)
        self.gbWrite.setObjectName(u"gbWrite")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gbWrite.sizePolicy().hasHeightForWidth())
        self.gbWrite.setSizePolicy(sizePolicy2)
        self.gbWrite.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.gbWrite)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leSend = QLineEdit(self.gbWrite)
        self.leSend.setObjectName(u"leSend")

        self.horizontalLayout_2.addWidget(self.leSend)

        self.cbSendEoL = QComboBox(self.gbWrite)
        self.cbSendEoL.addItem("")
        self.cbSendEoL.addItem("")
        self.cbSendEoL.addItem("")
        self.cbSendEoL.addItem("")
        self.cbSendEoL.setObjectName(u"cbSendEoL")

        self.horizontalLayout_2.addWidget(self.cbSendEoL)

        self.cbEchoSend = QCheckBox(self.gbWrite)
        self.cbEchoSend.setObjectName(u"cbEchoSend")

        self.horizontalLayout_2.addWidget(self.cbEchoSend)

        self.pbSend = QPushButton(self.gbWrite)
        self.pbSend.setObjectName(u"pbSend")

        self.horizontalLayout_2.addWidget(self.pbSend)

        self.pbDTR = QPushButton(self.gbWrite)
        self.pbDTR.setObjectName(u"pbDTR")
        self.pbDTR.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pbDTR)

        self.pbRTS = QPushButton(self.gbWrite)
        self.pbRTS.setObjectName(u"pbRTS")
        self.pbRTS.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pbRTS)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pbMacro1 = QPushButton(self.gbWrite)
        self.pbMacro1.setObjectName(u"pbMacro1")
        self.pbMacro1.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro1)

        self.pbMacro2 = QPushButton(self.gbWrite)
        self.pbMacro2.setObjectName(u"pbMacro2")
        self.pbMacro2.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro2)

        self.pbMacro3 = QPushButton(self.gbWrite)
        self.pbMacro3.setObjectName(u"pbMacro3")
        self.pbMacro3.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro3)

        self.pbMacro4 = QPushButton(self.gbWrite)
        self.pbMacro4.setObjectName(u"pbMacro4")
        self.pbMacro4.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro4)

        self.pbMacro5 = QPushButton(self.gbWrite)
        self.pbMacro5.setObjectName(u"pbMacro5")
        self.pbMacro5.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro5)

        self.pbMacro6 = QPushButton(self.gbWrite)
        self.pbMacro6.setObjectName(u"pbMacro6")
        self.pbMacro6.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro6)

        self.pbMacro7 = QPushButton(self.gbWrite)
        self.pbMacro7.setObjectName(u"pbMacro7")
        self.pbMacro7.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro7)

        self.pbMacro8 = QPushButton(self.gbWrite)
        self.pbMacro8.setObjectName(u"pbMacro8")
        self.pbMacro8.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro8)

        self.pbMacro9 = QPushButton(self.gbWrite)
        self.pbMacro9.setObjectName(u"pbMacro9")
        self.pbMacro9.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro9)

        self.pbMacro10 = QPushButton(self.gbWrite)
        self.pbMacro10.setObjectName(u"pbMacro10")
        self.pbMacro10.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.horizontalLayout_4.addWidget(self.pbMacro10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.gbWrite)

        self.gbRead = QGroupBox(self.centralwidget)
        self.gbRead.setObjectName(u"gbRead")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gbRead.sizePolicy().hasHeightForWidth())
        self.gbRead.setSizePolicy(sizePolicy3)
        self.gbRead.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.gbRead)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pteReadSerial = QPlainTextEdit(self.gbRead)
        self.pteReadSerial.setObjectName(u"pteReadSerial")
        self.pteReadSerial.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.pteReadSerial.setOverwriteMode(False)
        self.pteReadSerial.setMaximumBlockCount(0)

        self.gridLayout_2.addWidget(self.pteReadSerial, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.gbRead)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbCTS = QCheckBox(self.groupBox)
        self.cbCTS.setObjectName(u"cbCTS")
        self.cbCTS.setEnabled(False)
        self.cbCTS.setCheckable(True)

        self.gridLayout.addWidget(self.cbCTS, 0, 0, 1, 1)

        self.cbCD = QCheckBox(self.groupBox)
        self.cbCD.setObjectName(u"cbCD")
        self.cbCD.setEnabled(False)
        self.cbCD.setCheckable(True)

        self.gridLayout.addWidget(self.cbCD, 0, 1, 1, 1)

        self.cbDSR = QCheckBox(self.groupBox)
        self.cbDSR.setObjectName(u"cbDSR")
        self.cbDSR.setEnabled(False)
        self.cbDSR.setCheckable(True)

        self.gridLayout.addWidget(self.cbDSR, 1, 0, 1, 1)

        self.cbRI = QCheckBox(self.groupBox)
        self.cbRI.setObjectName(u"cbRI")
        self.cbRI.setEnabled(False)
        self.cbRI.setCheckable(True)

        self.gridLayout.addWidget(self.cbRI, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.gbRead)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pbStartStopLog = QPushButton(self.groupBox_2)
        self.pbStartStopLog.setObjectName(u"pbStartStopLog")
        self.pbStartStopLog.setCheckable(True)

        self.gridLayout_3.addWidget(self.pbStartStopLog, 8, 0, 1, 1)

        self.pbAutoScroll = QPushButton(self.groupBox_2)
        self.pbAutoScroll.setObjectName(u"pbAutoScroll")

        self.gridLayout_3.addWidget(self.pbAutoScroll, 3, 0, 1, 1)

        self.pbClear = QPushButton(self.groupBox_2)
        self.pbClear.setObjectName(u"pbClear")

        self.gridLayout_3.addWidget(self.pbClear, 0, 0, 1, 1)

        self.pbSaveWindow = QPushButton(self.groupBox_2)
        self.pbSaveWindow.setObjectName(u"pbSaveWindow")

        self.gridLayout_3.addWidget(self.pbSaveWindow, 7, 0, 1, 1)

        self.cbTextEncode = QComboBox(self.groupBox_2)
        self.cbTextEncode.addItem("")
        self.cbTextEncode.addItem("")
        self.cbTextEncode.addItem("")
        self.cbTextEncode.addItem("")
        self.cbTextEncode.addItem("")
        self.cbTextEncode.addItem("")
        self.cbTextEncode.addItem("")
        self.cbTextEncode.setObjectName(u"cbTextEncode")

        self.gridLayout_3.addWidget(self.cbTextEncode, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.cbTime = QCheckBox(self.groupBox_2)
        self.cbTime.setObjectName(u"cbTime")

        self.gridLayout_3.addWidget(self.cbTime, 6, 0, 1, 1)

        self.cbWarp = QCheckBox(self.groupBox_2)
        self.cbWarp.setObjectName(u"cbWarp")

        self.gridLayout_3.addWidget(self.cbWarp, 1, 0, 1, 1)

        self.cb1Window = QCheckBox(self.groupBox_2)
        self.cb1Window.setObjectName(u"cb1Window")

        self.gridLayout_3.addWidget(self.cb1Window, 4, 0, 1, 1)

        self.cbIgnoreRN = QCheckBox(self.groupBox_2)
        self.cbIgnoreRN.setObjectName(u"cbIgnoreRN")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cbIgnoreRN.sizePolicy().hasHeightForWidth())
        self.cbIgnoreRN.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.cbIgnoreRN, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.gbRead)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.aScan)
        self.toolBar.addAction(self.aPortInfo)
        self.toolBar.addAction(self.aHelp)
        self.toolBar.addAction(self.aAbout)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Terminal by ZoMbiE", None))
        self.aScan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.aPortInfo.setText(QCoreApplication.translate("MainWindow", u"Port info", None))
        self.aHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.gbConnect.setTitle(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.cbSerial.setItemText(0, QCoreApplication.translate("MainWindow", u"COM ##", None))

        self.pbConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.lBaudRaste.setText(QCoreApplication.translate("MainWindow", u"Baud rate", None))
        self.cbBaudRate.setItemText(0, QCoreApplication.translate("MainWindow", u"300", None))
        self.cbBaudRate.setItemText(1, QCoreApplication.translate("MainWindow", u"600", None))
        self.cbBaudRate.setItemText(2, QCoreApplication.translate("MainWindow", u"1200", None))
        self.cbBaudRate.setItemText(3, QCoreApplication.translate("MainWindow", u"2400", None))
        self.cbBaudRate.setItemText(4, QCoreApplication.translate("MainWindow", u"4800", None))
        self.cbBaudRate.setItemText(5, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cbBaudRate.setItemText(6, QCoreApplication.translate("MainWindow", u"14400", None))
        self.cbBaudRate.setItemText(7, QCoreApplication.translate("MainWindow", u"19200", None))
        self.cbBaudRate.setItemText(8, QCoreApplication.translate("MainWindow", u"38400", None))
        self.cbBaudRate.setItemText(9, QCoreApplication.translate("MainWindow", u"115200", None))
        self.cbBaudRate.setItemText(10, QCoreApplication.translate("MainWindow", u"230400", None))
        self.cbBaudRate.setItemText(11, QCoreApplication.translate("MainWindow", u"460800", None))
        self.cbBaudRate.setItemText(12, QCoreApplication.translate("MainWindow", u"921600", None))

        self.lDataBits.setText(QCoreApplication.translate("MainWindow", u"Data bits", None))
        self.cbDataBits.setItemText(0, QCoreApplication.translate("MainWindow", u"Data5", None))
        self.cbDataBits.setItemText(1, QCoreApplication.translate("MainWindow", u"Data6", None))
        self.cbDataBits.setItemText(2, QCoreApplication.translate("MainWindow", u"Data7", None))
        self.cbDataBits.setItemText(3, QCoreApplication.translate("MainWindow", u"Data8", None))

        self.lParity.setText(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.cbParity.setItemText(0, QCoreApplication.translate("MainWindow", u"NoParity", None))
        self.cbParity.setItemText(1, QCoreApplication.translate("MainWindow", u"EvenParity", None))
        self.cbParity.setItemText(2, QCoreApplication.translate("MainWindow", u"OddParity", None))
        self.cbParity.setItemText(3, QCoreApplication.translate("MainWindow", u"SpaceParity", None))
        self.cbParity.setItemText(4, QCoreApplication.translate("MainWindow", u"MarkParity", None))

        self.lStopBits.setText(QCoreApplication.translate("MainWindow", u"Stop bits", None))
        self.cbStopBits.setItemText(0, QCoreApplication.translate("MainWindow", u"OneStop", None))
        self.cbStopBits.setItemText(1, QCoreApplication.translate("MainWindow", u"OneAndHalfStop", None))
        self.cbStopBits.setItemText(2, QCoreApplication.translate("MainWindow", u"TwoStop", None))

        self.lFlowControl.setText(QCoreApplication.translate("MainWindow", u"Flow control", None))
        self.cbFlowControl.setItemText(0, QCoreApplication.translate("MainWindow", u"NoFlowControl", None))
        self.cbFlowControl.setItemText(1, QCoreApplication.translate("MainWindow", u"HardwareControl", None))
        self.cbFlowControl.setItemText(2, QCoreApplication.translate("MainWindow", u"SoftwareControl", None))

        self.gbWrite.setTitle(QCoreApplication.translate("MainWindow", u"Write", None))
        self.cbSendEoL.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cbSendEoL.setItemText(1, QCoreApplication.translate("MainWindow", u"\\n", None))
        self.cbSendEoL.setItemText(2, QCoreApplication.translate("MainWindow", u"\\r", None))
        self.cbSendEoL.setItemText(3, QCoreApplication.translate("MainWindow", u"\\r\\n", None))

        self.cbEchoSend.setText(QCoreApplication.translate("MainWindow", u"Echo", None))
        self.pbSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.pbDTR.setText(QCoreApplication.translate("MainWindow", u"DTR", None))
        self.pbRTS.setText(QCoreApplication.translate("MainWindow", u"RTS", None))
        self.pbMacro1.setText(QCoreApplication.translate("MainWindow", u"Macro 1", None))
        self.pbMacro2.setText(QCoreApplication.translate("MainWindow", u"Macro 2", None))
        self.pbMacro3.setText(QCoreApplication.translate("MainWindow", u"Macro 3", None))
        self.pbMacro4.setText(QCoreApplication.translate("MainWindow", u"Macro 4", None))
        self.pbMacro5.setText(QCoreApplication.translate("MainWindow", u"Macro 5", None))
        self.pbMacro6.setText(QCoreApplication.translate("MainWindow", u"Macro 6", None))
        self.pbMacro7.setText(QCoreApplication.translate("MainWindow", u"Macro 7", None))
        self.pbMacro8.setText(QCoreApplication.translate("MainWindow", u"Macro 8", None))
        self.pbMacro9.setText(QCoreApplication.translate("MainWindow", u"Macro 9", None))
        self.pbMacro10.setText(QCoreApplication.translate("MainWindow", u"Macro 10", None))
        self.gbRead.setTitle(QCoreApplication.translate("MainWindow", u"Read", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input signals", None))
        self.cbCTS.setText(QCoreApplication.translate("MainWindow", u"CTS", None))
        self.cbCD.setText(QCoreApplication.translate("MainWindow", u"CD", None))
        self.cbDSR.setText(QCoreApplication.translate("MainWindow", u"DSR", None))
        self.cbRI.setText(QCoreApplication.translate("MainWindow", u"RI", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Reading settings", None))
        self.pbStartStopLog.setText(QCoreApplication.translate("MainWindow", u"Start log", None))
        self.pbAutoScroll.setText(QCoreApplication.translate("MainWindow", u"Auto scroll", None))
        self.pbClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pbSaveWindow.setText(QCoreApplication.translate("MainWindow", u"Save window", None))
        self.cbTextEncode.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.cbTextEncode.setItemText(1, QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.cbTextEncode.setItemText(2, QCoreApplication.translate("MainWindow", u"iso-8859-1", None))
        self.cbTextEncode.setItemText(3, QCoreApplication.translate("MainWindow", u"UTF-16", None))
        self.cbTextEncode.setItemText(4, QCoreApplication.translate("MainWindow", u"UTF-32", None))
        self.cbTextEncode.setItemText(5, QCoreApplication.translate("MainWindow", u"HEX", None))
        self.cbTextEncode.setItemText(6, QCoreApplication.translate("MainWindow", u"BIN", None))

        self.cbTime.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.cbWarp.setText(QCoreApplication.translate("MainWindow", u"Warp", None))
        self.cb1Window.setText(QCoreApplication.translate("MainWindow", u"1 window", None))
        self.cbIgnoreRN.setText(QCoreApplication.translate("MainWindow", u"Ingnore \\r\\n", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

