answ = 0
for i in range(1, 10000):
    s = i // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        answ = max(answ, i)
print(answ)
