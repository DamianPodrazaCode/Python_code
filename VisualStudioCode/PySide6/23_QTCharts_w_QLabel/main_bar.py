from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QtCharts w QLabel")

        # Tworzenie zestawu danych
        bar_set = QBarSet("Data")
        bar_set.append(1)
        bar_set.append(2)
        bar_set.append(3)
        bar_set.append(4)
        bar_set.append(5)

        # Tworzenie serii wykresu
        bar_series = QBarSeries()
        bar_series.append(bar_set)

        # Tworzenie wykresu
        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Wykres QtCharts")
        chart.setAnimationOptions(QChart.SeriesAnimations)

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
