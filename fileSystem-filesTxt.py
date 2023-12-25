import os, sys

print('-------------------start!!!')
print(__file__)  #ścieżka do pliku w tego kodu
print(sys.argv)
sFile = os.path.abspath(sys.argv[0]) #ścieżka do pliku w tego kodu
print(sFile)

fileName = 'testFile.txt'
#fileName = 'funkcje.py'
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

#ustawienie pozycji w pliku
file.seek(0)
print(file.tell(), os.stat(sFile).st_size)

#odczytanie całego pliku i wstawienie go do listy stringów
file.seek(0)
fileShow = file.readlines()
print(fileShow)

#odczyt i wyświetlenie linia po lini
file.seek(0)
for l in file.readlines():
    print(l.strip()) #strip - usuwa białe znaki na początku i końcu stringa

#close file
file.close()    

#zapis do pliku
def toFile(fileName, mode, data):
    f = open(fileName, mode)
    for i in range(5):
        f.write(str(i) + ':' + data + '\r\n')
    #f.flush() #szybki zapis bufora zapisu na dysk, niepotrzebny jak następny jest close()
    f.close() 

#overwrite
def writeFile(filename):
    toFile(filename, 'w', 'write test test test')        

#append
def appendFile(filename):
    toFile(filename, 'a', 'append test test test')        
        
#read        
def readFile(filename):
    if not os.path.exists(filename):
        print('File not found...')
        return
    f = open(filename, 'r')
    f.seek(0)
    print(f.read())
    f.close()

myFile = 'test.txt'
writeFile(myFile)
appendFile(myFile)
readFile(myFile)
