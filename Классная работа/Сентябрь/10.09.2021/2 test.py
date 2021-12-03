for c in range(2):
    for b in range(2):
        for a in range(2):
            print(a, b, c, int((not (a or b) or (b == c))))
