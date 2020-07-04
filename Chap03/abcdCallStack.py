def a():
    print('a() starts')
    b()
    d()
    print('a() stops')

def b():
    print('b() starts')
    c()
    print('b() stops')

def c():
    print('c() starts')
    print('c() stops')

def d():
    print('d() starts')
    print('d() stops')

a()