import sys
from PySide6.QtCore import QProcess, QSettings
from PySide6.QtWidgets import QWidget 
from ui_connectForm import Ui_ConnectForm

class connectPortWindow(QWidget, Ui_ConnectForm) :
    def __init__(self, comNr) :
        super().__init__()
        self.comNr = comNr
        self.setupUi(self)
        self.setWindowTitle(self.comNr)

        self.process = QProcess(self) 
        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.readSettings()
        self.pbCancel.clicked.connect(self.close)
        self.pbConnect.clicked.connect(self.serialConnect)

    def serialConnect(self) :
        python_path = sys.executable 
        script_path = "serialForm.py" 
        self.process.start(python_path, [script_path, 
                                    self.comNr, 
                                    self.leBautRate.text(), 
                                    self.cbDataBits.currentText(), 
                                    self.cbParity.currentText(), 
                                    self.cbStopBits.currentText(), 
                                    self.cbFlowControl.currentText()])
        self.writeSettings()
        self.close()

    def readSettings(self) :
        self.leBautRate.setText(self.settings.value("leBautRate"))
        self.cbDataBits.setCurrentIndex(self.settings.value("cbDataBits", 0, type=int))
        self.cbParity.setCurrentIndex(self.settings.value("cbParity", 0, type=int))
        self.cbStopBits.setCurrentIndex(self.settings.value("cbStopBits", 0, type=int))
        self.cbFlowControl.setCurrentIndex(self.settings.value("cbFlowControl", 0, type=int))

    def writeSettings(self) :
        self.settings.setValue("leBautRate", self.leBautRate.text())
        self.settings.setValue("cbDataBits", self.cbDataBits.currentIndex())
        self.settings.setValue("cbParity", self.cbParity.currentIndex())
        self.settings.setValue("cbStopBits", self.cbStopBits.currentIndex())
        self.settings.setValue("cbFlowControl", self.cbFlowControl.currentIndex())