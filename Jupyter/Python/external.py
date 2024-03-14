class Klasa:
    def __init__(self):  #konstruktor (tak jak by, ale ta funkcja tak naprawde uruchamia się po stworzeniu objektu)
        print('konstruktor')
    
    def metoda1(self):   # metoda
        print('metoda1')

    def __del__(self):  # destruktor
        print('destruktor')