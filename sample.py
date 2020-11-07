from math import sin
from time import sleep

def f(x):
    return 10.0 * sin(x)

def compute(n):
    x = 1
    for i in range(n):
        x = f(x)
    return x

def fun1():
    return compute(3*10**5)

def fun2():
    return compute(5*10**5)

def fun3():
    sleep_()
    return compute(7*10**5)

def sleep_():
    sleep(0.1)


def main():
    sum = fun1() + fun2() + fun3()
    sleep_()
    print('Calculated sum: {:.3f}'.format(sum))


if __name__ == '__main__':
    main()
