from PySide6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QPushButton # noqa: F401

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("combo box")
        self.setMinimumSize(400, 100)
        
        self.combo = QComboBox()
        self.combo.addItem("One")
        self.combo.addItems(["111", "222", "333", "444", "555"])

        pb_value = QPushButton("current value")
        pb_value.clicked.connect(self.current_value)
        pb_set = QPushButton("set value")
        pb_set.clicked.connect(self.set_value)
        pb_get = QPushButton("get value")
        pb_get.clicked.connect(self.get_value)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo)
        v_layout.addWidget(pb_value)
        v_layout.addWidget(pb_set)
        v_layout.addWidget(pb_get)
        
        self.setLayout(v_layout)

    def current_value(self) :
        print(self.combo.currentIndex(), self.combo.currentText())

    def get_value(self) :
        for i  in range(self.combo.count()) :
            print(self.combo.itemText(i))

    def set_value(self) :
        self.combo.setCurrentIndex(2)
        
    
        
        
        