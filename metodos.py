from pylab import *


def f(x):
    return (x/2)**2 - sin(x)


def df(x):
    return x/2 - cos(x)


def falsa_posicao(a, b, e, itmax):
    it = 0
    x = a
    er = 1
    while er >= e and it < itmax:
        xold = x
        x = a - f(a)*(b-a)/(f(b)-f(a))
        er = abs((x-xold)/x)
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        it += 1
    return x, er, it


def newton(xo, e, itmax):
    it = 1
    while abs(f(xo)) > e and it < itmax:
        x = xo - f(xo)/df(xo)
        xo = x
        it += 1
    return xo, it, f(xo)

