# -------------- None
a = None
print(a) # None

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
