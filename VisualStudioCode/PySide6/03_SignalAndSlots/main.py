# >>> wersja nie checkable
# import sys
# from PySide6.QtWidgets import QApplication, QPushButton

# def button_clicked():
#     print('jest jest jest ....')

# app = QApplication(sys.argv)
# button = QPushButton('ok to print')
# button.clicked.connect(button_clicked)
# button.show()
# app.exec()        
# -------------------------------------------------------------------

# >>> wersja checkable
# import sys
# from PySide6.QtWidgets import QApplication, QPushButton

# def button_clicked(data):
#     print('clicked ', data)
# def button_pressed():
#     print('pressed ')
# def button_released():
#     print('released ')

# app = QApplication(sys.argv)
# button = QPushButton('ok to print')
# button.setCheckable(True)
# button.clicked.connect(button_clicked)
# button.pressed.connect(button_pressed)
# button.released.connect(button_released)

# button.show()
# app.exec()        

# -------------------------------------------------------------------
# >>> slider
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respound_to_slider(data):
    print('slider data', data)

app = QApplication(sys.argv)
slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(255)
slider.setValue(127)

slider.valueChanged.connect(respound_to_slider)
slider.show()
app.exec()   

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------