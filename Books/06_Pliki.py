print('---------------------------------------------uchwyt otwarcie')
import os, sys

print('ścieżka do pliku w tego kodu ', __file__) # ścieżka do pliku w tego kodu
print('lista argumentów ', sys.argv) # lista argumentów przy uruchamianiu programu
sFile = os.path.abspath(sys.argv[0]) # ścieżka do pliku w tego kodu, bo pierwszy argument to zawsze ścieżka do pliku uruchmianego
print('pierwszy argument ', sFile)

# sprawdzenie czy plik istnieje
fileName = 'Books/mbox.txt'
if not os.path.exists(fileName) :
    print('file not exist')
    exit(1)
else : 
    sFile = os.path.abspath(fileName) # 
    print(sFile)

# otwarcie pliku
fhand = open(fileName, 'r') 
print(fhand) # nazwa, tryb otwarcia pliku, kodowanie 
# zamknięcie pliku
fhand.close()

print('---------------------------------------------uchwyt zliczenie lini')
fileName = 'Books/mbox-short.txt'
if not os.path.exists(fileName) :
    print('file not exist')
    exit(1)
else : 
    sFile = os.path.abspath(fileName) # 
    print(sFile)

fhand = open(fileName, 'r') 

count = 0
for line in fhand :
    count += 1
print(count, 'lini w pliku')

fhand.close()

# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')
# print('---------------------------------------------')