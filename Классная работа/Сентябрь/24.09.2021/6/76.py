for i in range(10000):
    s = i
    n = 0
    while s + n <= 300:
        s = s - 5
        n = n + 25
    if n == 250:
        print(i)
        break
