import klasy as code
from klasy import Klasa1 
from klasy import Klasa2

def test():
    obj1 = Klasa1('kl1', 100)
    print(obj1) # adress objektu
    obj1.showAll()
    
    obj2 = Klasa2('kl2', 12, 34, 56)
    print(obj2) # adress objektu
    obj2.showAll()

if __name__ == "__main__":
    test()
    

