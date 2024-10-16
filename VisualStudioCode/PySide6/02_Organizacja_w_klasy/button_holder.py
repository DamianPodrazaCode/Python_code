from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        button = QPushButton("OK")
        self.setCentralWidget(button)
        button.clicked.connect(self.doSomting)
       
    def doSomting(self):
        print("ok!!!")