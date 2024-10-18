from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("label and line edit")
        self.setMinimumSize(500, 100)

        l_name = QLabel("Full name:")
        self.le_name = QLineEdit()
        self.le_name.setMinimumWidth(400)

        layout_name = QHBoxLayout()
        layout_name.addWidget(l_name)
        layout_name.addWidget(self.le_name)

        button = QPushButton("click")
        self.l_out = QLabel("OUT")

        layout_all = QVBoxLayout()
        layout_all.addLayout(layout_name)
        layout_all.addWidget(button)
        layout_all.addWidget(self.l_out)

        self.setLayout(layout_all)

        self.le_name.editingFinished.connect(self.le_name_editingFinished)
        button.clicked.connect(self.btn_clicked)

    def le_name_editingFinished(self) :
        print("le_name_editingFinished")
        self.l_out.setText(self.le_name.text())
        self.le_name.setText("")
        
    def btn_clicked(self) :        
        print("btn_clicked")
