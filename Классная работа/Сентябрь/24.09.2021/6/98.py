for i in range(1, 1000000):
    s = i
    n = 32
    while n > s:
        s = s + 1
        n = n - 1
    if n >= 30:
        print(i)
        break
