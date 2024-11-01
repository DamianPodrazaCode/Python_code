from PySide6.QtWidgets import QWidget 
from ui_topForm import Ui_TopForm 

from serialForm import serialPortWindow

class mainWindow(QWidget, Ui_TopForm) :
    def __init__(self) :
        super().__init__()

        self.windowsSerial = []
        self.windowsPort = []

        self.setupUi(self)

        self.pbScanSerial.clicked.connect(self.pbScanSerial_clicked)
        self.pbConnectSerial.clicked.connect(self.pbConnectSerial_clicked)
        self.pbScanPort.clicked.connect(self.pbScanPort_clicked)
        self.pbConnectPort.clicked.connect(self.pbConnectPort_clicked)
       

    def pbScanSerial_clicked(self) :
        print("pbScanSerial_clicked")
        print(len(self.windowsSerial))
        if len(self.windowsSerial) > 0 :
            self.windowsSerial.pop(0)

    def pbConnectSerial_clicked(self) :
        print("pbConnectSerial_clicked")
        serial = serialPortWindow()
        serial.show()
        self.windowsSerial.append(serial)

    def pbScanPort_clicked(self) :
        print("pbScanPort_clicked")

    def pbConnectPort_clicked(self) :
        print("pbConnectPort_clicked")
        
    def closeEvent(self, event) :
        print("closeWindow")
        self.windowsSerial.clear()        