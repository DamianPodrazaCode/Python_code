# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oknoqTstBq.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt) #noqa F401
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform) #noqa F401
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget) #noqa F401

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(417, 102)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_full_name = QLabel(Widget)
        self.l_full_name.setObjectName(u"l_full_name")

        self.horizontalLayout.addWidget(self.l_full_name)

        self.le_full_name = QLineEdit(Widget)
        self.le_full_name.setObjectName(u"le_full_name")

        self.horizontalLayout.addWidget(self.le_full_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_occupation = QLabel(Widget)
        self.l_occupation.setObjectName(u"l_occupation")

        self.horizontalLayout_2.addWidget(self.l_occupation)

        self.le_occupation = QLineEdit(Widget)
        self.le_occupation.setObjectName(u"le_occupation")

        self.horizontalLayout_2.addWidget(self.le_occupation)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pb_submit = QPushButton(Widget)
        self.pb_submit.setObjectName(u"pb_submit")

        self.verticalLayout.addWidget(self.pb_submit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Firs Widget", None))
        self.l_full_name.setText(QCoreApplication.translate("Widget", u"Full name:", None))
        self.l_occupation.setText(QCoreApplication.translate("Widget", u"Occupation :", None))
        self.pb_submit.setText(QCoreApplication.translate("Widget", u"Submit", None))
    # retranslateUi

