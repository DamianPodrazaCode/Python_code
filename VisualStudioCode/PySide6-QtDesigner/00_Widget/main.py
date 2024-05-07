# pliki generowane z QtDesigner wskazane jest żeby miały przedrostek 'ui_':
# ui_Dialog.ui -> zapisany projekt z QtDesigner, w projekcie nie używany 
# ui_Dialog.py -> wygenerowany plik z QtDesigner lub poleceniem 'pyside6-uic ui_Dialog.ui > ui_Dialog.py'
# main.py -> główny plik uruchomieniowy
# dialog.py -> główna klasa wyświetlanego okna 

import sys
from PySide6 import QtWidgets
from widget import Okno # import głównej klasy onka

app = QtWidgets.QApplication(sys.argv) # uruchomienie qt

window = Okno() # instancja głównego okna
window.show() # wyświetlenie okna

app.exec() # uruchomienie aplikacji i pętli komunikatów