from PySide6.QtWidgets import QApplication
from topForm import mainWindow
import sys

app = QApplication(sys.argv)

widget = mainWindow()
widget.show()

app.exec()
