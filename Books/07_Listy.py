print('---------------------------------------------Lista')
'''
* jest sekwencja elementów
* elementy mogą być dowolnego typu
* mogą być mieszane na jednej liście
* liste tworzy się za pomocą nawiasów kwadratowych []
'''
lista = [] # stworzenie listy pustej
lista.append('asd') # dodanie elementu do listy
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


# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')