import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, QIODevice, Qt, QPoint, QTimer, QFile
from PySide6.QtWidgets import QMainWindow, QMessageBox, QMenu, QPlainTextEdit, QFileDialog
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
from mainWindow import Ui_MainWindow
from macroWindow import MacroWindow
from datetime import datetime

# ------------------------------------------------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()

        # inicjalizacja okna z QTDesigner
        self.setupUi(self)
        # pierwszy skan portów
        self.scanTriger()

        # obiekt ostawień i wczytanie z pliku ini
        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.readSettings()

        # obiekt serial
        self.serialPort = QSerialPort(self)

        # emity od paska pocznego
        self.aScan.triggered.connect(self.scanTriger)
        self.aPortInfo.triggered.connect(self.portInfoTriger)
        self.aHelp.triggered.connect(self.helpTriger)
        self.aAbout.triggered.connect(self.aboutTriger)

        # emity od połączenia z portem
        self.pbConnect.clicked.connect(self.connectClick)
        self.cbBaudRate.currentIndexChanged.connect(self.baudRateCurrentIndexChanged)
        self.leBaudRate.returnPressed.connect(self.baudRateReturnPressed)
        self.cbDataBits.currentIndexChanged.connect(self.dataBitsCurrentIndexChanged)
        self.cbParity.currentIndexChanged.connect(self.parityCurrentIndexChanged)
        self.cbStopBits.currentIndexChanged.connect(self.stopBitsCurrentIndexChanged)
        self.cbFlowControl.currentIndexChanged.connect(self.flowControlCurrentIndexChanged)

        # emity od wysyłania
        self.pbSend.clicked.connect(self.sendClicked)
        self.leSend.returnPressed.connect(self.sendReturnPressed)
        self.pbDTR.clicked.connect(self.DTRclicked)
        self.pbRTS.clicked.connect(self.RTSclicked)
        self.pbMacro1.clicked.connect(lambda: self.macroClicked(self.pbMacro1.text()))
        self.pbMacro2.clicked.connect(lambda: self.macroClicked(self.pbMacro2.text()))
        self.pbMacro3.clicked.connect(lambda: self.macroClicked(self.pbMacro3.text()))
        self.pbMacro4.clicked.connect(lambda: self.macroClicked(self.pbMacro4.text()))
        self.pbMacro5.clicked.connect(lambda: self.macroClicked(self.pbMacro5.text()))
        self.pbMacro6.clicked.connect(lambda: self.macroClicked(self.pbMacro6.text()))
        self.pbMacro7.clicked.connect(lambda: self.macroClicked(self.pbMacro7.text()))
        self.pbMacro8.clicked.connect(lambda: self.macroClicked(self.pbMacro8.text()))
        self.pbMacro9.clicked.connect(lambda: self.macroClicked(self.pbMacro9.text()))
        self.pbMacro10.clicked.connect(lambda: self.macroClicked(self.pbMacro10.text()))
        self.pbMacro1.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro1.mapToGlobal(QPoint(0,0)), self.pbMacro1))
        self.pbMacro2.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro2.mapToGlobal(QPoint(0,0)), self.pbMacro2))
        self.pbMacro3.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro3.mapToGlobal(QPoint(0,0)), self.pbMacro3))
        self.pbMacro4.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro4.mapToGlobal(QPoint(0,0)), self.pbMacro4))
        self.pbMacro5.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro5.mapToGlobal(QPoint(0,0)), self.pbMacro5))
        self.pbMacro6.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro6.mapToGlobal(QPoint(0,0)), self.pbMacro6))
        self.pbMacro7.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro7.mapToGlobal(QPoint(0,0)), self.pbMacro7))
        self.pbMacro8.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro8.mapToGlobal(QPoint(0,0)), self.pbMacro8))
        self.pbMacro9.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro9.mapToGlobal(QPoint(0,0)), self.pbMacro9))
        self.pbMacro10.customContextMenuRequested.connect(lambda: self.macroCustomContextMenuRequested(self.pbMacro10.mapToGlobal(QPoint(0,0)), self.pbMacro10))

        # timer potrzebny do nasłuchiwania sygnałów CTS, DSR, CD, RI
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkPinoutSerialInputSignals)
        self.timer.start(200) 

        # emity od odbierania
        self.pbClear.clicked.connect(self.clearClicked)
        self.cbWarp.checkStateChanged.connect(self.warpCheckStateChanged)
        self.cb1Window.checkStateChanged.connect(self.oneWindowCheckStateChanged)
        self.myEncode = self.cbTextEncode.currentText()
        self.cbTextEncode.currentIndexChanged.connect(self.textEncodeCurrentIndexChanged)
        self.pbSaveWindow.clicked.connect(self.saveWindowClicked)
        self.pbStartStopLog.clicked.connect(self.startStopLogClicked)
        
        # obiekt do zapisywania
        self.file = None

        # emit do stremingu danych do pliku        
        self.pteReadSerial.textChanged.connect(self.streamWrite)

