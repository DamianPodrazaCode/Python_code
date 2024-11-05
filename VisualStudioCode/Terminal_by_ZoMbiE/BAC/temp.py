import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Odczytywanie Ustawień Portu Szeregowego")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.button = QPushButton("Odczytaj Ustawienia")
        self.button.clicked.connect(self.read_settings)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.serial_port = QSerialPort()
        self.serial_port.setPortName("COM3")
        self.serial_port.setBaudRate(QSerialPort.Baud9600)
        self.serial_port.setDataBits(QSerialPort.Data8)
        self.serial_port.setParity(QSerialPort.NoParity)
        self.serial_port.setStopBits(QSerialPort.OneStop)
        self.serial_port.setFlowControl(QSerialPort.NoFlowControl)

    def read_settings(self):
        if self.serial_port.isOpen():
            settings = (
                f"Port: {self.serial_port.portName()}\n"
                f"Baud Rate: {self.serial_port.baudRate()}\n"
                f"Data Bits: {self.serial_port.dataBits()}\n"
                f"Parity: {self.serial_port.parity()}\n"
                f"Stop Bits: {self.serial_port.stopBits()}\n"
                f"Flow Control: {self.serial_port.flowControl()}\n"
            )
            self.text_edit.append(settings)
        else:
            self.text_edit.append("Port nie jest otwarty")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
