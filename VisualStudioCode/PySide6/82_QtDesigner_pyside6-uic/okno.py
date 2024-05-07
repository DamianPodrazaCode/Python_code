from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_okno import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('ok ok ok ...')
        self.pb_submit.clicked.connect(self.do_somthing)

    def do_somthing(self):
        print(self.le_full_name.text(), 'is a ', self.le_occupation.text())
