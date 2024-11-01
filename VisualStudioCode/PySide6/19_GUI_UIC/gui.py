from PySide6.QtCore import Qt # noqa F401
from PySide6.QtWidgets import QWidget # noqa F401
from ui_gui import Ui_Gui # noqa F401

class Gui(QWidget, Ui_Gui) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.pb_submit.clicked.connect(self.doSomting)

    def doSomting(self) :
        print("okokok!!!")
