import sys
from PySide6 import QtWidgets 
from gui import Gui 

app = QtWidgets.QApplication(sys.argv)

window = Gui()
window.show()

app.exec()