# oddczyty i zapisy ustawień------------------------------------------------------------------------------------------------------
    def readSettings(self) :
        '''odczyt głównych ustawień'''
        self.leBaudRate.setText(self.settings.value("leBaudRate"))
        self.cbDataBits.setCurrentIndex(self.settings.value("cbDataBits", 0, type=int))
        self.cbParity.setCurrentIndex(self.settings.value("cbParity", 0, type=int))
        self.cbStopBits.setCurrentIndex(self.settings.value("cbStopBits", 0, type=int))
        self.cbFlowControl.setCurrentIndex(self.settings.value("cbFlowControl", 0, type=int))
        self.cbSendEoL.setCurrentIndex(self.settings.value("cbSendEoL", 0, type=int))
        self.cbEchoSend.setChecked(self.settings.value("cbEchoSend", 0, type=bool))
        self.pbMacro1.setText(self.settings.value("pbMacro1"))
        self.pbMacro2.setText(self.settings.value("pbMacro2"))
        self.pbMacro3.setText(self.settings.value("pbMacro3"))
        self.pbMacro4.setText(self.settings.value("pbMacro4"))
        self.pbMacro5.setText(self.settings.value("pbMacro5"))
        self.pbMacro6.setText(self.settings.value("pbMacro6"))
        self.pbMacro7.setText(self.settings.value("pbMacro7"))
        self.pbMacro8.setText(self.settings.value("pbMacro8"))
        self.pbMacro9.setText(self.settings.value("pbMacro9"))
        self.pbMacro10.setText(self.settings.value("pbMacro10"))
        self.cbWarp.setChecked(self.settings.value("cbWarp", 0, type=bool))
        self.cbIgnoreRN.setChecked(self.settings.value("cbIgnoreRN", 0, type=bool))
        self.cbAutoScroll.setChecked(self.settings.value("cbAutoScroll", 0, type=bool))
        self.cb1Window.setChecked(self.settings.value("cb1Window", 0, type=bool))
        self.cbTextEncode.setCurrentIndex(self.settings.value("cbTextEncode", 0, type=int))
        self.cbTime.setChecked(self.settings.value("cbTime", 0, type=bool))

    def writeSettings(self) :
        '''zapis głównych ustawień'''
        self.settings.setValue("leBaudRate", self.leBaudRate.text())
        self.settings.setValue("cbDataBits", self.cbDataBits.currentIndex())
        self.settings.setValue("cbParity", self.cbParity.currentIndex())
        self.settings.setValue("cbStopBits", self.cbStopBits.currentIndex())
        self.settings.setValue("cbFlowControl", self.cbFlowControl.currentIndex())
        self.settings.setValue("cbSendEoL", self.cbSendEoL.currentIndex())
        self.settings.setValue("cbEchoSend", self.cbEchoSend.isChecked())
        self.settings.setValue("pbMacro1", self.pbMacro1.text())
        self.settings.setValue("pbMacro2", self.pbMacro2.text())
        self.settings.setValue("pbMacro3", self.pbMacro3.text())
        self.settings.setValue("pbMacro4", self.pbMacro4.text())
        self.settings.setValue("pbMacro5", self.pbMacro5.text())
        self.settings.setValue("pbMacro6", self.pbMacro6.text())
        self.settings.setValue("pbMacro7", self.pbMacro7.text())
        self.settings.setValue("pbMacro8", self.pbMacro8.text())
        self.settings.setValue("pbMacro9", self.pbMacro9.text())
        self.settings.setValue("pbMacro10", self.pbMacro10.text())
        self.settings.setValue("cbWarp", self.cbWarp.isChecked())
        self.settings.setValue("cbIgnoreRN", self.cbIgnoreRN.isChecked())
        self.settings.setValue("cbAutoScroll", self.cbAutoScroll.isChecked())
        self.settings.setValue("cb1Window", self.cb1Window.isChecked())
        self.settings.setValue("cbTextEncode", self.cbTextEncode.currentIndex())
        self.settings.setValue("cbTime", self.cbTime.isChecked())

