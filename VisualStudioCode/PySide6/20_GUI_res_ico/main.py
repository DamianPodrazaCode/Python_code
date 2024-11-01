import sys
from PySide6 import QtWidgets #noqa
from gui import Gui #noqa

app = QtWidgets.QApplication(sys.argv)

window = Gui()
window.show()

app.exec()
