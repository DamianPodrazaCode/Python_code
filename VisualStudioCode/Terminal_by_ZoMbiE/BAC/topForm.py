from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
from PySide6.QtCore import QIODevice, Signal, Slot
from sympy import false
from ui_topForm import Ui_TopForm 
from connectForm import connectPortWindow

class mainWindow(QWidget, Ui_TopForm) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self) # setup onka z designera

        self.windowsConnect = [] # lista obiektów z nowym oknem

        self.twSerial.setHeaderLabels(["Port Name", "Description", "Manufacturer", "Serial Number", "System Location", "PID", "VID"])
        self.pbScanSerial_clicked()

        self.pbScanSerial.clicked.connect(self.pbScanSerial_clicked)
        self.pbConnectSerial.clicked.connect(self.pbConnectSerial_clicked)
        self.twSerial.itemClicked.connect(self.treeItem)
       
    def pbScanSerial_clicked(self) :
        self.twSerial.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports : 
            d1 = port.portName()
            d2 = port.description()
            d3 = port.manufacturer()
            d4 = port.serialNumber()
            d5 = port.systemLocation()
            d6 = port.productIdentifier()
            d7 = port.vendorIdentifier()
            item =  QTreeWidgetItem([d1, d2, d3, d4, d5, d6, d7])
            self.twSerial.addTopLevelItem(item) 
        for column in range(self.twSerial.columnCount()) :  
            self.twSerial.resizeColumnToContents(column)    
        if self.twSerial.topLevelItemCount() > 0 :
            self.twSerial.setCurrentItem(self.twSerial.topLevelItem(0))
            self.pbConnectSerial.setEnabled(True)
        else :
            self.pbConnectSerial.setEnabled(False)

    def pbConnectSerial_clicked(self) :
        connect = connectPortWindow(self.twSerial.currentItem().text(0))
        connect.show()
        self.windowsConnect.append(connect)
        
    def closeEvent(self, event) :
        print("close Top Window")
        self.windowsConnect.clear()        

    def treeItem(self, itemIndex) :
        pass
        # print(itemIndex.text(0))

