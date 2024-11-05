import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtSerialPort import QSerialPortInfo
from mainWindow import Ui_MainWindow
# ------------------------------------------------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.scanTriger()

        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.readSettings()

        self.aScan.triggered.connect(self.scanTriger)
        self.aPortInfo.triggered.connect(self.portInfoTriger)
        self.aHelp.triggered.connect(self.helpTriger)
        self.aAbout.triggered.connect(self.aboutTriger)

        self.pbConnect.clicked.connect(self.connectClick)
        self.cbBaudRate.currentIndexChanged.connect(self.baudRatecurrentIndexChanged)
# ------------------------------------------------------------------------------------------------------
    def scanTriger(self) :
        self.cbSerial.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports : 
            self.cbSerial.addItem(port.portName())

    def portInfoTriger(self) :
        msgBox = QMessageBox() 
        msgBox.setWindowTitle("Serial port info") 
        ports = QSerialPortInfo.availablePorts()
        index = self.cbSerial.currentIndex()
        d1 = "Port Name : " + str(ports[index].portName()) + "\n"
        d2 = "Description : " + str(ports[index].description()) + "\n"
        d3 = "Manufacturer : " + str(ports[index].manufacturer()) + "\n"
        d4 = "Serial Number : " + str(ports[index].serialNumber()) + "\n"
        d5 = "System Location : " + str(ports[index].systemLocation()) + "\n" 
        d6 = "PID : " + str(ports[index].productIdentifier()) + "\n" 
        d7 = "VID : " + str(ports[index].vendorIdentifier()) 
        msgBox.setText(d1 + d2 + d3 + d4 + d5 + d6 + d7) 
        msgBox.setStandardButtons(QMessageBox.Ok) 
        msgBox.exec()

    def helpTriger(self) :
        print("helpTriger")

    def aboutTriger(self) :
        print("aboutTriger")
# ------------------------------------------------------------------------------------------------------
    def readSettings(self) :
        self.leBaudRate.setText(self.settings.value("leBaudRate"))
        self.cbDataBits.setCurrentIndex(self.settings.value("cbDataBits", 0, type=int))
        self.cbParity.setCurrentIndex(self.settings.value("cbParity", 0, type=int))
        self.cbStopBits.setCurrentIndex(self.settings.value("cbStopBits", 0, type=int))
        self.cbFlowControl.setCurrentIndex(self.settings.value("cbFlowControl", 0, type=int))

    def writeSettings(self) :
        self.settings.setValue("leBaudRate", self.leBaudRate.text())
        self.settings.setValue("cbDataBits", self.cbDataBits.currentIndex())
        self.settings.setValue("cbParity", self.cbParity.currentIndex())
        self.settings.setValue("cbStopBits", self.cbStopBits.currentIndex())
        self.settings.setValue("cbFlowControl", self.cbFlowControl.currentIndex())
# ------------------------------------------------------------------------------------------------------
    def connectClick(self) :
        if self.pbConnect.text() == "Connect" :
            self.pbConnect.setText("Disconnect")
        else :
            self.pbConnect.setText("Connect")

        self.writeSettings()
    
    def baudRatecurrentIndexChanged(self) :
        # print("baudRatecurrentIndexChanged")
        self.leBaudRate.setText(self.cbBaudRate.currentText())
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
    def closeEvent(self, event) :
        self.writeSettings()
        print("close Top Window")
# ------------------------------------------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
# ------------------------------------------------------------------------------------------------------
