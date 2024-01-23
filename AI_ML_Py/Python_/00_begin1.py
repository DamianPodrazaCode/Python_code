# podstawowe typy 
int
float
complex
str
bool
list
tuple
set
dict

print(6)
print(type(6))
print(0.1)
print(type(0.1))
print(2 / 5)
print(type(2 / 5))

print(2 ** 2) # pow
print(2 // 2) # dzielenie całkowite zwraca int
print(2 % 2) # module - rzeszta z dzielenia
print(2 / 2) # dzielenie zmiennoprzecinkowe

print(round(3.123)) # zaokrągleni, bez przecinków
print(round(3.123, 1)) # zaokrąglenie z wyznaczeniem ile miejsc po przecinku

print(bin(5)) # reprezentacja binarna
print(hex(234)) # repezentacja hex
print(int(0xabcd)) # reprezenntacja dziesiętna
print(int(0b011011))
print(int('0b011011', 2))

a,b,c = 1,2,3
print(a)
print(b)
print(c)

aaa = 10
aaa += 2
aaa -=3
aaa *= 0.2
print(aaa)

#string
print(type('asdsfsd'))
napis = "sdfsdf"
long_str = '''asdfas
asdfasd
asdasd
asasdasd
asdf
'''
print(long_str)
print('sdfgh' + ' aaa' * 5)

# casting
a = str(100.23)
b = float(a)
c = type(b)
print(a, b, c)

# formatowany string
str1 = "str1"
str2 = "str2"
data1 = 12
data2 = 23.45
print(f'to str1 {str1} str2 {str2} data1 {data1} data2 {data2}') # python3
print('to str1 {} str2 {} data1 {} data2 {}'.format('a', str2, 'c', data2)) # python2
print('to str1 {3} str2 {1} data1 {2} data2 {0}'.format('a', str2, 'c', data2)) # python2
print('to str1 {} str2 {aaa} data1 {bbb} data2 {ddd}'.format('a', aaa=34, bbb='c', ddd=data2)) # python2
string = (f'to str1 {str1} str2 {str2} data1 {data1} data2 {data2}')
print(string)

string = '012345678'
print(string[0:9]) # (012345678)
print(string[0:9:2])  # wyświetl co drugi (02468)
print(string[:5]) # od początku do 5 (01234)
print(string[3:]) # (345678)
print(string[:]) # (012345678)
print(string[::]) # (012345678)
print(string[::3]) # co trzy (036)
print(string[-2]) # druga od końca (7)
print(string[::-1]) # revers co jeden (876543210)
print(string[::-2])  # revers co dwie (86420)
#print(string[start:stop:step]) 
#string[1] = 's' -> error nie wolno, trzeba nadpisać całego stringa

print('str3' in 'asd fde rew str2 str3') # sprawdzenie stringa w stringu, true jeżeli 'str3' istnieje w drugim stringu


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

# -------------- Dict # nieuporządkowana mapa para->wartość 
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
    }
]
print(lista) # [{'a': [1, 2, 3], 'b': 'one', 'c': True}, {'a': [4, 5, 6], 'b': 'two', 'c': False}]
print(lista[0]) # {'a': [1, 2, 3], 'b': 'one', 'c': True}
print(lista[0]['b']) # 'one'
print(lista[0]['a'][1]) # 2
lista[0]['a'][1] = 34
print(lista[0]) # {'a': [1, 34, 3], 'b': 'one', 'c': True}

# -----------------
