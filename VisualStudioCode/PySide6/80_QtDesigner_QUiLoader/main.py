import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load('okno.ui', None)

def do_somthing():
    print(window.le_full_name.text(), 'is a ', window.le_occupation.text())

window.setWindowTitle('ok ok ok ...')

window.pb_submit.clicked.connect(do_somthing)
window.show()

app.exec()