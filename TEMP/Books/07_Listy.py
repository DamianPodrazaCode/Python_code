# konwersja napisu na listę
napis = 'asdfghjkl'
lista = list(napis)
print(napis)
print(lista)

# rozdzielenie napisu specjalnym znakiem
napis = 'asd fgh 123 543'
lista = napis.split(' ')
print(napis)
print(lista)

# złączenie w napis
napis = ''
singn = ':' # separator
napis = singn.join(lista)
print(napis)


lista = napis.split(':')
print(lista)
lista.sort() # tylko lista z niepomieszanymi typami
print(lista)
lista.reverse() # odwrotność listy
print(lista)
# można to zrobić za jednym zamachem
lista.sort(reverse=True);

print(len(lista)) # ilość elementów w liście
print(lista.count('asd')) # ilość wystąpieńdanego elementu
cLista = lista.copy() # kopia listy
print(cLista)
cLista = lista[1:4] # kopia części listy
print(cLista)

print(lista.index('asd')) # pobranie indexu elementu, jeżeli go nie ma to wywali błąd

#Listy składane

liczby = []
for x in range(1, 21) : 
    liczby.append(x)
print(liczby)

parzyste = []
for i in liczby:
    if(i % 2 == 0):
        parzyste.append(i)
print(parzyste)

parzyste = [i for i in liczby if i % 2 == 0] 
# wynik z 'i' bedzie dodany do listy 'parzyste', dla karzdej kolejnej 'liczby' która spełna warunek (i modulo 2) = 0 czyli parzysta
print(parzyste)

parzyste=[i * 10 for i in liczby]
# przed przypisaniem każdej i do parzyste pomnóż i przez 10
print(parzyste)

# totalny skrót
print( [i for i in range(1, 21) if i % 2 == 0] )

# map z lambdą
print(list(map(lambda x : x * 2, liczby)))
# to samo, map z funkcją
def fun(x) :
    return x * 2
print(list(map(fun, liczby))) # do funkcji przekazywany jest każdy kolejnmy elemant jako parametr
# map(funkcja, iterator) 


