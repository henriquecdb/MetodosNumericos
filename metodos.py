from pylab import *


def f(x):
    return x**4 - 78


def df(x):
    return 4*x**3


def falsa_posicao(a, b, tol, kmax):
    k = 0
    x = a
    er = 1
    while er >= tol and k < kmax:
        xo = x
        x = (a*f(b) - b*f(a))/(f(b)-f(a))
        er = abs((x-xo)/x)
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        k += 1
    return x, er, k


def newton(xo, tol, itmax):
    it = 0
    while abs(f(xo)) > tol and it < itmax:
        x = xo - f(xo)/df(xo)
        xo = x
        it += 1
    return xo, f(xo), it
