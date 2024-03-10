# try - except (jeżeli w 'try' wystąpi wyjątek to wykona się exept)
inp = input('Podaj temperaturę w skali Fahrenheita: ')
try:
    fahr = float(inp) # cast z worowadzonej liczby na float, tu może wystąpić wyjątek
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Musisz wprowadzić liczbę')

