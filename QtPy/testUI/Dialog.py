from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_Dialog import Ui_Dialog

class Okno(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_print.clicked.connect(self.slot_pb_print_clicked)
        # self.setWindowTitle('ok ok ok ...')
        # self.pb_submit.clicked.connect(self.do_somthing)

    def slot_pb_print_clicked(self):
        print('pb_print kliknięty')

    # def do_somthing(self):
    #     print(self.le_full_name.text(), 'is a ', self.le_occupation.text())