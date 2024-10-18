from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("message box-y")
        self.setMinimumWidth(400)

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_hard_clicked)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_critical_clicked)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_question_clicked)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_information_clicked)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_warning_clicked)

        button_abaut = QPushButton("Abaut")
        button_abaut.clicked.connect(self.button_abaut_clicked)
        
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_abaut)
        self.setLayout(layout)
        
    def button_hard_clicked(self):
        messageOut = QMessageBox()
        messageOut.setWindowTitle("Tytuł")
        messageOut.setText("tekst olidjfvpsdjfp[vosjdvpo opdjpojspojposd /n oiasdhfoaisfoasi /n seaddfohfaso /n asdfiasdfi]")
        messageOut.setInformativeText("info tekst")
        messageOut.setIcon(QMessageBox.Information) # o ikony zależą dźwięki
        messageOut.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messageOut.setDefaultButton(QMessageBox.Ok)
        ret = QMessageBox.exec(messageOut)
        if ret == QMessageBox.Ok :
            print("ok")
        else :
            print("cancel")            

    def button_critical_clicked(self):
        ret = QMessageBox.critical(self, "tytuł", "tekst", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("ok")
        else :
            print("cancel")            

    def button_question_clicked(self):
        ret = QMessageBox.question(self, "tytuł", "tekst", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("ok")
        else :
            print("cancel")            

    def button_information_clicked(self):
        ret = QMessageBox.information(self, "tytuł", "tekst", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("ok")
        else :
            print("cancel")            

    def button_warning_clicked(self):
        ret = QMessageBox.warning(self, "tytuł", "tekst", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("ok")
        else :
            print("cancel")            

    def button_abaut_clicked(self):
        ret = QMessageBox.about(self, "tytuł", "tekst")
        if ret == QMessageBox.Ok :
            print("ok")
        else :
            print("cancel")            



