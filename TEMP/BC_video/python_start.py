# sortowanie
x = ['wer', 'gfd', 'vcx', 'hgy', 'jhgf', 'fddde']
print(x)
x.sort()  # posortowanie, można sortować listy jednego typu wartości albo tylko stringi alb tylko liczby
print(x)
x.reverse()  # odwrócenie listy
print(x)
x = [5, 23, 0.7, 3, 56, 34, 7, 4, 2, 7, 9, 34,
     23.45, 675.2, 1.3435, 67, 23, 12, 6, 78]
print(x)
x.sort()  # posortowanie, można sortować listy albo tylko stringi alb tylko liczby
print(x)
x.reverse()  # odwrucenie listy
print(x)

# listy list
lista = [[1, 2, 3], ["asd", 34.32, 'qwe'], [43.76, 123.32, 65.23, 1, 2]]
print(lista)  # wszystkie listy
print(lista[0])  # poszczególna lista
print(lista[1])
print(lista[2])
print(lista[0][1])  # element w liście z listy


# -------------------------------------------------------------------------------------------------------------------------------------------

# sets {} , tablica z szybkim dostępem, samoukładająca, redukująca, do operacji na zbiorach danych, porównywanie zbiorów, AND OR XOR
s = {1, 2, 3, 4, 56, 67, 3, 3}
print(s)
l = ['asd', 'wer', 23, 34, 564]
s = set(l)  # przepisanie listy do seta
print(s)
s.add(5634)  # doddanie do seta, nie ma gwarancji na której pozyvji wyląduje
s.add('sdaf')
s.update(l)  # dodanie całej listy
# dodanie kilku elementów w postaci listy
s.update(['dsfs', 345, 65.34, 'dfsdf'])
print(s)
s.discard(345)  # usunięcie po wartości
print(s)
# s.remove(1) # po indeksie jak nie ma to error
s.remove('wer')  # po wartości jak nie ma to error
print(s)
# nie ma możliwości zmiany wartości

# tuple () -> szybla lista const
t = (1, 2, 3, 4, 5, 6, 7, 8)  # definicja
print(t)
print(t[0])  # dostęp do elementu
print(t[3:])
print(t[:6])
print({3 in t})  # czy 3 jest w tuple t
tt = ('sss', 3.45, "asdf", 123)
print(tt)
print({"asdf" in tt})  # czy "asdf" jest w tuple tt
# przypisanie do zmiennych
(x, y, z) = (1, 2, 3)
print(x)
print(y)
print(z)
x = 10
print(x)

# -------------------------------------------------------------------------------------------------------------------------------------------

# dictionary {k:v, k:v} -> para: key - value
# tworzenie 1
d = {'asd': 'dsa', 'qwe': 'ewq', 1: 'jeden', 2: 'dwa', 'trzy': 3, "cztery": 4}
print(d)
print(d.items())
# tworzenie 2
d = dict(asd='dsa', qwe='ewq', jeden=1, dwa=2, trzy=3, cztery=4)
print(d)

print(d.items())  # wyświetlenie w formacie par
print(d.keys())  # same klucze
print(d.values())  # same wartości

print(d['jeden'])  # odczyt po kluczu
print(f'value {d["dwa"]}')  # to co wyżej tylko w sformatowanym stringu

d['add'] = 'cvb'  # dodanie do map
print(d.items())
d['add'] = 'fgdsfgdfg'  # zmiana wartości
print(d.items())
del d['add']  # usuwanie pozycji
print(d.items())


# -------------------------------------------------------------------------------------------------------------------------------------------

# flow control

# przy if zamiast nawiasów{} są odsunięcia tabem
x = True  # lub 1
if x:  # lub x==True:
    print('true')
    print(x)
else:
    print('false')

x = 100
y = 25
if x == y:
    print('równe')
if x != y:
    print('nierówne')
if x < y:
    print('mniejsze')
if x > y:
    print('większe')

x = 100
if x == 10:
    print(x)
elif x == 20:
    print(x)
elif x == 30:
    print(x)
else:
    print("reszta", x)

x = 0
while x < 10:
    x += 1
    print(x)

# x = 0
# while x < 10:
#     pass #taki nop, ale wtym przypadku zrobi się pętla nieskończona
# są jeszcze continue i break standard jak w C

x = [1, '123', 3, 4, 'abc', 6, 7]  # to samo dla Tuple, i Set
for i in x:  # i bedzie przyjmowała kolejne wartości listy
    print(i)

d = dict(asd='dsa', qwe='ewq', jeden=1, dwa=2, trzy=3, cztery=4)
print(d)
for k in d.keys():     # wylistowanie kluczy
    print(k)
for k in d.values():    # wylistowanie wartości
    print(k)
for k in d.items():    # wylistowanie par
    print(k)
for k in d.keys():  # wylistowanie wartości po kluczu
    print(k, d[k])
for k, v in d.items():  # wylistowanie wartości i klucza
    print(k, v)

# range() -> automat do tworzenia iteratora
x = range(10)  # iterator od <0 - 10)
print(x)
for i in x:
    print(i)

x = range(2, 10)  # iterator od <2 - 10) (start, stop)
print(x)
for i in x:
    print(i)

x = range(2, 10, 2)  # iterator od <2 - 10) z krokiem co 2 (start,stop,step)
print(x)
for i in x:
    print(i)

for i in range(10): # bezpośrednio w for
    print(i)    

s = input("wpisz coś :")  # pobieranie z terminala
print(s)
strToList = s.split(',')  # podzielenie w miejscach ',', stworzenie listy
print(strToList)


lista = [] #pusta lista, jeszcze nie określona
item1 = [x,y] #stworzenie elementu listy który jest listą
item2 = [z,v]
lista.append(item1) #dodanie do listy elementu który jest listą
lista.append(item2)
print(lista)

# Zasięg zmiennej.
x = 'zmienna globalna'

def myFunc():
    x = 'zmienna lokalna'
    print(x)

myFunc()
print(x)