import math


def f(n):
    if n <= 1:
        return n * 2
    return f(n - 1)**g(n - 1)


def g(n):
    if n <= 2:
        return n + 1
    return f(n - 1) + 2 * g(n - 1)


a = f(3) / g(1)
b = math.sqrt(2 * g(3) + g(2) + g(1)) / 2 * g(1) + 1

print(a, b, a + b)
