# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connectForm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ConnectForm(object):
    def setupUi(self, ConnectForm):
        if not ConnectForm.objectName():
            ConnectForm.setObjectName(u"ConnectForm")
        ConnectForm.resize(259, 194)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectForm.sizePolicy().hasHeightForWidth())
        ConnectForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ConnectForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ConnectForm)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.leBautRate = QLineEdit(ConnectForm)
        self.leBautRate.setObjectName(u"leBautRate")

        self.horizontalLayout.addWidget(self.leBautRate)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(ConnectForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.cbDataBits = QComboBox(ConnectForm)
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.setObjectName(u"cbDataBits")

        self.horizontalLayout_2.addWidget(self.cbDataBits)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(ConnectForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.cbParity = QComboBox(ConnectForm)
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.setObjectName(u"cbParity")

        self.horizontalLayout_3.addWidget(self.cbParity)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(ConnectForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.cbStopBits = QComboBox(ConnectForm)
        self.cbStopBits.addItem("")
        self.cbStopBits.addItem("")
        self.cbStopBits.addItem("")
        self.cbStopBits.setObjectName(u"cbStopBits")

        self.horizontalLayout_4.addWidget(self.cbStopBits)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(ConnectForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.cbFlowControl = QComboBox(ConnectForm)
        self.cbFlowControl.addItem("")
        self.cbFlowControl.addItem("")
        self.cbFlowControl.addItem("")
        self.cbFlowControl.setObjectName(u"cbFlowControl")

        self.horizontalLayout_5.addWidget(self.cbFlowControl)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.pbConnect = QPushButton(ConnectForm)
        self.pbConnect.setObjectName(u"pbConnect")

        self.horizontalLayout_6.addWidget(self.pbConnect)

        self.pbCancel = QPushButton(ConnectForm)
        self.pbCancel.setObjectName(u"pbCancel")

        self.horizontalLayout_6.addWidget(self.pbCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(ConnectForm)

        QMetaObject.connectSlotsByName(ConnectForm)
    # setupUi

    def retranslateUi(self, ConnectForm):
        ConnectForm.setWindowTitle(QCoreApplication.translate("ConnectForm", u"COM ###", None))
        self.label.setText(QCoreApplication.translate("ConnectForm", u"Baut Rate", None))
        self.leBautRate.setText(QCoreApplication.translate("ConnectForm", u"9600", None))
        self.label_2.setText(QCoreApplication.translate("ConnectForm", u"Data Bits", None))
        self.cbDataBits.setItemText(0, QCoreApplication.translate("ConnectForm", u"Data8", None))
        self.cbDataBits.setItemText(1, QCoreApplication.translate("ConnectForm", u"Data7", None))
        self.cbDataBits.setItemText(2, QCoreApplication.translate("ConnectForm", u"Data6", None))
        self.cbDataBits.setItemText(3, QCoreApplication.translate("ConnectForm", u"Data5", None))

        self.label_3.setText(QCoreApplication.translate("ConnectForm", u"Parity", None))
        self.cbParity.setItemText(0, QCoreApplication.translate("ConnectForm", u"NoParity", None))
        self.cbParity.setItemText(1, QCoreApplication.translate("ConnectForm", u"EvenParity", None))
        self.cbParity.setItemText(2, QCoreApplication.translate("ConnectForm", u"OddParity", None))
        self.cbParity.setItemText(3, QCoreApplication.translate("ConnectForm", u"SpaceParity", None))
        self.cbParity.setItemText(4, QCoreApplication.translate("ConnectForm", u"MarkParity", None))

        self.label_4.setText(QCoreApplication.translate("ConnectForm", u"Stop Bits", None))
        self.cbStopBits.setItemText(0, QCoreApplication.translate("ConnectForm", u"OneStop", None))
        self.cbStopBits.setItemText(1, QCoreApplication.translate("ConnectForm", u"OneAndHalfStop", None))
        self.cbStopBits.setItemText(2, QCoreApplication.translate("ConnectForm", u"TwoStop", None))

        self.label_5.setText(QCoreApplication.translate("ConnectForm", u"Flow Control", None))
        self.cbFlowControl.setItemText(0, QCoreApplication.translate("ConnectForm", u"NoFlowControl", None))
        self.cbFlowControl.setItemText(1, QCoreApplication.translate("ConnectForm", u"HardwareControl", None))
        self.cbFlowControl.setItemText(2, QCoreApplication.translate("ConnectForm", u"SoftwareControl", None))

        self.pbConnect.setText(QCoreApplication.translate("ConnectForm", u"Connect", None))
        self.pbCancel.setText(QCoreApplication.translate("ConnectForm", u"Cancel", None))
    # retranslateUi

