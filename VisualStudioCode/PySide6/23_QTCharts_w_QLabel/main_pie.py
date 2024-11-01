from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wykres Kołowy w QLabel")

        # Tworzenie serii wykresu kołowego
        series = QPieSeries()
        series.append("Jabłka", 40)
        series.append("Banany", 30)
        series.append("Wiśnie", 20)
        series.append("Datyle", 10)

        # Tworzenie wykresu
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Wykres Kołowy")

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
