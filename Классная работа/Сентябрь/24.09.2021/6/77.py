for i in range(10000):
    s = i
    n = 5
    while s < 110:
        n = n + 1
        s = s + n
    if n == 15:
        print(i)
