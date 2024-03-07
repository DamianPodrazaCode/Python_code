print('---------------------------------------------while break continue')
zm1 = 0
while zm1 < 10 : # wykonuj dopóki zm1 mniejsze od 10
    print(zm1)
    zm1 += 1
print('end while')    

# Instrukcja "break" służy do przerywana działania pętli.
zm1 = 10
while True : # pętla nieskończona
    if zm1 <= 0 :
        break
    print(zm1)
    zm1 -= 1
print('end while')    

# Instrukcja "continue" powoduje przeskok do następnego obrotu pętli.
zm1 = 10
while True :
    zm1 -= 1
    if zm1 % 2 : # jeżeli wynik z dzielenia ma reszte to pomin ta pętle i wykonaj następną
        continue
    if zm1 <= 0 :
        break 
    print(zm1)
print('end while')    

print('---------------------------------------------for')
# for to pętla iteracyjna, całkiem inna niż w C
# iteracja wg listy, for przejedzie przez całą listę pokolei od elementu pierwszego
lista = ['jeden', 'dwa', 'trzy', 'cztery', 'pięć'] 
for str in lista : 
    print(str)
print('end for')

# lista wbudowana w for'a
for str in [2, 3, 4, 5, 3, 567, 23423, 564, 23, 12334, 45, 45, 3] :
    print(str)
print('end for')

# iteracja oparta na zakresie liczbowym
# range([start],stop,[step]) - tylko liczby całkowite
for str in range(10) : # będzie liczyć od 0 do 9
    print(str)
print('end for')

for str in range(2,50) : # bedzie liczyć o 2 do 49
    print(str)
print('end for')

for str in range(20,1,-1) : # bedzie liczyć o 20 do 2
    print(str)
print('end for')

for str in range(5,20,2) : # bedzie liczyć o 5 do 19 z krokiem co 2
    print(str)
print('end for')

