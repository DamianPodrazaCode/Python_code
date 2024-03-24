from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('FirstApp')

button = QPushButton()
button.setText('ok')

window.setCentralWidget(button)

window.show()
app.exec()