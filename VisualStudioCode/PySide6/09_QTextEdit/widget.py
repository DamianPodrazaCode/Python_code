from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("text edit")
        self.setMinimumSize(800, 100)

        btn_currentText = QPushButton("Current Text")
        btn_copy = QPushButton("Copy")
        btn_cut = QPushButton("Cut")
        btn_paste = QPushButton("Paste")
        btn_undo = QPushButton("Undo")
        btn_redo = QPushButton("Redo")
        btn_setPlainText = QPushButton("Set Plain Text")
        btn_setHTML = QPushButton("Set HTML")
        btn_clear = QPushButton("Clear")

        layout_button = QHBoxLayout()
        layout_button.addWidget(btn_currentText)
        layout_button.addWidget(btn_copy)
        layout_button.addWidget(btn_cut)
        layout_button.addWidget(btn_paste)
        layout_button.addWidget(btn_undo)
        layout_button.addWidget(btn_redo)
        layout_button.addWidget(btn_setPlainText)
        layout_button.addWidget(btn_setHTML)
        layout_button.addWidget(btn_clear)

        self.pte_text = QTextEdit()

        layout_all = QVBoxLayout()
        layout_all.addLayout(layout_button)
        layout_all.addWidget(self.pte_text)

        self.setLayout(layout_all)

        btn_currentText.clicked.connect(self.btn_currentText_clicked)
        # btn_copy.clicked.connect(self.btn_copy_clicked)
        btn_copy.clicked.connect(self.pte_text.copy) # bezpośrednie wywołanie copy, a wyżej podłączenie do slotu własnego
        btn_cut.clicked.connect(self.btn_cut_clicked)
        btn_paste.clicked.connect(self.btn_paste_clicked)
        btn_undo.clicked.connect(self.btn_undo_clicked)
        btn_redo.clicked.connect(self.btn_redo_clicked)
        btn_setPlainText.clicked.connect(self.btn_setPlainText_clicked)
        btn_setHTML.clicked.connect(self.btn_setHTML_clicked)
        btn_clear.clicked.connect(self.btn_clear_clicked)

    def btn_currentText_clicked(self) :
        print(self.pte_text.toPlainText())
    # def btn_copy_clicked(self) :
    #     self.pte_text.copy()        
    def btn_cut_clicked(self) :
        self.pte_text.cut()
    def btn_paste_clicked(self) :
        self.pte_text.paste()
    def btn_undo_clicked(self) :
        self.pte_text.undo()
    def btn_redo_clicked(self) :
        self.pte_text.redo()
    def btn_setPlainText_clicked(self) :
        self.pte_text.setPlainText("Jakiś tekst")
    def btn_setHTML_clicked(self) :
        self.pte_text.setHtml("<h1>aaa</h1>")
    def btn_clear_clicked(self) :
        self.pte_text.clear()
        
        