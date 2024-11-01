import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drugie Okno")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Jestem w drugim oknie!"))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Główne Okno")
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Otwórz Drugie Okno")
        button.clicked.connect(self.open_second_window)

        layout = QVBoxLayout()
        layout.addWidget(button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.windows = []

    def open_second_window(self):
        second_window = SecondWindow()
        second_window.show()
        self.windows.append(second_window)  # Przechowywanie odniesienia do okna

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
