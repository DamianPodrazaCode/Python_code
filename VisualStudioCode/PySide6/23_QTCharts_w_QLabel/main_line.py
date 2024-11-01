from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wykres Liniowy w QLabel")

        # Tworzenie serii wykresu liniowego
        series = QLineSeries()
        series.append(0, 6)
        series.append(2, 4)
        series.append(3, 8)
        series.append(7, 4)
        series.append(10, 5)

        # Tworzenie wykresu
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Wykres Liniowy")
        chart.createDefaultAxes()

        # Tworzenie widoku wykresu
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Tworzenie QLabel i ustawienie widoku wykresu jako jego zawartość
        label = QLabel()
        label.setFixedSize(400, 300)
        label.setAlignment(Qt.AlignCenter)
        label.setLayout(QVBoxLayout())
        label.layout().addWidget(chart_view)

        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
