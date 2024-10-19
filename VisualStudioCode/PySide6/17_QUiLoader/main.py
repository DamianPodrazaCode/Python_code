from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import sys

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("gui.ui", None)

def doSomting() :
    print("okokok!!!")

window.pb_submit.clicked.connect(doSomting)
window.show()
app.exec()
