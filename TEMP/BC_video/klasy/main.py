# import klasy as code
from klasy import Klasa1 
from klasy import Klasa2
from klasy import Klasa3

def test():
    print('-----------------------')
    obj1 = Klasa1('kl1', 100)
    # print(obj1) # adress objektu
    obj1.showAll()
    obj1.metodaKl1()

    print('-----------------------')
    obj2 = Klasa2('kl2', 12, 34, 56)
    # print(obj2) # adress objektu
    obj2.showAll()
    obj2.metodaKl1()
    obj2.metodaKl2()

    # print('-----------------------')
    # obj3 = Klasa3('kl3', 2, 3, 6)
    # # print(obj3) # adress objektu
    # obj3.showAll()
    # obj3.metodaKl1()
    # obj3.metodaKl2()

if __name__ == "__main__":
    test()
    

