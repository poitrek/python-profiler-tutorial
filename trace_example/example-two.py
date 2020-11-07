from random import randint

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(randint(10, 1000), randint(10, 1000)))
