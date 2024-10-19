from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy  # noqa: F401

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid layout")
        # self.setMinimumSize(800, 800)

        pb_one = QPushButton("One")
        pb_two = QPushButton("Two")
        pb_three = QPushButton("Three")
        pb_four = QPushButton("Four")
        pb_five = QPushButton("Five")
        pb_six = QPushButton("Six")
        pb_seven = QPushButton("Seven")

        pb_three.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        grid_layout = QGridLayout()
        grid_layout.addWidget(pb_one, 0, 0)
        grid_layout.addWidget(pb_two, 0, 1, 1, 2)
        grid_layout.addWidget(pb_three, 1, 0, 2, 1)
        grid_layout.addWidget(pb_four, 1, 1)
        grid_layout.addWidget(pb_five, 1, 2)
        grid_layout.addWidget(pb_six, 2, 1)
        grid_layout.addWidget(pb_seven, 2, 2)

        self.setLayout(grid_layout)
        