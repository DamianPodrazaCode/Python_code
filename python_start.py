#zmienn bez definicji
x = 5 / 23
y = 'napis'
print(x,y)
y = 123.543
print(x,y)

#coment
"""
koment
komentKomet
"""

#bool
x = True
print(x)
print(x < 0)
print(f'x = {x}')
print('x =', x)
print(f'out = {x == 0}')
print(f'out = {x < 0}')
print(f'out = {x != 0}')
print(f'out = {x > 0}')

#numbers
#int
iVal = 234
print(iVal)
#float
iVal = 234.3425
print(iVal)
import sys # https://docs.python.org/3/library/sys.html#sys.float_info
print(sys.float_info)
#complex - liczby zespolone
iVal = 3 + 6j
jVal = 5 + 6j
#lub
aVal = complex(3,6)
bVal = complex(5,6)
#operacja na liczbach zespolonych
print(iVal + jVal)
print(iVal * jVal)
print(aVal + bVal)
print(aVal * bVal)
#pobieranie i wyświetlanie części liczb zespolonych
print(aVal.real, aVal.imag, iVal.real, iVal.imag)

#operacje + - * / 
# % - modulo
# ** pow 
# // floor div
x = 3 ** 2
print(x)
x = 3 / 2
print(x)
x = 3 // 2
print(x)
x = 3 % 2
print(x)

#strings
x = "ąćźćł"
z = 'ąćźćł'  # obojętnie czy " " , ' '
print(x)
print(f'sdfgsdf {x} {y} {aVal} {bVal}')  # print z formatowaniem

for y in 'asdfas' :  # ze stringa
    print(y, " " , ord(y)) # odr - numer utf8
for y in x : # ze stringa w zmiennej
    print(y, " " , ord(y)) # odr - numer utf8

# z numeru na znak
s1 = chr(104)
s2 = chr(68)
print(s1, s2)    # wyświetlanie jako znaków osobnych
print(s1 + s2)    # łączenie w stringa

# ze znaku na numer
z1 = ord("a")
z2 = ord("$")
z3 = ord("ę")
print(z1, z2, z3)    

# ESCAPE
print("1234\r\n5678")
print(f'1234\r\n5678')
print(f'2222{chr(13)+chr(10)}3333')
#tab
print("asd\tasd")
#formatowanie print
sVal = "asdfg"
iVal = 234
# print(sVal + "" + iVal) error połączenia int z str
print("napis", sVal, "int", iVal) 
print(f'napis {sVal} int {iVal}')
print("napis %s int %i" % (sVal, iVal))

str = "jakiś string - napis czy cos..."
print(len(str)) # długość
print(str * 3) # powielenie 
print(str.replace('.','!')) # zamiana
print(str.replace('string','str')) # zamiana
print(str.split('-')) # rozdzielenie d dwóch stringów
print(str.startswith('j')) # czy zaczyna się na
print(str.startswith('.')) # czy zaczyna się na 
print(str.endswith('.')) #czy kończy się na
print(str[2:10]) # wycinek od do
print(str[2:]) # wycinek od do końca
print(str[:10]) # wycinek od początku do 
print(str[-5:]) # wycinek ostatnich 5
print(str.find(' '))   # -1 jak nie znajdzie
print(str.find(' ', 6, 10)) # znajdź w wycinku, -1 jak nie znajdzie
# print(str.index('#'))  # jak nieznajdzie to error
# print(str.index(' ', 6, 10)) # znajdź w wycinku jak nieznajdzie to error

#Lists []
x = ['asdf',34,"asddf",654,45, 2.345, "ssdf", "3245234"]
print(x)
print(x.index(34)) # zwraca indeks wg wartości
print(x[0]) # wartość po indeksie
print(x[1])
print(x[2])
print(x[3])
print(len(x)) # ilość elementów
print(x[2:6]) # lista od elementu do elementu, taksamo ja w stringach

y = [] # pusta lista
y.append("asda") # dodanie do listy
y.append(99)
y.insert(1,"2222") # dodanie wg pozycji
print(y)

print(x)
x.remove(34) # usuwanie ale tylko po wartości nie po indexie
print(x)
x.pop(2) # usuwanie po indexie
print(x)
del x[3] # usuwa po indexie ale niezwraca stringa
print(x)

z = x + y #dodawanie list
print(z)
x.extend(y) # x rozszeżone o y
print(x)

#sortowanie
x = ['wer', 'gfd', 'vcx', 'hgy', 'jhgf', 'fddde']
print(x)
x.sort() # posortowanie, można sortować listy albo tylko stringi alb tylko liczby
print(x)
x.reverse() # odwrucenie listy
print(x)

x = [5,23,0.7,3,56,34,7,4,2,7,9,34,23.45,675.2,1.3435,67,23,12,6,78]
print(x)
x.sort() # posortowanie, można sortować listy albo tylko stringi alb tylko liczby
print(x)
x.reverse() # odwrucenie listy
print(x)

# kasowanie 
del z # kasuje całą liste z pamięci i niemożna się do niej odwołać bo error
# print(z) error

print(y)
y.clear() # czyści listę, ale lista pusta jest dostępna do zapełnienia
print(y)

#listy list
lista = [[1,2,3], ["asd", 34.32, 'qwe'], [43.76, 123.32, 65.23, 1, 2]]
print(lista) # wszystkie listy
print(lista[0]) # poszczególna lista
print(lista[1])
print(lista[2])
print(lista[0][1]) # element w liście z listy

#zmiana w liście
lista = [1,2,3,4,5,6,71]
print(lista)
lista[2] = "sdfsd"
print(lista)

#sets {} , tablica z szybkim dostępem, samoukładająca, redukująca, do operacji na zbiorach danych, porównywanie, AND OR XOR
s = {1,2,3,4,56,67,3,3}
print(s)
l = ['asd', 'wer', 23, 34, 564]
s = set(l) # przepisanie do seta
print(s)
s.add(5634) # doddanie do seta
s.add('sdaf')
s.update(l) # dodanie całej listy
s.update(['dsfs',345,65.34,'dfsdf']) # dodanie kilku elementów w postaci listy
print(s)
s.discard(345) # usunięcie po wartości
print(s)
#s.remove(1) # po indeksie jak nie ma to error
s.remove('wer') # po wartości jak nie ma to error
print(s)
# nie ma możliwości zmiany wartości

#tuple () -> szybla lista const
