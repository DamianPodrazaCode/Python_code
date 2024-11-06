from PySide6.QtCore import Signal
from PySide6.QtWidgets import  QVBoxLayout, QWidget, QPushButton, QLineEdit, QDialog

class MacroWindow(QDialog):
    macroSubmitted = Signal(str)  # Definiowanie sygnału, który wyśle tekst do głównego okna

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit macro.")
        self.setGeometry(150, 150, 300, 50)

        self.leNewMacro = QLineEdit()
        self.leNewMacro.setPlaceholderText("")
        self.leNewMacro.returnPressed.connect(self.submitMacro)

        layout = QVBoxLayout()
        layout.addWidget(self.leNewMacro)
        self.setLayout(layout)

    def submitMacro(self):
        text = self.leNewMacro.text()
        self.macroSubmitted.emit(text)  # Emitowanie sygnału z tekstem
        self.accept()  # Zamknięcie okna dialogowego