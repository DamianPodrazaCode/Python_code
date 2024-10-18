from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout  # noqa: F401

class RockWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TITLE")

        button1 = QPushButton("BUtton1")        
        button2 = QPushButton("BUtton2")

        button1.clicked.connect(self.btn1_clicked)
        button2.clicked.connect(self.btn2_clicked)

        # button_layout = QHBoxLayout()
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)        
        button_layout.addWidget(button2)
        
        self.setLayout(button_layout)

    def btn1_clicked(self):
        print("button1 clicked")        
    
    def btn2_clicked(self):
        print("button2 clicked")        