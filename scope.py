y = 444

def fun():
    x = 111
    print(x)
    print(y)

def test():
    x = 222
    print(x)
    print(y)


fun()
test()
x = 0
while x < 10:
    print(x)
    x += 1
fun()
test()

