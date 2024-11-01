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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resource_rc

class Ui_Gui(object):
    def setupUi(self, Gui):
        if not Gui.objectName():
            Gui.setObjectName(u"Gui")
        Gui.resize(555, 42)
        self.horizontalLayout = QHBoxLayout(Gui)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_minus = QPushButton(Gui)
        self.pb_minus.setObjectName(u"pb_minus")
        icon = QIcon()
        icon.addFile(u":/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_minus.setIcon(icon)

        self.horizontalLayout.addWidget(self.pb_minus)

        self.sb_show = QSpinBox(Gui)
        self.sb_show.setObjectName(u"sb_show")

        self.horizontalLayout.addWidget(self.sb_show)

        self.pb_plus = QPushButton(Gui)
        self.pb_plus.setObjectName(u"pb_plus")
        icon1 = QIcon()
        icon1.addFile(u":/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_plus.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pb_plus)


        self.retranslateUi(Gui)

        QMetaObject.connectSlotsByName(Gui)
    # setupUi

    def retranslateUi(self, Gui):
        Gui.setWindowTitle(QCoreApplication.translate("Gui", u"Resource_designer", None))
        self.pb_minus.setText(QCoreApplication.translate("Gui", u"minus", None))
        self.pb_plus.setText(QCoreApplication.translate("Gui", u"plus", None))
    # retranslateUi

