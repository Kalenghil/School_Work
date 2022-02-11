for i in range(10000):
    s = i
    n = 1
    while s > 20:
        s -= 3
        n = n * 3 + 1

    if n == 3280:
        print(i)