# panel boczny------------------------------------------------------------------------------------------------------
    def scanTriger(self) :
        '''Skanowanie w celu znalezienia serial portów, zapis do cbSerial'''
        self.cbSerial.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports : 
            self.cbSerial.addItem(port.portName())

    def portInfoTriger(self) :
        '''Info o serial porcie, dane wypiswane do messageBox-a'''
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
        msgBox = QMessageBox() 
        msgBox.setWindowTitle("Help ...") 
        msgBox.setText("Under construction....") 
        msgBox.setStandardButtons(QMessageBox.Ok) 
        msgBox.exec()

    def aboutTriger(self) :
        msgBox = QMessageBox() 
        msgBox.setWindowTitle("About ...") 
        d1 = "Author - Damian Podraza<br>"
        d2 = "Done in Visual Studio Code<br>"
        d3 = "Python, PySide6, Qt6, Qt Widgets Designer<br>"
        d4 = 'Source on <a href="https://github.com/DamianPodrazaCode/Python_code/tree/main/VisualStudioCode/Terminal_by_ZoMbiE">github</a>'
        msgBox.setText(d1 + d2 + d3 + d4) 
        msgBox.setTextFormat(Qt.RichText)
        msgBox.setStandardButtons(QMessageBox.Ok) 
        msgBox.exec()

# panel connect--------------------------------------------------------------------------------------------------------
    def connectClick(self) :
        '''przycisk connect, łączy z wybranym portem (cbSerial)'''
        if self.pbConnect.text() == "Connect" :
            self.pbConnect.setText("Disconnect")
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
        # inicjalizacja niektórych ustawień z kontrolek
        self.warpCheckStateChanged(self.cbWarp.checkState())
        self.oneWindowCheckStateChanged(self.cb1Window.checkState())
    
    def baudRateCurrentIndexChanged(self) :
        '''slot baud rate, zmiana w combo box'''
        self.leBaudRate.setText(self.cbBaudRate.currentText())
        self.serialPort.setBaudRate(int(self.leBaudRate.text()))
    
    def baudRateReturnPressed(self) :
        '''slot baud rate, przyciśnięcie enter w line edit'''
        self.serialPort.setBaudRate(int(self.leBaudRate.text()))

    def dataBitsCurrentIndexChanged(self) :
        self.serialPort.setDataBits(getattr(QSerialPort, self.cbDataBits.currentText(), None))

    def parityCurrentIndexChanged(self) :
        self.serialPort.setParity(getattr(QSerialPort, self.cbParity.currentText(), None))

    def stopBitsCurrentIndexChanged(self) :
        self.serialPort.setStopBits(getattr(QSerialPort, self.cbStopBits.currentText(), None))

    def flowControlCurrentIndexChanged(self) :
        self.serialPort.setFlowControl(getattr(QSerialPort, self.cbFlowControl.currentText(), None))

# panel write------------------------------------------------------------------------------------------------------
    def sendClicked(self) :
        '''wysyłąnie danych z line edit'''

        # wybór co ma być na końcu paczki do wysłania
        text = "error send"
        if self.cbSendEoL.currentText() == "None" :
            text = self.leSend.text()
        elif self.cbSendEoL.currentText() == "\\n" :
            text = self.leSend.text() + "\n"
        elif self.cbSendEoL.currentText() == "\\r" :
            text = self.leSend.text() + "\r"
        elif self.cbSendEoL.currentText() == "\\r\\n" :
            text = self.leSend.text() + "\r\n"

        # echo do okna odczytu
        if self.cbEchoSend.isChecked() :
            self.pteReadSerial.appendPlainText(text)

        # wysłąnie danych
        if text and self.serialPort.isOpen() : 
            self.serialPort.write(text.encode('utf-8')) 
            self.leSend.clear()

    # slot wysłania za pomocą enter na line edit
    def sendReturnPressed(self) :
        self.sendClicked()

    # slot obsługi DTR
    def DTRclicked(self) :
        if self.serialPort.isOpen() : 
            if self.pbDTR.isChecked() :
                self.serialPort.setDataTerminalReady(True)
            else :
                self.serialPort.setDataTerminalReady(False)

    # slot obsługi RTS
    def RTSclicked(self) :
        if self.serialPort.isOpen() : 
            if self.pbRTS.isChecked() :
                self.serialPort.setRequestToSend(True)
            else :
                self.serialPort.setRequestToSend(False)
    
    # slot uniwersalny do przesłania tekstu z przycisku makra na liSend i wysłania, zakończenie lini takie jak ustawine cbSendEol
    def macroClicked(self, text) :            
        self.leSend.setText(text)
        self.sendClicked()   

    # slot uniwersalny do zmiany makra, przez menu kontekstowe, edycja otwierana w osobnym oknie
    def macroCustomContextMenuRequested(self, pos, ptrButton) :
        def update(text) :
            ptrButton.setText(text)  
        def menuAction() : 
            macroWin = MacroWindow()
            macroWin.macroSubmitted.connect(update) 
            macroWin.exec()  
        contextMenu = QMenu(self) 
        action = contextMenu.addAction("Edit this macro.") 
        action.triggered.connect(menuAction) 
        contextMenu.exec(pos)

