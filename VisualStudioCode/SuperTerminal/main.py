from PySide6.QtWidgets import QApplication
from ui_topForm import Ui_TopForm
import sys

app = QApplication(sys.argv)

widget = Ui_TopForm()
widget.show()

app.exec()
