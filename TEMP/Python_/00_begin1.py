
# lists -> uporzadkowana sekwencjas objektów
lista = [1, 2, 3, 4, 5]
lista = [1.23, 2.34, 3.45]
lista = ['str1', 'str2', 'str3','str4']
print(lista[1])
print(lista)
print(lista[0:1])
print(lista[0::2])
lista[0] = 'trs0' # w przeciwieństwie do string tu można wszystko zmieniać
print(lista)

lista_copy = lista[:] # kopiuje tworząc nową liste z nowym miejscem w pamięci
lista_copy[0] = 'copy'
print(lista, lista_copy) # ['trs0', 'str2', 'str3', 'str4'] ['copy', 'str2', 'str3', 'str4']

lista_copy = lista # kopia wskaźników
lista_copy[0] = 'copy' 
print(lista, lista_copy) # ['copy', 'str2', 'str3', 'str4'] ['copy', 'str2', 'str3', 'str4']
print(len(lista))

print('lista adding')
# adding
lista.append('add1')
print(lista) # ['copy', 'str2', 'insert', 'str3', 'str4', 'add1']
lista.insert(2, 'insert')
print(lista) #  ['copy', 'str2', 'insert', 'str3', 'str4', 'add1']
lista.extend('extend') 
print(lista) #  ['copy', 'str2', 'insert', 'str3', 'str4', 'add1', 'e', 'x', 't', 'e', 'n', 'd']
lista.extend(['extend']) # dodaje liste ['copy', 'str2', 'insert', 'str3', 'str4', 'add1', 'e', 'x', 't', 'e', 'n', 'd', 'extend']
print(lista)
lista = [1, 2, 3, 4, 5]
lista.append(10)
print(lista) # [1, 2, 3, 4, 5, 10]
lista.insert(2, 20)
print(lista) # [1, 2, 20, 3, 4, 5, 10]
lista.extend([30, 40])
print(lista) # [1, 2, 20, 3, 4, 5, 10, 30, 40]

print('list removing')
# removing
lista.pop() 
print(lista) # usuwanie ostatniego [1, 2, 20, 3, 4, 5, 10, 30]
lista.pop(0)
print(lista) # po indeksie od 0 [2, 20, 3, 4, 5, 10, 30]
lista.remove(20) 
print(lista) # po wartości [2, 3, 4, 5, 10, 30]
lista.clear()
print(lista) # []

# --------------
lista = ['str1', 'str2', 'str3', 'str4']
print(lista.index('str2')) # zwraca index stringa (1)
print(lista.index('str1', 0, 2)) # w zakresie od indexu 0 do indexu 2 (0)
print('str3' in lista) # sprawdzenie czy jest na liście
print('str3' in 'asd fde rew str2 str3') # sprawdzenie w stringach
lista.append('str2')
print(lista) # ['str1', 'str2', 'str3', 'str4', 'str2']
print(lista.count('str2')) # ilość wystąpień (2)

# -------------
print('sort')
lista.sort()
print(lista) # ['str1', 'str2', 'str2', 'str3', 'str4']
lista.append('str1')
print(lista) # ['str1', 'str2', 'str2', 'str3', 'str4', 'str1']
print(sorted(lista)) # zwraca posortowaną ale nie sortuje listy ['str1', 'str1', 'str2', 'str2', 'str3', 'str4']
print(lista) # ['str1', 'str2', 'str2', 'str3', 'str4', 'str1']
lista_copy = sorted(lista)
lista.append('111')
print(lista_copy) # ['str1', 'str1', 'str2', 'str2', 'str3', 'str4']
print(lista) # ['str1', 'str2', 'str2', 'str3', 'str4', 'str1', '111']
lista_copy = lista.copy() # tosamo co lista_copy = lista[:]
print(lista_copy) # ['str1', 'str2', 'str2', 'str3', 'str4', 'str1', '111']
lista.reverse()
print(lista) # ['111', 'str1', 'str4', 'str3', 'str2', 'str2', 'str1']
lista.sort(reverse=True) # ['str4', 'str3', 'str2', 'str2', 'str1', 'str1', '111']
print(lista)

# -------------
print('reverse reverse')
print(lista) # ['str4', 'str3', 'str2', 'str2', 'str1', 'str1', '111']
lista.reverse()
print(lista) # lista została odwrócona ['111', 'str1', 'str1', 'str2', 'str2', 'str3', 'str4']
print(lista[::-1]) # lista została wyświetlona jako odwrócona ['str4', 'str3', 'str2', 'str2', 'str1', 'str1', '111']
lista = lista[::-1]
print(lista) # a teraz została dopiero przepisana ['str4', 'str3', 'str2', 'str2', 'str1', 'str1', '111']
# ------------
print('range')
lista = list(range(10))
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = ['str1', 'str2', 'str3', 'str4']
sentence = ';'
lista_copy = sentence.join(lista)
print(lista_copy) # string (str1;str2;str3;str4)
napis = sentence.join(['asd', 'fgh', 'jkl'])
print(napis) # string asd;fgh;jkl
lista = napis.split(';')
print(lista) #['asd', 'fgh', 'jkl']
napis = ' '.join(lista)
print(napis) # string 'asd fgh jkl'

