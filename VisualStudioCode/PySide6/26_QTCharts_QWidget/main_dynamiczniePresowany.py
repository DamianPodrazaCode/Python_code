import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import QTimer, QPointF
from PySide6.QtGui import QPainter

class RealTimeLineChart(QWidget):
    def __init__(self):
        super().__init__()

        self.series = QLineSeries()

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Dynamiczny wykres liniowy w czasie rzeczywistym")

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        self.setLayout(layout)

        self.x = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(100)

        self.axisX = QValueAxis()
        self.axisY = QValueAxis()
        self.chart.setAxisX(self.axisX, self.series)
        self.chart.setAxisY(self.axisY, self.series)
        self.axisX.setRange(0, 10)
        self.axisY.setRange(0, 10)

    def update_chart(self):
        self.x += 1
        y = random.randint(0, 10)
        self.series.append(QPointF(self.x, y))
        print(f"Added point: ({self.x}, {y})")

        if self.x > 10:
            self.axisX.setRange(self.x - 10, self.x)

        self.chart_view.repaint()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time Line Chart with QtCharts")

        chart_widget = RealTimeLineChart()
        self.setCentralWidget(chart_widget)
        self.resize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
