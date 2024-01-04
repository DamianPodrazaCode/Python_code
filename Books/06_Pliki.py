print('---------------------------------------------uchwyt otwarcie')
import os, sys

print('ścieżka do pliku w tego kodu ', __file__) # ścieżka do pliku w tego kodu
print('lista argumentów ', sys.argv) # lista argumentów przy uruchamianiu programu
sFile = os.path.abspath(sys.argv[0]) # ścieżka do pliku w tego kodu, bo pierwszy argument to zawsze ścieżka do pliku uruchmianego
print('pierwszy argument ', sFile)

# sprawdzenie czy plik istnieje
fileName = 'mbox.txt'
if not os.path.exists(fileName) :
    print('file not exist')
    sys.exit(0)
else : 
    sFile = os.path.abspath(fileName) # 
    print(sFile)

# otwarcie pliku
fhand = open(fileName, 'r') 
print(fhand) # nazwa, tryb otwarcia pliku, kodowanie 
# zamknięcie pliku
fhand.close()

print('---------------------------------------------uchwyt zliczenie lini')
fileName = 'mbox-short.txt'
if not os.path.exists(fileName) :
    print('file not exist')
    sys.exit(0)
else : 
    sFile = os.path.abspath(fileName) # 
    print(sFile)

fhand = open(fileName, 'r', encoding='UTF-8') 

print('---------------------------------------------czytanie txt linia po linii')
count = 0
for line in fhand : # domyślnie w czasie iteracji do line są wrzucane linie pliku
    count += 1
    # print(line) # wyświetlanie linia po linii
print(count, 'lini w pliku')

print('---------------------------------------------czytanie txt w całości')
fhand.seek(0) # ustawienie pozycji w pliku na początek
plik = fhand.read() # odczyt całego pliku do stringa (tylko małe pliki)
print(plik)
print('rozmiar to ', len(plik), ' bajtów')
del plik # usunięcie zmienne plik

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

print('---------------------------------------------zabezpieczenie try - exept')
fileName = 'Books/mbox.txt'
sFile = os.path.abspath(fileName) 

try :
    fhand = open(fileName, 'r', encoding='UTF-8') 
    print(fhand) 
except :
    print('Nie można otworzyć:', sFile)
    sys.exit(0)

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

