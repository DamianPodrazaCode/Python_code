print('---------------------------------------------Funkcje wbudowane')
print(max('asdfgh')) # największa wartość w liście
print(min('asdfgh')) # najmniejsza wartość w liście
print(len('asdfgh')) # długość
# mogą być stosowane również przy innych listach tabelach i kontenerach
zm1 = 1.23
#zm1 = 'text' # to wywali błąd bo niemożna konwertować z str na typ liczbowy, można to sprawdzać przy pomocy 'try' (02_)
zm2 = int(zm1) # casting typu na int
print(zm1, zm2)
zm2 = float(12)
zm2 = str(2345.231)
zm2 = complex(15)

print('---------------------------------------------Funkcje matematyczne')
import math
# w prosty sposób można uzyskać coś na jego temat
print(math) # prawy przycisk na math->'Go to definition' 

print('---------------------------------------------Liczby losowe')
import random
zm1 = random.random() # losowa między 0.0 - 1.0 float
print(zm1)
zm1 = random.randint(5,20) # losowa int między 5 - 20
print(zm1)
zm1 = random.randbytes(20) # generule określoną liczbę bitów
print(zm1)

lista = [32,523,12,654,23,1,567,2,3,24] # sekwencja wyboru
zm1 = random.choice(lista) # wybierze liczbe losowo z powyższej listy
print(zm1)

print('---------------------------------------------Funkcje')
# nowa funkcja
def fun() :
    print('fun')

def fun2(x, y) :
    return x * y

fun() # funkcja pusta, bo niezwraca żadnej wartości
print(fun2(2, 3)) # funkcja owocna

