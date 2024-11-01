# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serialForm.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_SerialForm(object):
    def setupUi(self, SerialForm):
        if not SerialForm.objectName():
            SerialForm.setObjectName(u"SerialForm")
        SerialForm.resize(400, 300)

        self.retranslateUi(SerialForm)

        QMetaObject.connectSlotsByName(SerialForm)
    # setupUi

    def retranslateUi(self, SerialForm):
        SerialForm.setWindowTitle(QCoreApplication.translate("SerialForm", u"Connected to serial port ###", None))
    # retranslateUi

