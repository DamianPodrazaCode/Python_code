import sys
from PySide6.QtWidgets import QApplication, QWidget 
from ui_serialForm import Ui_SerialForm 

class serialPortWindow(QWidget, Ui_SerialForm) :
    def __init__(self, portName, bautRate, dataBits, parity, stopBits, flowControl) :
        super().__init__()
        self.portName = portName
        self.bautRate = bautRate
        self.dataBits = dataBits
        self.parity = parity
        self.stopBits = stopBits
        self.flowControl = flowControl
        self.setupUi(self)
        self.setWindowTitle(self.portName)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = serialPortWindow(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    window.show()
    sys.exit(app.exec())
