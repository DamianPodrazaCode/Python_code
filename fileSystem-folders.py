import os
path = os.getcwd() #katalog roboczy
print(path)

os.chdir('d:/') #zmień katalog
print(os.getcwd())

os.chdir(path)
print(os.getcwd())

print(os.listdir()) # wylistowanie katalogu, pliki i katalogi

print('--------ListDir')
for f in os.listdir():  # wylistowanie katalogu, pliki i katalogi i pełna ścieżka dostępu
    # print('file name ', f) #sama nazwa pliku
    # print('cała ścieżka ', os.path.abspath(f)) #cała absolutna ścieżka plus nazwa pliku lub katalogu
    if os.path.isdir(f):
        print('katalog ', os.path.abspath(f))
    if os.path.isfile(f):
        print('plik ', os.path.abspath(f))

print('--------ScanDir')
for e in os.scandir():
    # print(e)   
    # print('name ', e.name)             
    # print('path ', e.path)
    if e.is_dir():
        print('katalog ', e.name)
    if e.is_file():
        print('plik ', e.name)

print('--------RecrusiveScan')        
import glob
os.chdir('..') #katalog wyżej
dir = os.getcwd()

for filename in glob.glob(pathname=dir + '**/**', recursive=True):
    print(filename)

print('--------Walk')        
for currenPath, folders, files in os.walk('.'):
    for file in files:
        print(os.path.join(currenPath, file))

