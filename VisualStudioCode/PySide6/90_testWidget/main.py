import sys
from PySide6 import QtWidgets 
from PySide6.QtWidgets import QWidget
from widget import Ui_Form
# ------------------------------------------------------------------------------------------------------
class Widget(QWidget, Ui_Form) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv)
window = Widget()
window.show()
app.exec()
# ------------------------------------------------------------------------------------------------------
