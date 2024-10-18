from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("okno z menu, tulbar, statusbar")
        self.setFixedSize(600,600)        
        
        # ---->>> menu bar
        # główne menu        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        edit_menu = menu_bar.addMenu("&Edit")
        settings_menu = menu_bar.addMenu("&Settings")
        help_menu = menu_bar.addMenu("&Help")

        # pod menu
        file_menu.addAction("New")
        file_menu.addAction("Open")
        hExit = file_menu.addAction("Exit") # stworzenie zmiennej uchwytu 
        hExit.triggered.connect(self.mExit) # dołączenie uchwytu do metody

        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        
        settings_menu.addAction("Settings")
        settings_menu.addAction("save Settings")

        help_menu.addAction("Help")
        help_menu.addAction("Info")

        # ---->>> tool bar
        tool_bar = QToolBar("toolbar")
        tool_bar.setIconSize(QSize(32,32))

        self.addToolBar(tool_bar)
        
        # wykozystanie z menubar
        tool_bar.addAction(hExit)  # wykorzystany ten sam connect co wyżej

        # stworzenie i dodanie do toolbar
        newAction = QAction("newAction", self)
        newAction.setStatusTip("status tip")
        newAction.triggered.connect(self.newAction_click)
        tool_bar.addAction(newAction)
        
        newActionIcon = QAction(QIcon("icon.ico"), "newAction", self)
        newActionIcon.setStatusTip("status tip")
        newActionIcon.triggered.connect(self.newAction_click)
        tool_bar.addAction(newActionIcon)        

        # dodanie przycisku do menubar
        tool_bar.addSeparator()
        tool_bar.addWidget(QPushButton("ok ok ok"))

        # ---->>> status bar
        self.setStatusBar(QStatusBar(self))

    def mExit(self): 
        self.app.quit()

    def newAction_click(self):
        # self.statusBar().showMessage("okokokokokok !!!!")
        self.statusBar().showMessage("okokokokokok !!!!", 2000) # wyświetlanie z opóźninym wygaśnięciem w [ms]
