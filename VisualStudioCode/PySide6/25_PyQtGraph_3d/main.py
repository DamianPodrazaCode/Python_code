import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wykres 3D w PySide6")
        self.setFixedSize(1000,1000)

        # Tworzenie widoku GLViewWidget
        widget = gl.GLViewWidget()
        widget.opts['distance'] = 40

        # Tworzenie danych
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)
        z = np.sin(np.sqrt(x**2 + y**2))

        # Konwersja danych do odpowiedniego formatu
        x = x.flatten()
        y = y.flatten()
        z = z.flatten()

        # Tworzenie kolorów w zależności od wartości z
        colors = np.zeros((x.size, 4), dtype=np.float32)
        colors[:, 0] = np.linspace(0, 1, x.size)  # Kolor czerwony
        colors[:, 1] = np.linspace(1, 0, y.size)  # Kolor zielony
        colors[:, 2] = (z - z.min()) / (z.max() - z.min())  # Kolor niebieski w zależności od wartości z
        colors[:, 3] = 1.0  # Ustawienie pełnej przezroczystości

        # Tworzenie siatki 3D z kolorami
        points = gl.GLScatterPlotItem(pos=np.c_[x, y, z], color=colors, size=5)
        widget.addItem(points)

        # Ustawienie layoutu
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(widget)
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