# panel read------------------------------------------------------------------------------------------------------
    def readData(self) : 
        '''odczyt danych'''

        # opcja odczytu HEX
        if self.cbHex.isChecked() :
            data = self.serialPort.readAll()
            data = (data.toHex(":").toStdString())
            cursor = self.pteReadSerial.textCursor() 
            cursor.insertText(data + "\n")
            if self.cbAutoScroll.isChecked() :
                self.pteReadSerial.setTextCursor(cursor)

        # opcja odczytu BIN
        elif self.cbBin.isChecked() :
            data = str(self.serialPort.readAll())
            data = ' : '.join(format(ord(char), '08b') for char in data)
            cursor = self.pteReadSerial.textCursor() 
            cursor.insertText(data + "\n")
            if self.cbAutoScroll.isChecked() :
                self.pteReadSerial.setTextCursor(cursor)

        # opcja odczytu tekstowego
        else :            
            data = self.serialPort.readAll().data().decode(self.myEncode, errors="ignore")
            # ignorowanie \r \n
            if self.cbIgnoreRN.isChecked() :
                data = data.replace("\r", "")
                data = data.replace("\n", "")
            
            cursor = self.pteReadSerial.textCursor() 
            # dodatnie daty i czasu na początki każdego wiersza
            if self.cbTime.isChecked() :
                currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                columnNumber = cursor.columnNumber() 
                if columnNumber == 0:    
                    data = currentTime + " -> " + data 
            
            cursor.insertText(data)

            # autoscroll
            if self.cbAutoScroll.isChecked() :
                self.pteReadSerial.setTextCursor(cursor)

    # slot podpięty do timer, do odczytu specjalnych sygnałó wejściowych
    def checkPinoutSerialInputSignals(self):
        if self.serialPort.isOpen() : 
            signals = self.serialPort.pinoutSignals()
            cts = signals & QSerialPort.PinoutSignal.ClearToSendSignal
            dsr = signals & QSerialPort.PinoutSignal.DataSetReadySignal
            dcd = signals & QSerialPort.PinoutSignal.DataCarrierDetectSignal
            ri = signals & QSerialPort.PinoutSignal.RingIndicatorSignal
            self.cbCTS.setChecked(bool(cts))
            self.cbDSR.setChecked(bool(dsr))
            self.cbCD.setChecked(bool(dcd))
            self.cbRI.setChecked(bool(ri))
    
    # czyszczenie okna odczytu
    def clearClicked(self) :
        self.pteReadSerial.clear()

    # zawijanie wierszy
    def warpCheckStateChanged(self, state) :
        if state == Qt.CheckState.Checked :
            self.pteReadSerial.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        elif state == Qt.CheckState.Unchecked: 
            self.pteReadSerial.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

    # dane z odczytu mieszczą się w jednym oknie
    def oneWindowCheckStateChanged(self, state) :
        if state == Qt.CheckState.Checked :
            fontMetrics = self.pteReadSerial.fontMetrics() 
            lineHeight = fontMetrics.lineSpacing() 
            viewportHeight = self.pteReadSerial.viewport().height() 
            visibleLines = viewportHeight // lineHeight
            self.pteReadSerial.setMaximumBlockCount(visibleLines - 1)
        elif state == Qt.CheckState.Unchecked : 
            self.pteReadSerial.setMaximumBlockCount(0)

    # zmiana kodowania danych tekstowych, zmienna jest używana w odczycie
    def textEncodeCurrentIndexChanged(self) :
        self.myEncode = self.cbTextEncode.currentText()

    # zapis danych z okna
    def saveWindowClicked(self) :
        options = QFileDialog.Options() 
        filePath, _ = QFileDialog.getSaveFileName(window, "Save file", "", "Text files (*.txt);;All files (*)", options=options) 
        if filePath : 
            with open(filePath, 'w') as file : 
                file.write(self.pteReadSerial.toPlainText())

    # start ze wskazaniem pliku do zapisu, stremingu zapisu
    def startStopLogClicked(self, state) :
        if state :
            options = QFileDialog.Options() 
            filePath, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt);;All files (*)", options=options) 
            if filePath : 
                self.file = QFile(filePath) 
                if not self.file.open(QIODevice.WriteOnly | QIODevice.Text) : 
                    return
            else:
                self.pbStartStopLog.setChecked(False)
        else:
            self.file.close()

    # zapis streamingu
    def streamWrite(self) : 
        if self.file and self.file.isOpen() : 
            self.file.resize(0) # Clear file before writing new content 
            text = self.pteReadSerial.toPlainText() 
            self.file.write(text.encode('utf-8'))

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
    # zdarzenie zamykania okna
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
