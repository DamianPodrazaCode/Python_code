# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_buttonsFjeANF.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(272, 122)
        Form.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_lock = QPushButton(Form)
        self.pb_lock.setObjectName(u"pb_lock")
        self.pb_lock.setCheckable(True)

        self.gridLayout.addWidget(self.pb_lock, 0, 0, 1, 1)

        self.pb_exit = QPushButton(Form)
        self.pb_exit.setObjectName(u"pb_exit")

        self.gridLayout.addWidget(self.pb_exit, 0, 1, 1, 1)

        self.vl_choice = QVBoxLayout()
        self.vl_choice.setObjectName(u"vl_choice")
        self.rb_choice1 = QRadioButton(Form)
        self.rb_choice1.setObjectName(u"rb_choice1")

        self.vl_choice.addWidget(self.rb_choice1)

        self.rb_choice2 = QRadioButton(Form)
        self.rb_choice2.setObjectName(u"rb_choice2")

        self.vl_choice.addWidget(self.rb_choice2)

        self.rb_choice3 = QRadioButton(Form)
        self.rb_choice3.setObjectName(u"rb_choice3")

        self.vl_choice.addWidget(self.rb_choice3)


        self.gridLayout.addLayout(self.vl_choice, 1, 0, 1, 1)

        self.vl_check = QVBoxLayout()
        self.vl_check.setObjectName(u"vl_check")
        self.cb_check1 = QCheckBox(Form)
        self.cb_check1.setObjectName(u"cb_check1")

        self.vl_check.addWidget(self.cb_check1)

        self.cb_check2 = QCheckBox(Form)
        self.cb_check2.setObjectName(u"cb_check2")

        self.vl_check.addWidget(self.cb_check2)

        self.cb_check3 = QCheckBox(Form)
        self.cb_check3.setObjectName(u"cb_check3")

        self.vl_check.addWidget(self.cb_check3)


        self.gridLayout.addLayout(self.vl_check, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Buttons", None))
        self.pb_lock.setText(QCoreApplication.translate("Form", u"Lock", None))
        self.pb_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.rb_choice1.setText(QCoreApplication.translate("Form", u"Choice 1", None))
        self.rb_choice2.setText(QCoreApplication.translate("Form", u"Choise 2", None))
        self.rb_choice3.setText(QCoreApplication.translate("Form", u"Choise 3", None))
        self.cb_check1.setText(QCoreApplication.translate("Form", u"Check 1", None))
        self.cb_check2.setText(QCoreApplication.translate("Form", u"Check 2", None))
        self.cb_check3.setText(QCoreApplication.translate("Form", u"Check 3", None))
    # retranslateUi

