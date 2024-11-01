# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'portForm.ui'
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

class Ui_PortForm(object):
    def setupUi(self, PortForm):
        if not PortForm.objectName():
            PortForm.setObjectName(u"PortForm")
        PortForm.resize(400, 300)

        self.retranslateUi(PortForm)

        QMetaObject.connectSlotsByName(PortForm)
    # setupUi

    def retranslateUi(self, PortForm):
        PortForm.setWindowTitle(QCoreApplication.translate("PortForm", u"Connected to port ###", None))
    # retranslateUi

