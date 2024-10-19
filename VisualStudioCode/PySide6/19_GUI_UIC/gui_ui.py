# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(239, 121)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(Widget)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_occ = QLineEdit(Widget)
        self.le_occ.setObjectName(u"le_occ")

        self.horizontalLayout_2.addWidget(self.le_occ)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pb_submit = QPushButton(Widget)
        self.pb_submit.setObjectName(u"pb_submit")

        self.verticalLayout.addWidget(self.pb_submit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"QT Designer QWidget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Full name:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Occupation :", None))
        self.pb_submit.setText(QCoreApplication.translate("Widget", u"Submit", None))
    # retranslateUi

