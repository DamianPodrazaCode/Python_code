
print('---------------------------------------------wartości i typy')
# wartości i typy
# instrukcjia type() zwraca typ wartości
print(type(17)) #int
print(type(1.123)) #float
print(type('asd')) #string
print(type(1 + 5j)) #complex (liczby zespolone)

print('---------------------------------------------zmienne')
# zmienne, w python nie ma potrzeby deklarowania zmiennej parser wywnioskuje sobe sam jaki to typ
zm1 = 10
print(type(zm1))
zm2 = 1.23
print(type(zm2))
# jeżeli w trakcie programu zmieni się typ interpreter sie tym zajmnie sam
zm2 = 'text'
print(type(zm2))

''' 35 słów kluczowych w python:
and   del   from   None   True   as   elif   global   nonlocal   try   assert   else   if   not   while   break   except   import
or   with   class   False   in   pass   yield   continue   finally   is   raise   async   def   for   lambda   return   await
'''

print('---------------------------------------------operatory')
# operatory
'''
** -> potęgowanie
* -> mnożenie
/ -> dzielenie
// -> dzielenie całkowite
% -> reszta z dzielenia (jak jest podzielne całkowicie == 0)
+ -> dodawanie
- -> odejmowanie
operacje '+' na napisach to konkatencja (sklejanie)
'''
zm1 = 'text1'
zm2 = 'text1'
print(zm1 + " " + zm2)

print('---------------------------------------------wprowadzanie danych')
# wprowadzanie danych z klawiatury 
zm1 = input('input text:') 
print('wprowadzono ', zm1)


