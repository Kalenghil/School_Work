def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n // 2
    return 1 + f(n - 1)


counter = 0
for i in range(1, 901):
    print(i, f(i))

print(counter)
