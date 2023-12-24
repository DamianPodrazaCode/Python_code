def test():
    print('ok')


def test2(str):
    print('param', str)
    return 'return ok'



test()
s = test2('okok')
print(s)