import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap, QImage
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tworzymy kontrolkę QLabel
        self.label = QLabel(self)
        self.setCentralWidget(self.label)

        # Generujemy wykres
        self.create_plot()

    def create_plot(self):
        # Tworzymy figurę matplotlib
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Przykładowy wykres
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)

        # Renderowanie wykresu na buforze
        canvas.draw()

        # Konwersja na obraz QImage
        width, height = fig.get_size_inches() * fig.get_dpi()
        image = QImage(canvas.buffer_rgba(), int(width), int(height), QImage.Format_RGBA8888)

        # Wyświetlenie obrazu na QLabel
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

# Uruchomienie aplikacji
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
