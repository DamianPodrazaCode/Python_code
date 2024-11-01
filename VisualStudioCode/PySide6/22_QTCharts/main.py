import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import QPointF

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ustawienia głównego okna
        self.setWindowTitle("Wykres Liniowy z QtCharts")
        self.setGeometry(100, 100, 800, 600)

        # Tworzymy wykres i widok wykresu
        chart = QChart()
        chart.setTitle("Przykładowy Wykres Liniowy")

        # Tworzymy serię danych dla wykresu liniowego
        series = QLineSeries()
        data = [QPointF(x, x * x) for x in range(-10, 11)]  # Przykładowa funkcja kwadratowa
        series.append(data)

        # Dodajemy serię do wykresu
        chart.addSeries(series)
        chart.createDefaultAxes()

        # Tworzymy widok wykresu
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Ustawiamy układ dla głównego widżetu
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)
        layout.addWidget(chart_view)
        
        pb_OK = QPushButton("OK")
        layout.addWidget(pb_OK)

        self.setCentralWidget(main_widget)
        # self.setLayout(layout)

# Uruchomienie aplikacji
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
