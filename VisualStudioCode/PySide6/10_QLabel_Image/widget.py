from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel & Image")
        self.setMinimumSize(800, 800)

        image_label = QLabel()
        image_label.setPixmap(QPixmap("image.jpeg"))

        layout_img = QVBoxLayout()
        layout_img.addWidget(image_label)

        self.setLayout(layout_img)