from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Size policies and stretches")
        # self.setMinimumSize(800, 800)

        l_some_text = QLabel("Some text:")
        le_edit = QLineEdit()
        h_layout = QHBoxLayout()
        h_layout.addWidget(l_some_text)
        h_layout.addWidget(le_edit)

        pb_one = QPushButton("One")
        pb_two = QPushButton("Two")
        pb_three = QPushButton("Three")
        hb_layout = QHBoxLayout()
        hb_layout.addWidget(pb_one, 2) # drugi parametr to stretches
        hb_layout.addWidget(pb_two, 1)
        hb_layout.addWidget(pb_three, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(hb_layout)

        self.setLayout(v_layout)
        
        # le_edit.setSizePolicy(zachowanie w X, zachowanie w Y)
        le_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # le_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_some_text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # pb_one.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # pb_two.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # pb_three.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        