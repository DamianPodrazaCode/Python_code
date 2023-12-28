#odsłonięcie zmiennej globalnej
counter = 0  #zmienna globalna

def count(max):
    global counter #teraz niema zmiennej lokalnej wszystkie odwołania zą do zmiennej globalnej
    counter += 1 #odwołanie do zmiennej lokalnej
    print(counter)

count(1)   

#Walrus operator ":="
(y := len('sdfgdf'))
print(y)

