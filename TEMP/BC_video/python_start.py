


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