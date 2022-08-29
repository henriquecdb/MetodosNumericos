from pylab import *


def f(x):
    return (x/2)**2 - sin(x)


def falsa_posicao(a, b, erro, itMax):
    it = 0
    x = a
    Er = 1
    while (Er >= erro and it < itMax):
        xold = x
        x = a - f(a)*(b-a)/(f(b)-f(a))
        Er = abs((x-xold)/x)
        if (f(a)*f(x) < 0):
            b = x
        else:
            a = x
        it += 1
    return (x, Er, it)


def ponto_fixo():
    pass


def newton():
    pass


def secantes():
    pass

