import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, QIODevice, QIODeviceBase
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
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
        self.cbBaudRate.currentIndexChanged.connect(self.baudRateCurrentIndexChanged)
        self.leBaudRate.returnPressed.connect(self.baudRateReturnPressed)
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

            self.serialPort = QSerialPort(self)
            self.serialPort.readyRead.connect(self.readData)
            self.serialPort.setPortName(self.cbSerial.currentText())
            self.serialPort.setBaudRate(int(self.leBaudRate.text()))
            self.serialPort.setDataBits(getattr(QSerialPort, self.cbDataBits.currentText(), None))
            self.serialPort.setParity(getattr(QSerialPort, self.cbParity.currentText(), None))
            self.serialPort.setStopBits(getattr(QSerialPort, self.cbStopBits.currentText(), None))
            self.serialPort.setFlowControl(getattr(QSerialPort, self.cbFlowControl.currentText(), None))
            self.serialPort.open(QSerialPort.OpenModeFlag.ReadWrite)

        else :
            self.pbConnect.setText("Connect")
            if self.serialPort.isOpen() :
                self.serialPort.close()

        self.writeSettings()
    
    def baudRateCurrentIndexChanged(self) :
        self.leBaudRate.setText(self.cbBaudRate.currentText())
        if self.serialPort.isOpen() :
            self.serialPort.setBaudRate(int(self.leBaudRate.text()))
    
    def baudRateReturnPressed(self) :
        if self.serialPort.isOpen() :
            self.serialPort.setBaudRate(int(self.leBaudRate.text()))
       
# ------------------------------------------------------------------------------------------------------
    def readData(self) : 
        while self.serialPort.canReadLine() : 
            data = self.serialPort.readLine().data().decode().rstrip()
            self.pteReadSerial.appendPlainText(data)
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
        if self.serialPort.isOpen() :
            self.serialPort.close()
        print("close Top Window")
# ------------------------------------------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
# ------------------------------------------------------------------------------------------------------
