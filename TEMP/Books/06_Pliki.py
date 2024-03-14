print('---------------------------------------------uchwyt otwarcie')
import os, sys

print('---------------------------------------------czytanie txt z filtrowaniem wybieranie')
fhand.seek(0) # ustawienie pozycji w pliku na początek
for line in fhand : # domyślnie w czasie iteracji do line są wrzucane linie pliku
    if line.startswith('From:') : # sprawdzenie 
        print(line.rstrip()) # wyświetlenire lini z usunięciem końca linii

print('---------------------------------------------czytanie txt z filtrowaniem pominięcia')
fhand.seek(0) # ustawienie pozycji w pliku na początek
for line in fhand : # domyślnie w czasie iteracji do line są wrzucane linie pliku
    if not ( line.startswith('From:') or line.startswith('Subject:') ) : # sprawdzenie 
        continue
    else :
        print(line.rstrip()) # wyświetlenire lini z usunięciem końca linii

fhand.close()


print('--------------------------------------------- zapis')
fileName = 'Books/outTest.txt'
sFile = os.path.abspath(fileName) 

try :
    fhand = open(fileName, 'w', encoding='UTF-8') 
    print(fhand) 
except :
    print('Nie można zapisać:', sFile)
    sys.exit(0)

line = 'ęóąśłżźćń text text text\n' 
fhand.write(line)
fhand.write(line)

# fhand.flush() # nie musi być jeżeli za nią jest close()
fhand.close()

