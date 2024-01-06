print('---------------------------------------------Lista')
'''
* jest sekwencja elementów
* elementy mogą być dowolnego typu
* mogą być mieszane na jednej liście
* liste tworzy się za pomocą nawiasów kwadratowych []
'''
lista = [] # stworzenie listy pustej
lista = list() # jw.
lista.append('asd') # dodanie elementu do listy
lista.insert(1, 'insert1') # wciśnięcie na pozycję 1
lista.append(123) 
lista.append(123.12) 
lista.append(10 + 15j)
lista.append([12, 3.4, 'ghj']) # dodanie listy jako elementu
print(lista)

lista = [12, 3.45, 'ytr', [1, 2, 3]] # stworzenie listy bezpośrednio
print(lista)

lista[0] = 'text' # bezpośredni dostęp do listy
lista[1] = 12 + 6j
print(lista)

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

