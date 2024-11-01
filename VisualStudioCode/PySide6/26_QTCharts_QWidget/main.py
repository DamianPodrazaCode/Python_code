import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtGui import QPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wykres QtCharts w Oddzielnym QWidget")
        self.setFixedSize(600, 600)

        # Tworzenie QWidget
        chart_widget = QWidget()
        layout = QVBoxLayout(chart_widget)

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
        chart.setTitle("Liniowy Wykres QtCharts")
        chart.createDefaultAxes()

        # Tworzenie widoku wykresu
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Dodanie widoku wykresu do layoutu
        layout.addWidget(chart_view)

        # Ustawienie QWidget jako centralny widget
        self.setCentralWidget(chart_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
