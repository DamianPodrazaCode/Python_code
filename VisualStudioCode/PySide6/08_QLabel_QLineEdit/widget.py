from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("label and line edit")
        self.setMinimumSize(500, 100)

        l_name = QLabel("Full name:")
        le_name = QLineEdit()
        le_name.setMinimumWidth(400)

        layout_name = QHBoxLayout()
        layout_name.addWidget(l_name)
        layout_name.addWidget(le_name)

        button = QPushButton("click")
        l_out = QLabel("OUT")

        layout_all = QVBoxLayout()
        layout_all.addLayout(layout_name)
        layout_all.addWidget(button)
        layout_all.addWidget(l_out)

        self.setLayout(layout_all)