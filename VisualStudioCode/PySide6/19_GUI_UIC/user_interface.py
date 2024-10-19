from PySide6 import QtCore, QtWidgets # noqa F401
from PySide6.QtUiTools import QUiLoader # noqa F401

loader = QUiLoader()

class UserInterface(QtCore.QObject) :
    def __init__(self) :
        super().__init__()
        self.ui = loader.load("gui.ui", None)
        self.ui.pb_submit.clicked.connect(self.doSomting)

    def show(self):
        self.ui.show()

    def doSomting(self) :
        print("okokok!!!")
