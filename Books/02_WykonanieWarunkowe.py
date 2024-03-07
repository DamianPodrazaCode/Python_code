print('---------------------------------------------operatory logiczne')
x = True #typ bool
y = False
print(type(x))


print('---------------------------------------------instrukcja warunkowa')
zm1 = 1
# w przypadku każdej instrukcji zakończonej ':' pod spodem jest albo pojedyncza instrukcjia albo blok instrukcji, 
# który jest wcięty, jest to jedyne oznaczenie bloku instrukcji w 'C' jesto to para '{}'
if zm1 > 0 : 
    print('jest większa od zera')

# czasami pisze się warunek ale jeszcze niema się ciała warunku, wtedy używa sie instrukcji pustej 'pass' tymczasowo
if zm1 != 0 :
    pass    

# składnia z else
if zm1 > 10 :
    pass
else :
    pass

# składnia z elif - wykona się tylko pierwszy prawdziwy warunek, jak go niebędzie to wykona się else
if zm1 > 10 :
    pass
elif zm1 < 5 :
    pass
elif zm1 == 0 :
    pass
else :
    pass

# try - except (jeżeli w 'try' wystąpi wyjątek to wykona się exept)
inp = input('Podaj temperaturę w skali Fahrenheita: ')
try:
    fahr = float(inp) # cast z worowadzonej liczby na float, tu może wystąpić wyjątek
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Musisz wprowadzić liczbę')

