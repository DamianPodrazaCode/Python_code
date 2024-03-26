import sys
from PySide6 import QtWidgets
from Dialog import Okno

app = QtWidgets.QApplication(sys.argv)

window = Okno()
window.show()

app.exec()