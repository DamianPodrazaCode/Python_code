# sprawdzanie po wartości
print('text' in lista) # True, jeżeli 'text' jest w lista

for inLista in lista : # odczyt przez wartości 
    print(inLista)

for index in range(len(lista)) : # dostęp przez indexy
    print(index, lista[index])

# dodawanie list konkatenacja (sklejanie)
l1 = ['aa', 'bb', 'cc']
l2 = [1, 2, 3]
print(l1, '+', l2, '=', l1 + l2) 

# powielanie list
print(l1 * 4)

# wycinanie indeksem
lista = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
print(lista)
print(lista[:3]) # od początku do elementu 3, czyli index 0,1,2
print(lista[2:]) # od elementu 2 do końca
print(lista[2:4]) # od elementu do elementu
print(lista[1:-1]) # od elementu drugiego do elementu przedostatniego
lista.append('a1') # dodaje jeden element
lista.extend(l1) # rozszerza o liste lub wiele elementów
print(lista)
lista.sort() 
print(lista)
out = lista.pop(1) # usuwanie po indeksie, metoda zwrtaca wartość usuwaną
del lista[1] # usuwanie po indeksie bez zwrotu (pewnie szybsze)
print(lista)
lista.remove('dd') # usuwanie po wartości
print(lista)
del lista[1:3] # zwracanie wielu po indeksie
print(lista)

print('---------------------------------------------funkcje wbudowane')
lista = [12, 54, 34, 76, 2.34, 6.43, 10.1112233, 23, 654]
print(len(lista)) # długość
# funcje agregujące min, max, sum
print(max(lista)) # maksymalna wartość
print(min(lista)) # minimalna wartość
print(sum(lista)) # suma wartości, muszą być liczby
print(sum(lista) / len(lista)) # średnia arytmetyczna, muszą być same liczby

# konwersja napisu na listę
napis = 'asdfghjkl'
lista = list(napis)
print(napis)
print(lista)

# rozdzielenie napisu specjalnym znakiem
napis = 'asd fgh 123 543'
lista = napis.split(' ')
print(napis)
print(lista)

# złączenie w napis
napis = ''
singn = ':' # separator
napis = singn.join(lista)
print(napis)


lista = napis.split(':')
print(lista)
lista.sort() # tylko lista z niepomieszanymi typami
print(lista)
lista.reverse() # odwrotność listy
print(lista)
# można to zrobić za jednym zamachem
lista.sort(reverse=True);

print(len(lista)) # ilość elementów w liście
print(lista.count('asd')) # ilość wystąpieńdanego elementu
cLista = lista.copy() # kopia listy
print(cLista)
cLista = lista[1:4] # kopia części listy
print(cLista)

print(lista.index('asd')) # pobranie indexu elementu, jeżeli go nie ma to wywali błąd

#Listy składane

liczby = []
for x in range(1, 21) : 
    liczby.append(x)
print(liczby)

parzyste = []
for i in liczby:
    if(i % 2 == 0):
        parzyste.append(i)
print(parzyste)

parzyste = [i for i in liczby if i % 2 == 0] 
# wynik z 'i' bedzie dodany do listy 'parzyste', dla karzdej kolejnej 'liczby' która spełna warunek (i modulo 2) = 0 czyli parzysta
print(parzyste)

parzyste=[i * 10 for i in liczby]
# przed przypisaniem każdej i do parzyste pomnóż i przez 10
print(parzyste)

# totalny skrót
print( [i for i in range(1, 21) if i % 2 == 0] )

# map z lambdą
print(list(map(lambda x : x * 2, liczby)))
# to samo, map z funkcją
def fun(x) :
    return x * 2
print(list(map(fun, liczby))) # do funkcji przekazywany jest każdy kolejnmy elemant jako parametr
# map(funkcja, iterator) 


