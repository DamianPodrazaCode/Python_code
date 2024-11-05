import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QIODevice, Signal, Slot
from PySide6.QtSerialPort import QSerialPort
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
        self.setWindowTitle("Connect to: " + self.portName)

        self.serialPort = QSerialPort(self)
        self.serialPort.readyRead.connect(self.readData)
        self.serialPort.setPortName(self.portName)
        self.serialPort.setBaudRate(int(self.bautRate))
        self.serialPort.setDataBits(getattr(QSerialPort, self.dataBits, None))
        self.serialPort.setParity(getattr(QSerialPort, self.parity, None))
        self.serialPort.setStopBits(getattr(QSerialPort, self.stopBits, None))
        self.serialPort.setFlowControl(getattr(QSerialPort, self.flowControl, None))

        if self.serialPort.open(QIODevice.ReadWrite) :
            pass
            # self.lwDebug.addItem("port otwarty")
        else : 
            msgBox = QMessageBox() 
            msgBox.setWindowTitle("Error") 
            msgBox.setText("Port is busy. !!!") 
            msgBox.setStandardButtons(QMessageBox.Ok) 
            msgBox.exec()
            sys.exit()

        # self.lwDebug.addItem(self.serialPort.portName())
        # self.lwDebug.addItem(str(self.serialPort.baudRate()))
        # self.lwDebug.addItem(str(self.serialPort.dataBits()))
        # self.lwDebug.addItem(str(self.serialPort.parity()))
        # self.lwDebug.addItem(str(self.serialPort.stopBits()))
        # self.lwDebug.addItem(str(self.serialPort.flowControl()))

        self.serialPort.open(QIODevice.ReadWrite) 

    def readData(self) : 
        while self.serialPort.canReadLine() : 
            data = self.serialPort.readLine().data().decode('utf-8').rstrip() 
            self.pteReadSerial.appendPlainText(data)

    def closeEvent(self, event) :
        print("Close Serial Form")
        self.serialPort.close()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = serialPortWindow(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    window.show()
    sys.exit(app.exec())
