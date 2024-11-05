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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.label = QLabel(self.gbConnect)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

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

        self.label_2 = QLabel(self.gbConnect)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

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

        self.label_3 = QLabel(self.gbConnect)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

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

        self.label_4 = QLabel(self.gbConnect)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

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

        self.label_5 = QLabel(self.gbConnect)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

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
        sizePolicy.setHeightForWidth(self.gbWrite.sizePolicy().hasHeightForWidth())
        self.gbWrite.setSizePolicy(sizePolicy)
        self.gbWrite.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.gbWrite)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.gbWrite)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.comboBox_2 = QComboBox(self.gbWrite)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.pushButton = QPushButton(self.gbWrite)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.gbWrite)

        self.gbRead = QGroupBox(self.centralwidget)
        self.gbRead.setObjectName(u"gbRead")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gbRead.sizePolicy().hasHeightForWidth())
        self.gbRead.setSizePolicy(sizePolicy2)
        self.gbRead.setFlat(True)
        self.plainTextEdit = QPlainTextEdit(self.gbRead)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 20, 781, 331))

        self.verticalLayout.addWidget(self.gbRead)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Baud rate", None))
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

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data bits", None))
        self.cbDataBits.setItemText(0, QCoreApplication.translate("MainWindow", u"Data5", None))
        self.cbDataBits.setItemText(1, QCoreApplication.translate("MainWindow", u"Data6", None))
        self.cbDataBits.setItemText(2, QCoreApplication.translate("MainWindow", u"Data7", None))
        self.cbDataBits.setItemText(3, QCoreApplication.translate("MainWindow", u"Data8", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.cbParity.setItemText(0, QCoreApplication.translate("MainWindow", u"NoParity", None))
        self.cbParity.setItemText(1, QCoreApplication.translate("MainWindow", u"EvenParity", None))
        self.cbParity.setItemText(2, QCoreApplication.translate("MainWindow", u"OddParity", None))
        self.cbParity.setItemText(3, QCoreApplication.translate("MainWindow", u"SpaceParity", None))
        self.cbParity.setItemText(4, QCoreApplication.translate("MainWindow", u"MarkParity", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stop bits", None))
        self.cbStopBits.setItemText(0, QCoreApplication.translate("MainWindow", u"OneStop", None))
        self.cbStopBits.setItemText(1, QCoreApplication.translate("MainWindow", u"OneAndHalfStop", None))
        self.cbStopBits.setItemText(2, QCoreApplication.translate("MainWindow", u"TwoStop", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Flow control", None))
        self.cbFlowControl.setItemText(0, QCoreApplication.translate("MainWindow", u"NoFlowControl", None))
        self.cbFlowControl.setItemText(1, QCoreApplication.translate("MainWindow", u"HardwareControl", None))
        self.cbFlowControl.setItemText(2, QCoreApplication.translate("MainWindow", u"SoftwareControl", None))

        self.gbWrite.setTitle(QCoreApplication.translate("MainWindow", u"Write", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.gbRead.setTitle(QCoreApplication.translate("MainWindow", u"Read", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

