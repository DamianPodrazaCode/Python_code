class Klasa1:
    zm1 = ''
    zm2 = ''

    def __init__(self, zm1='zm1', zm2='zm2'):  #konstruktor, dobrze jest zainicjalizować tutaj zmienne w szczegulniości do pobierania adresu, self jest wymagane
        self.zm1 = zm1
        self.zm2 = zm2
        print(f'konstruktor {self.zm1}  {self.zm2}')

    def showAll(self): #metoda, self jest wymagane ale z zewnątrz nie urzywane
        print(f'showAll {self.zm1}  {self.zm2}')
    

class Klasa2(Klasa1):  #dziedzieczenie Klasa2 dziedziczy po Klasa1
    zm3 = ''
    am4 = ''

    def __init__(self, zm1='zm1', zm2='zm2', zm3='zm3', zm4='zm4'):
        # super().__init__(zm1, zm2)
        self.zm1 = zm1
        self.zm2 = zm2
        self.zm3 = zm3
        self.zm4 = zm4
        print(f'konstruktor {self.zm1}  {self.zm2} {self.zm3}  {self.zm4}')

    def showAll(self): #metoda, self jest wymagane ale z zewnątrz nie urzywane
        print(f'showAll {self.zm1} {self.zm2} {self.zm3} {self.zm4}')
