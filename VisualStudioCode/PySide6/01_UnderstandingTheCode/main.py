from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

def doSomting():
    print("ok ok ok !!!")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('FirstApp')

button = QPushButton()
button.setText('ok')

button.clicked.connect(doSomting)

window.setCentralWidget(button)

window.show()
app.exec()