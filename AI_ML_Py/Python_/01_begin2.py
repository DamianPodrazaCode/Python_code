# --------------------------
war1 = True
war2 = False
if war1:
    print(war1)
elif war2:
    print(war2)
else:
    print('end')
    
# --------------------------    
# thernary operator
print('ok') if (war1) else print('else')
#"wykonaj" if "warunek" else "wykonaj to"

# --------------------------    
# and or not
# < > <= >= == !=
# is - porównanie w pamięci, zmienna musi być w tym samym miejscu w pamięci
# a = 10
# b = 10
# a is b -> False, a == b -> True
# --------------------------    
for item in 'text': 
    print(item)

for i in (1,2,3,4,5,6,7):
    print(i)

for i in [[1,2,3], 'asd', 123, 12.34]:
    print(i)

for i in range(10):
    print(i)
   
for i in range(1, 10, 2): #range(start, stop, step)
    print(i)

print('do tyłu')
for i in range(10, 0, -1): # od dtyłu range(start, stop, step)
    print(i)

# --------------------------    
# enumerate
for char in enumerate('text test'):
    print(char)
# (0, 't')
# (1, 'e')
# (2, 'x')
# (3, 't')
# (4, ' ')
# (5, 't')
# (6, 'e')
# (7, 's')
# (8, 't')
for i, char in enumerate('text test'):
    print(i, char)
# 0 t
# 1 e
# 2 x
# 3 t
# 4
# 5 t
# 6 e
# 7 s
# 8 t    

# --------------------------    
lista = [1,2,3,4,5,6]
i = 0
while i < len(lista):
    print(i)
    i += 1
    
#break, continue, pass    
    
# while True:
#     respone = input('in <<<')    
#     if respone == 'stop':
#         break

# while True:
#     respone = input('in <<<')    
#     if respone == 'stop':
#         break
#     if respone == 'rep':
#         continue
#     print(respone)

pass  # -> NOP
# np. jak jest już stworzona pętla a niema ciała to daje się pass
for i in range(10):
    pass #coś tu będzie

# --------------------------    
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

print('tekst') # na końcu ma domyślnie zakończenie lini
print('tekst', end='') # a tak nie ma, albo ma co mu wpiszemy
print('tekst')

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# --------------------------    
def fun1():
    print('in fun')
fun1()

# --------------------------    
def fun2(param1, param2):
    print(param1)
    print(param2)

fun2('param fun', 12.34)
fun2(231, 1)

# --------------------------    
def fun3(param1='asd', param2='fgh'):
    print(param1)
    print(param2)

fun3()
fun3(123,456)
fun3(param1='dsa', param2='fds432')
fun3(param2='dsa', param1='fds432')
fun3('sadasd')

# --------------------------    
def fun4(p1 = 0, p2 = 0):
    return p1 + p2

print(fun4(1.1, 2.1))

# --------------------------    
#info funkcji 
def fun_info():
    '''to jest info które się wyświetli w helpie funkcji'''
    pass

fun_info()
print(fun_info.__doc__) # a to jest tekst pomocy

# --------------------------  
# *args **kwargs

def fun(*args):
    print(*args) # 1 2 3 4 5  -> elementy po kolei
    print(args) # (1, 2, 3, 4, 5) -> tuple elementów
    return sum(args)
print(fun(1, 2, 3, 4, 5)) # 15

def fun(**kwargs):
    print(*kwargs) # param1 param2 ->lista parametrów
    print(kwargs) # {'param1': 'aaa', 'param2': 12} -> parametry i wartości w postaci dict
fun(param1='aaa', param2=12)    

def fun(*args, **kwargs):
    print(*args) # 1 2 3 4 5  -> elementy po kolei
    print(args) # (1, 2, 3, 4, 5) -> tuple elementów
    print(*kwargs) # param1 param2 ->lista parametrów
    print(kwargs) # {'param1': 'aaa', 'param2': 12} -> parametry i wartości w postaci dict
fun(1, 2, 3, 4, 5, param1='aaa', param2=12)

#regóła: params, *args, default params, **kwargs

# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    
# --------------------------    