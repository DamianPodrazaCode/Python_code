print('---------------------------------------------napisy')
string = 'to je napis '
string = "to je napis " # to samo co wyżej

print(string[0]) # dostęp do pola
print(len(string))  # długość
print(string * 3)  # powielenie
print(string.replace('.', '!'))  # zamiana
print(string.replace('string', 'str'))  # zamiana
print(string.split('-'))  # rozdzielenie d dwóch stringów
print(string.startswith('j'))  # czy zaczyna się na
print(string.startswith('.'))  # czy zaczyna się na
print(string.endswith('.'))  # czy kończy się na
print(string[2:10])  # wycinek od do
print(string[2:])  # wycinek od do końca
print(string[:10])  # wycinek od początku do
print(string[-5:])  # wycinek ostatnich 5
print(string.find(' '))   # -1 jak nie znajdzie
print(string.find(' ', 6, 10))  # znajdź w wycinku, -1 jak nie znajdzie
# print(string.index('#'))  # jak nieznajdzie to error
# print(string.index(' ', 6, 10)) # znajdź w wycinku jak nieznajdzie to error
print(string.upper()) # na duże
print(string.lower()) # na małe
print(string.strip()) # usówa białę znaki na początku i końcu

print('---------------------------------------------porównywanie')
napis = 'abcd' 
if 'a' in 'abc' :   # sprawdza czy 'a' zawiera się w 'abc' w tym przypadku to True
    pass
if napis == 'abcd' : # czy równe 
    pass
if napis < 'abcd' : # czy napis jest przed 'abcd'
    pass
if napis == 'abcd' : # czy napis jest za 'abcd'
    pass

print('---------------------------------------------dąstępne metody')
# print(dir(napis)) # dir to lista dostępnych metod w objekcie
# print(help(str)) # manual dla klasy

print('---------------------------------------------formatowanie')
'''
'd' - Signed integer decimal.
'i' - Signed integer decimal.
'o' - Signed octal value.
'u' - Obsolete type - it is identical to 'd'.
'x' - Signed hexadecimal (lowercase).
'X' - Signed hexadecimal (uppercase).
'e' - Floating point exponential format (lowercase).
'E' - Floating point exponential format (uppercase).
'f' - Floating point decimal format.
'F' - Floating point decimal format.
'g' - Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
'G' - Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
'c' - Single character (accepts integer or single character string).
'r' - String (converts any Python object using repr()).
's' - String (converts any Python object using str()).
'a' - String (converts any Python object using ascii()).
'%' - No argument is converted, results in a '%' character in the result.
'''

zm1 = 15
zm2 = 1.23
zm3 = -1.23

print('text %d text %f text %+f' % (zm1, zm2, zm3)) # formatowanie
print('text %+d text %+f text %+f' % (zm1, zm2, zm3)) # formatowanie ze znakiem plus normalnie nie wyświetlanym
napis = 'text %03d text %f' % (zm1, zm2)
print(napis)
print('text %04d text % 4d' % (zm1, zm1)) # formatowanie, zero przed liczbą lub spacja przed liczbą
print('text %f' % (zm2)) # formatowanie, zero przed liczbą lub spacja przed liczbą

