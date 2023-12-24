def test():
    print('ok')

def test2(str):
    print('param', str)
    return 'return ok'

test()
s = test2('okok')
print(s)

# pozycje argumentów
def test3(p1, p2, p3):
    print(p1, p2, p3)

test3('p1', 'p2', 'p3')  # pozycje podane prawidłowo,
test3('p1', 'p3', 'p1')  # pozycje podane nieprawidłowo
test3(p1='p1', p3='p3', p2='p2') # pozycje wymieszane ale przypisane prawidłowym

# funkcja z argumentem starowym
def fun(x=1):
    print(x)
    x += 1
    print(x)

fun()
fun(33)

# funkcja w funkcji
def fun1():
    def fun2():
        print('fun2 in fun1')
    print('fun1')
    fun2()

fun1()

# funkcja z nieznaną ilością argumentów
def fun(*args):
    for i in args:
        print(i)

fun('a1')
fun('a1', 'a2')
fun('a1', 2, 45, 12, 2.34)

# funkcja z argumentami typu key - val
def fun(**args):
    print(args)
    def disp(key):
        if key in args.keys():  # jeżeli w argumencie występuje klucz
            print(args[key])
    disp('arg1')
    disp('arg2')
    disp('arg3')
    if 'arg4' in args.keys():
        print('jest arg4', args['arg4'])

fun(arg1='111', arg2='222')
fun(arg1='111')
fun(arg1='111', arg2='222', arg3='333')
fun(arg4='ok')
fun(arg2='aaa', arg3='dsa')

# lambda

# normal
def fun(x=0, y=0):
    return x*y
print(fun(2,3))
print(fun(12,3))

#lambda
ret = lambda x=0, y=0: x*y
print(ret(2,3))
print(ret(12,3))
