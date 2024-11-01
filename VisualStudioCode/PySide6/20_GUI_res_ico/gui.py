from PySide6.QtCore import Qt # noqa F401
from PySide6.QtWidgets import QWidget # noqa F401
from ui_gui import Ui_Gui # noqa F401

class Gui(QWidget, Ui_Gui) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        self.sb_show.setValue(50)
        self.pb_plus.clicked.connect(self.plus)
        self.pb_minus.clicked.connect(self.minus)

    def plus(self) :
        value = self.sb_show.value()
        self.sb_show.setValue(value + 1)

    def minus(self) :
        value = self.sb_show.value()
        self.sb_show.setValue(value - 1)
        