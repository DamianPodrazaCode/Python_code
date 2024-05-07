from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_buttons import Ui_Form  # import klasy wygenerowanej z QtDesigner (ui_Widget.py)

class Okno(QWidget, Ui_Form): # wszystkie widgety dziedziczone z Ui_Form
    def __init__(self):
        super().__init__()
        self.setupUi(self) # z dziedziczenia, inicjalizacja okna
        self.pb_exit.clicked.connect(self.f_pb_exit)
        self.rb_choice2.setChecked(True)
        self.pb_lock.clicked.connect(self.f_pb_lock)
        self.pb_lock.toggled.connect(self.f_pb_lock_toggle)

    def f_pb_exit(self):
        print('f_pb_exit')
        self.close()

    def f_pb_lock(self, check):
        if check:
            print('click lock')
            self.pb_lock.setText('unLock')
            self.rb_choice1.setEnabled(False)            
            self.rb_choice2.setEnabled(False)            
            self.rb_choice3.setEnabled(False)            
        else:
            print('click unlock')
            self.pb_lock.setText('Lock')
            self.rb_choice1.setEnabled(True)            
            self.rb_choice2.setEnabled(True)            
            self.rb_choice3.setEnabled(True)            

    def f_pb_lock_toggle(self, check):
            print('toggle', check)