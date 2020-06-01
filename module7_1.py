import math


def S(x):
    return 5 ** 0.5 * (5 + 2 * 5 ** 0.5) ** 0.5 / 4 * x ** 2 * 12 + 3 * 3 ** 0.5 / 2 * x ** 2 * 20


def S_ceil(x):
    return math.ceil(S(x))


a = 3
b = 4

from scipy.optimize import golden
def f(x):
    return (x + a) ** 2 - b


def g(x):
    return abs(f(x))

# print(golden(f), golden(g))
print(f(golden(f)),g(golden(g)))

