from PySide6.QtWidgets import QWidget, QCheckBox, QRadioButton, QGroupBox, QButtonGroup, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy # noqa: F401

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("chek box and radio btton")
        # self.setMinimumSize(800, 800)

        # ------------------------------------------------------
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_toggled)
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_toggled)
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)

        os = QGroupBox("Wybierz OS")
        os.setLayout(os_layout)

        # ------------------------------------------------------
        beer = QCheckBox("Beer")
        beer.setChecked(True)
        juice = QCheckBox("Juice")
        coffe = QCheckBox("Coffe")

        # exclusive button group
        ebg_drink = QButtonGroup(self)
        ebg_drink.addButton(beer)
        ebg_drink.addButton(juice)
        ebg_drink.addButton(coffe)
        ebg_drink.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffe)

        drink = QGroupBox("Wybierz drina")
        drink.setLayout(drink_layout)

        # ------------------------------------------------------
        answer_a = QRadioButton("A")
        answer_a.setChecked(True)
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")

        answer_layout = QVBoxLayout()
        answer_layout.addWidget(answer_a)
        answer_layout.addWidget(answer_b)
        answer_layout.addWidget(answer_c)

        answer = QGroupBox("Wybierz odpowiedź")
        answer.setLayout(answer_layout)

        # ------------------------------------------------------
        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drink)
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answer)

        self.setLayout(v_layout)

    # ------------------------------------------------------
    def windows_toggled(self, check):
        print("windows_toggled", check)
    def linux_toggled(self, check):
        print("linux_toggled", check)
    def mac_toggled(self, check):
        print("mac_toggled", check)
        