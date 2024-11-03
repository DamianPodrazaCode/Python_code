from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem
from ui_topForm import Ui_TopForm 
from serialForm import serialPortWindow
import serial.tools.list_ports

class mainWindow(QWidget, Ui_TopForm) :
    def __init__(self) :
        super().__init__()

        self.windowsSerial = []

        self.setupUi(self)

        self.twSerial.setHeaderLabels(["Device", "Description", "Manufacturer", "Hwid"])
        self.pbScanSerial_clicked()

        self.pbScanSerial.clicked.connect(self.pbScanSerial_clicked)
        self.pbConnectSerial.clicked.connect(self.pbConnectSerial_clicked)
        self.twSerial.itemClicked.connect(self.treeItem)
       
    def pbScanSerial_clicked(self) :
        self.twSerial.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports : 
            item = QTreeWidgetItem([port.device, port.description, port.manufacturer, port.hwid])        
            self.twSerial.addTopLevelItem(item) 
        for column in range(self.twSerial.columnCount()) :  
            self.twSerial.resizeColumnToContents(column)    
        if self.twSerial.topLevelItemCount() > 0 :
            self.twSerial.setCurrentItem(self.twSerial.topLevelItem(0))


    def pbConnectSerial_clicked(self) :
        serial = serialPortWindow(self.twSerial.currentItem().text(0))
        serial.show()
        self.windowsSerial.append(serial)
        
    def closeEvent(self, event) :
        print("closeWindow")
        self.windowsSerial.clear()        

    def treeItem(self, itemIndex) :
        pass
        # print(itemIndex.text(0))

