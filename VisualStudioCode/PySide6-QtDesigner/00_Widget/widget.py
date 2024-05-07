from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_Widget import Ui_Form  # import klasy wygenerowanej z QtDesigner (ui_Widget.py)

class Okno(QWidget, Ui_Form): # wszystkie widgety dziedziczone z Ui_Form
    def __init__(self):
        super().__init__()
        self.setupUi(self) # z dziedziczenia, inicjalizacja okna
