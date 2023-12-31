print('---------------------------------------------Słowniki: pary key value')
d = {} # pusty słownik
d['jeden'] = '1' # dodanie pary elementów, pary są dowolne typowo w prtzypadku klucza jak i wartości
d[2.0] = 'dwa'
d['text'] = 1 +23j
d[1.23] = 2.34
print(d)

d = {'text': 12, 23: 32, 12.32: 'asd'} # definicja słownika odrazu z wieloma elementami
print(d)
# albo
dd = dict(text = 12, asd = 32.23, dfg = 'asd') 
print(dd)

print(d[23]) # dostęp do wartość poprzez klucz
print(d.items())  # wyświetlenie w formacie par
print(d.keys())  # same klucze
print(d.values())  # same wartości
d[23] = 'zmiana' # jeżeli para istnieje to odwołanie się do istniejącego klucza zmienia poprostu wartość przy tym kluczu
print(d[23]) # dostęp do wartość poprzez klucz
print(d)
# nie można  zmienić nazwy klucza trzeba go poprostu usunąć i stworzyć nową pare
del d[23] # usunięcie pary
print(d)

print('text' in d) # sprawdzenie czy istnieje klucz



# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')