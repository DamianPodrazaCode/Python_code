from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QCandlestickSeries, QCandlestickSet
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QPainter
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wykres Świecowy w QLabel")

        # Tworzenie serii wykresu świecowego
        series = QCandlestickSeries()
        series.setName("Wykres Świecowy")
        series.append(QCandlestickSet(1, 5, 3, 4, QDateTime.currentDateTime().toMSecsSinceEpoch()))
        series.append(QCandlestickSet(2, 6, 4, 5, QDateTime.currentDateTime().addDays(1).toMSecsSinceEpoch()))
        series.append(QCandlestickSet(3, 7, 5, 6, QDateTime.currentDateTime().addDays(2).toMSecsSinceEpoch()))
        series.append(QCandlestickSet(4, 8, 6, 7, QDateTime.currentDateTime().addDays(3).toMSecsSinceEpoch()))
        series.append(QCandlestickSet(5, 9, 7, 8, QDateTime.currentDateTime().addDays(4).toMSecsSinceEpoch()))

        # Tworzenie wykresu
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Wykres Świecowy")
        chart.createDefaultAxes()

        # Tworzenie widoku wykresu
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Tworzenie QLabel i ustawienie widoku wykresu jako jego zawartość
        label = QLabel()
        label.setFixedSize(800, 600)
        label.setAlignment(Qt.AlignCenter)
        label.setLayout(QVBoxLayout())
        label.layout().addWidget(chart_view)

        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
