import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeWidget z Rozwijanymi Komórkami")

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderHidden(True)

        # Dodawanie głównych elementów
        item1 = QTreeWidgetItem(["Element 1"])
        item2 = QTreeWidgetItem(["Element 2"])
        item3 = QTreeWidgetItem(["Element 3"])

        self.tree_widget.addTopLevelItem(item1)
        self.tree_widget.addTopLevelItem(item2)
        self.tree_widget.addTopLevelItem(item3)

        # Dodawanie podpozycji
        child1 = QTreeWidgetItem(["Podpozycja 1-1"])
        child2 = QTreeWidgetItem(["Podpozycja 1-2"])
        item1.addChild(child1)
        item1.addChild(child2)

        child3 = QTreeWidgetItem(["Podpozycja 2-1"])
        item2.addChild(child3)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Połącz sygnał kliknięcia elementu z metodą wyświetlającą message box
        self.tree_widget.itemClicked.connect(self.show_message_box)

    def show_message_box(self, item):
        message = f"Kliknąłeś na: {item.text(0)}"
        QMessageBox.information(self, "Informacja", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
