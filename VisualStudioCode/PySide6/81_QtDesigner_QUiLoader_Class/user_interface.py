from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject): 
    def __init__(self):
        super().__init__()
        self.ui = loader.load('okno.ui', None)
        self.ui.setWindowTitle('ok ok ok ...')
        self.ui.pb_submit.clicked.connect(self.do_somthing)
    def show(self):
        self.ui.show()
    def do_somthing(self):
        print(self.ui.le_full_name.text(), 'is a ', self.ui.le_occupation.text())


