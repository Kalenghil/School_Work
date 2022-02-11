for i in range(1000, 10000):
    num = i
    a, b, c, d = list(map(int, list(str(num))))
    fst, snd = a * d, c * b
    ans = ''.join(list(map(str, sorted([fst, snd]))))
    if ans == '345':
        print(i)
