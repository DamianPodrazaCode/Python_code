# --------------------------    
# filter
lista = [1,2,3]

def fun_odd(item):
    return item%2 != 0 # zwróci tylko te któresą większe od zera

print(list(filter(fun_odd, lista))) # [1, 3]
print(lista) # [1, 2, 3]

# --------------------------    
# zip
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
print(list(zip(lista1,lista2))) # [(1, 10), (2, 20), (3, 30)]

# --------------------------    
# reduce
from functools import reduce
lista = [1,2,3]

def accmulator(acc, item):  # acc po każdym returnie, dostaje wartość z returna
    print(acc, item)
    return acc + item

print((reduce(accmulator, lista, 0)))
# 0 1
# 1 2
# 3 3
# 6

# --------------------------    
# List Comprehensions
lista = [i for i in 'tekst']
print(lista) # ['t', 'e', 'k', 's', 't']

# jest to równoznaczne z:

lista = []
for i in 'tekst':
    lista.append(i)
print(lista) # ['t', 'e', 'k', 's', 't']

lista = [i for i in range(0, 10)]
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = [i*2 for i in range(0, 10)]
print(lista) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

lista = [i*2 for i in range(0, 10) if i % 2 == 0]
print(lista) # [0, 4, 8, 12, 16]

# --------------------------  
# Set Comprehensions, to samo co wyżej tylko zmieniają się nawiasy
set = {i for i in range(0, 10)}
print(set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
 
# --------------------------    
# Dict Comprehensions
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
dict = {key:value**2 for key,value in simple_dict.items()}
print(dict) # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
print(dict) # {'b': 4, 'd': 16}

dict = {i:i*2 for i in [1,2,3,4]}
print(dict) # {1: 2, 2: 4, 3: 6, 4: 8}
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    