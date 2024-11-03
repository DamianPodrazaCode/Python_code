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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_TopForm(object):
    def setupUi(self, TopForm):
        if not TopForm.objectName():
            TopForm.setObjectName(u"TopForm")
        TopForm.resize(771, 173)
        self.gridLayout = QGridLayout(TopForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.twSerial = QTreeWidget(TopForm)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.twSerial.setHeaderItem(__qtreewidgetitem)
        self.twSerial.setObjectName(u"twSerial")

        self.verticalLayout_2.addWidget(self.twSerial)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbScanSerial = QPushButton(TopForm)
        self.pbScanSerial.setObjectName(u"pbScanSerial")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbScanSerial.sizePolicy().hasHeightForWidth())
        self.pbScanSerial.setSizePolicy(sizePolicy)
        self.pbScanSerial.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pbScanSerial)

        self.pbConnectSerial = QPushButton(TopForm)
        self.pbConnectSerial.setObjectName(u"pbConnectSerial")
        sizePolicy.setHeightForWidth(self.pbConnectSerial.sizePolicy().hasHeightForWidth())
        self.pbConnectSerial.setSizePolicy(sizePolicy)
        self.pbConnectSerial.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pbConnectSerial)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(TopForm)

        QMetaObject.connectSlotsByName(TopForm)
    # setupUi

    def retranslateUi(self, TopForm):
        TopForm.setWindowTitle(QCoreApplication.translate("TopForm", u"Super Serial", None))
        self.pbScanSerial.setText(QCoreApplication.translate("TopForm", u"Scan Serial", None))
        self.pbConnectSerial.setText(QCoreApplication.translate("TopForm", u"Connect Serial", None))
    # retranslateUi