# ------------
lista = [1, 2, 3]
a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
print(c) # 3

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8, 9]

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8]
print(d) # 9

# -------------- None
a = None
print(a) # None

lista = list()
print(lista) # [] -> pusta lista
lista.append('str')
print(lista) # ['str']

# -------------- Dict (słownik) # nieuporządkowana mapa para->wartość 
print('Dictionary')
mapa = {
    'a': 1,
    'b': 2,
    'hex': 0x345a,
    'lista': [1,2,3,4,5]
}

print(mapa['b']) # 2
print(mapa) # {'a': 1, 'b': 2, 'hex': 13402, 'lista': [1, 2, 3, 4, 5]}

lista = [
    {
        'a': [1,2,3],
        'b': 'one',
        'c': True
    },
    {
        'a': [4,5,6],
        'b': 'two',
        'c': False
    },
    {
        123: [4,5,6],  # klucze mogą być jakiekolwiek byle by niebyły możliwe do zmiany "unchangeable"
        True: 'two',
        'c': False
    }
]
print(lista) # [{'a': [1, 2, 3], 'b': 'one', 'c': True}, {'a': [4, 5, 6], 'b': 'two', 'c': False}]
print(lista[0]) # {'a': [1, 2, 3], 'b': 'one', 'c': True}
print(lista[0]['b']) # 'one'
print(lista[0]['a'][1]) # 2
lista[0]['a'][1] = 34
print(lista[0]) # {'a': [1, 34, 3], 'b': 'one', 'c': True}

# -----------------
mapa = {
    'a': [1,2,3,4],
    'b': 'hello'
}
print(mapa) # {'a': [1, 2, 3, 4], 'b': 'hello'}

#print(mapa['c']) # error
print(mapa.get('c')) # None
print(mapa.get('c', 111)) # jeżeli nie ma pozycji 'c' to zwróć 111

# ----------------
print('a' in mapa.keys()) # True
print('hello' in mapa.keys()) # False
print('hello' in mapa.values()) # True
print(mapa.items()) # dict_items([('a', [1, 2, 3, 4]), ('b', 'hello')])

mapa2 = mapa.copy()
mapa.clear()
print(mapa) # {}
print(mapa2) # {'a': [1, 2, 3, 4], 'b': 'hello'}
mapa = mapa2.copy()
print(mapa.pop('b')) # hello
print(mapa) # {'a': [1, 2, 3, 4]}
mapa = mapa2.copy()

mapa.update({'a': 1234})
print(mapa) # {'a': 1234, 'b': 'hello'}
mapa.update({'aaa': 1234})
print(mapa) # jeżeli niema pola do update to doda nowe {'a': 1234, 'b': 'hello', 'aaa': 1234}

# ------------------ tuples () -> lista nie do edycji
tLista = (1, 2, 3, 4, 5)
print(tLista)
print(tLista[4])
# wszystko co w liscie oprócz zapisu

# ------------------ sets -> nieuporządkowana kolekcja objektów, do szybkich operacji na zbiorach
mySet = {1,2,3,4,5}
print(mySet) # {1, 2, 3, 4, 5}
mySet = {111,232,3.453,4.2,523}
print(mySet) # {3.453, 4.2, 232, 523, 111}
mySet = {111,232,3.453,4.2,523,111} # nie można dodać takiego samego elementu
print(mySet) # {3.453, 4.2, 232, 523, 111}
mySet.add(3.453)
print(mySet) # {3.453, 4.2, 232, 523, 111}

# usunięcie z lisy powtarzających się elementów
myList = [1,2,3,4,5,2,3,4,5]
print(myList) # [1, 2, 3, 4, 5, 2, 3, 4, 5]
mySet = set(myList)
myList = list(mySet)
print(myList) # [1, 2, 3, 4, 5]

# set - brak dostępu przez index
print(2 in mySet) # True

# -----------------
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.difference(set2)) # {1, 2, 3} wyświetliło różnice (różnica bez zmian w set1, set2)
print(set1.discard(5)) # usunięcie 5
print(set1) # {1, 2, 3, 4}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
set1.difference_update(set2)
print(set1) # {1, 2, 3} usuneło wszystko co było takiesamo w set2 (różnica ze zmianami w set1)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.intersection(set2)) # {4, 5} część wspólna bez zmian w set1
print(set1) # {1, 2, 3, 4, 5}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
set1.intersection_update(set2) 
print(set1) # {4, 5} część wspólna ze zmianą w set1

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.isdisjoint(set2)) # czy zbiory są rozłączne False

set1 = {1,2,3}
set2 = {4,5,6,7,8,9,10}
print(set1.isdisjoint(set2)) # czy zbiory są rozłączne True

set1 = {4,5,6}
set2 = {4,5,6,7,8,9,10}
print(set1.issubset(set2)) # czy set1 jest podzbiorem set2

set1 = {4,5,6,7}
set2 = {4,5}
print(set1.issuperset(set2)) # czy set2 jest podzbiorem set1

set1 = {4,5,6,7}
set2 = {4,5,10,11,12}
print(set1.union(set2)) # łączenie {4, 5, 6, 7, 10, 11, 12}
print(set1 | set2) # jw {4, 5, 6, 7, 10, 11, 12}
print(set1 & set2) # {4, 5}
