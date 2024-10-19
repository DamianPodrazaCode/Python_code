from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QAbstractItemView # noqa: F401

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("list widget")
        # self.setMinimumSize(800, 800)

        self.lista = QListWidget()
        self.lista.setSelectionMode(QAbstractItemView.MultiSelection)
        self.lista.addItem("One")
        self.lista.addItems(["Two", "Three"])
        self.lista.currentItemChanged.connect(self.item_changed)
        self.lista.currentTextChanged.connect(self.text_changed)

        pb_add = QPushButton("Add Item")
        pb_add.clicked.connect(self.add_item)
        pb_delete = QPushButton("Delete Item")
        pb_delete.clicked.connect(self.delete_item)
        pb_count = QPushButton("Item Count")
        pb_count.clicked.connect(self.count_item)
        pb_selected = QPushButton("Selected Items")
        pb_selected.clicked.connect(self.selected_item)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.lista)
        v_layout.addWidget(pb_add)
        v_layout.addWidget(pb_delete)
        v_layout.addWidget(pb_count)
        v_layout.addWidget(pb_selected)
        self.setLayout(v_layout)


    def item_changed(self, item) :
        print("item changet ", item.text())  

    def text_changed(self, text) :
        print("change text ", text)

    def add_item(self) :
        self.lista.addItem("nowy !!")

    def delete_item(self) :
        self.lista.takeItem(self.lista.currentRow())

    def count_item(self) :
        print("item count", self.lista.count())

    def selected_item(self) :
        lists = self.lista.selectedItems()
        for i in lists :
            print(i.text()) 
    