from PySide6.QtWidgets import QWidget 
from ui_serialForm import Ui_SerialForm 

class serialPortWindow(QWidget, Ui_SerialForm) :
    def __init__(self, comNr) :
        super().__init__()
        self.comNr = comNr
        self.setupUi(self)
        self.setWindowTitle(self.comNr)