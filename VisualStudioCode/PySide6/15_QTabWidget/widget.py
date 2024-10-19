from PySide6.QtWidgets import QWidget, QTabWidget, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QAbstractItemView # noqa: F401

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tab widget")
        # self.setMinimumSize(800, 800)

