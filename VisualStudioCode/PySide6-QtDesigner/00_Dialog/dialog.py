from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_Dialog import Ui_Dialog  # import klasy wygenerowanej z QtDesigner (ui_Dialog.py)

class OknoDialog(QWidget, Ui_Dialog): # wszystkie widgety dziedziczone z Ui_Dialog
    def __init__(self):
        super().__init__()
        self.setupUi(self) # z dziedziczenia, inicjalizacja okna
