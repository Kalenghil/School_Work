for i in range(1, 10000):
    s = i
    n = 50
    while s > 0:
        s = s // 2
        n = n - 3
    if n == 23:
        print(i)
