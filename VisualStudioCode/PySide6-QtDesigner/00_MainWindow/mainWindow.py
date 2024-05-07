from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow
from ui_MainWindow import Ui_MainWindow  # import klasy wygenerowanej z QtDesigner (ui_MainWindow.py)

class Okno(QMainWindow, Ui_MainWindow): # wszystkie widgety dziedziczone z Ui_MainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self) # z dziedziczenia, inicjalizacja okna
