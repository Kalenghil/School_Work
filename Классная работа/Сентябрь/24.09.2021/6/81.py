for i in range(8, 10000, 10):
    d = i
    S = 15
    N = 10
    while S <= 2400:
        S = S + d
        N = N + 5
    if N == 50:
        print(i)
