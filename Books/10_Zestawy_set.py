z = {}
z2 = set()

z3 = {1,2,3,4,5,6,7}
print(z3)

# zestawy nie posiadają powtórzeń 

# usunięci wartości powtarzających się
lista = [1, 'sd', 'sd', 2, 3, 1, 1]
print(lista)
z = set(lista)
print(z)

z.add('asdf') # dodanie do zestawu
print(z)
z.add('asdf') # próba dodania do zestawu, taki element już jest więc się go nie doda
print(z)

# zestawy się układają po swojemu, sortują, 
# modyfikować elementu nie można, ale można usunąć po wartości i dodać nowy

z.remove('asdf')
z.add('zxcv')

