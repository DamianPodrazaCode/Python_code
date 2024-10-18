
from PySide6.QtWidgets import QApplication
from rockwidget import RockWidget
import sys

app = QApplication(sys.argv)

widget = RockWidget()
widget.show()

# window = QWidget()
# window.show()

app.exec()
