lista = [111,222,'333', True, 1.23]
# tuple to praktucznie listy tylko - tylko do odczytu
krotka = ('asd', 123, 0xa5, -1.234)
print(krotka)
krotka = tuple() # inicjalizacja pustej krotki
krotka = () # jw
krotka = tuple(lista) # kopia z listy do krotki, jak si niedoda rzutowania to powstanie lista
# krotka to szybki dostęp do danych
print(lista, krotka)
print(krotka[1:]) # dostęp do odczytu z krotki jest takisam jak z listy