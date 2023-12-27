import klasy as code
from klasy import Klasa1 
from klasy import Klasa2

def test():
    b = Klasa1('kl1', 100)
    b.showAll()
    c = Klasa2('kl2', 12, 34, 56)
    c.showAll()

if __name__ == "__main__":
    print(Klasa1('test'))  #adres objektu
    print(Klasa2('test'))  #adres objektu
    test()
    

