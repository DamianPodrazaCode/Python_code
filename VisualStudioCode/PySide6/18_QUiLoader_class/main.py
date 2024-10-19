import sys
from PySide6 import QtWidgets #noqa
from user_interface import UserInterface #noqa

app = QtWidgets.QApplication(sys.argv)

window = UserInterface()
window.show()

app.exec()
