for i in range(1, 10000):
    s = i
    n = 5
    while s > 5:
        s = s // 2
        n = n + 4
    if n == 29:
        print(i)
