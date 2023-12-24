import os
path = os.getcwd() #katalog roboczy
print(path)

os.chdir('d:/') #zmień katalog
print(os.getcwd())

os.chdir(path)
print(os.getcwd())

print(os.listdir()) # wylistowanie katalogu, pliki i katalogi
for f in os.listdir():
    print(f)