from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("push button")
        self.setMinimumSize(500, 200)

        button = QPushButton("click me")
        button.clicked.connect(self.btn_clicked)
        button.pressed.connect(self.btn_pressed)
        button.released.connect(self.btn_realeased)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def btn_clicked(self):
        print("clicked")
    def btn_pressed(self):
        print("pressed")
    def btn_realeased(self):
        print("released")
    