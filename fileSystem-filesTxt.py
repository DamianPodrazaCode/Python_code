import os, sys

print('-------------------start!!!')
print(__file__)  #ścieżka do pliku w tego kodu
print(sys.argv)
sFile = os.path.abspath(sys.argv[0]) #ścieżka do pliku w tego kodu
print(sFile)

print('-------------------exist')
fileName = 'testFile.txt'
if not os.path.exists(fileName):
    print('file not exist')
    exit(1)
else: 
    sFile = os.path.abspath(fileName)
    print(sFile)

file = open(sFile, 'r')

#odczyt jednej linii
line = file.readline()
print(line)

#odczyt określonej ilości znaków
chr = file.read(15)
#print(type(chr))
print(chr)

#pozycja odczytu znaku, rozmiar pliku
print(file.tell(), os.stat(sFile).st_size)