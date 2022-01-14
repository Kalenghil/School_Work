for i in range(10000):
    n = list(map(int, list(str(i))))
    s1 = sum(list(filter(lambda x: x % 2 == 0, n)))
    s2 = sum(n[1::2])
    if abs(s2 - s1) == 11:
        print(i)