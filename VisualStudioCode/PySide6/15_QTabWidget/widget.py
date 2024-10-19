from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QTabWidget, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QAbstractItemView # noqa: F401

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tab widget")
        # self.setMinimumSize(800, 800)
        
        # tab1 
        l_name = QLabel("Full name :")
        le_name = QLineEdit()
        h_layout = QHBoxLayout()
        h_layout.addWidget(l_name)
        h_layout.addWidget(le_name)
        widget_tab1 = QWidget()
        widget_tab1.setLayout(h_layout)

        #tab2
        pb_1 = QPushButton("One")
        pb_2 = QPushButton("Two")
        pb_3 = QPushButton("Three")
        pb_layout = QVBoxLayout()
        pb_layout.addWidget(pb_1)
        pb_layout.addWidget(pb_2)
        pb_layout.addWidget(pb_3)
        widget_tab2 = QWidget()
        widget_tab2.setLayout(pb_layout)

        #tab widget
        tab_widget = QTabWidget()
        tab_widget.addTab(widget_tab1, "Informations")
        tab_widget.addTab(widget_tab2, "Buttons")

        v_layout = QVBoxLayout()
        v_layout.addWidget(tab_widget)

        self.setLayout(v_layout)
        
        
        
        