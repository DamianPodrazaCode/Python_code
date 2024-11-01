from PySide6.QtWidgets import QWidget 
from ui_serialForm import Ui_SerialForm 

class serialPortWindow(QWidget, Ui_SerialForm) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)