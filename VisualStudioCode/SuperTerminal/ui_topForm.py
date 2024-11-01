# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'topForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_TopForm(object):
    def setupUi(self, TopForm):
        if not TopForm.objectName():
            TopForm.setObjectName(u"TopForm")
        TopForm.resize(820, 393)
        self.gridLayout = QGridLayout(TopForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbScanSerial = QPushButton(TopForm)
        self.pbScanSerial.setObjectName(u"pbScanSerial")

        self.horizontalLayout.addWidget(self.pbScanSerial)

        self.pbConnectSerial = QPushButton(TopForm)
        self.pbConnectSerial.setObjectName(u"pbConnectSerial")

        self.horizontalLayout.addWidget(self.pbConnectSerial)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.twSerial = QTreeWidget(TopForm)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.twSerial.setHeaderItem(__qtreewidgetitem)
        self.twSerial.setObjectName(u"twSerial")

        self.verticalLayout_2.addWidget(self.twSerial)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.line = QFrame(TopForm)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pbScanPort = QPushButton(TopForm)
        self.pbScanPort.setObjectName(u"pbScanPort")

        self.horizontalLayout_2.addWidget(self.pbScanPort)

        self.pbConnectPort = QPushButton(TopForm)
        self.pbConnectPort.setObjectName(u"pbConnectPort")

        self.horizontalLayout_2.addWidget(self.pbConnectPort)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.leRefFreq = QLineEdit(TopForm)
        self.leRefFreq.setObjectName(u"leRefFreq")
        self.leRefFreq.setMinimumSize(QSize(0, 0))
        self.leRefFreq.setMaximumSize(QSize(40, 16777215))
        self.leRefFreq.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.leRefFreq)

        self.label = QLabel(TopForm)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lePortNumber = QLineEdit(TopForm)
        self.lePortNumber.setObjectName(u"lePortNumber")
        self.lePortNumber.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lePortNumber)

        self.label_2 = QLabel(TopForm)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.twPort = QTreeWidget(TopForm)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.twPort.setHeaderItem(__qtreewidgetitem1)
        self.twPort.setObjectName(u"twPort")

        self.verticalLayout_3.addWidget(self.twPort)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(TopForm)

        QMetaObject.connectSlotsByName(TopForm)
    # setupUi

    def retranslateUi(self, TopForm):
        TopForm.setWindowTitle(QCoreApplication.translate("TopForm", u"Super Serial", None))
        self.pbScanSerial.setText(QCoreApplication.translate("TopForm", u"Scan Serial", None))
        self.pbConnectSerial.setText(QCoreApplication.translate("TopForm", u"Connect Serial", None))
        self.pbScanPort.setText(QCoreApplication.translate("TopForm", u"Scan Port", None))
        self.pbConnectPort.setText(QCoreApplication.translate("TopForm", u"Connect Port", None))
        self.label.setText(QCoreApplication.translate("TopForm", u"Ref. Freq. [ms]", None))
        self.label_2.setText(QCoreApplication.translate("TopForm", u"Port Number", None))
    # retranslateUi

