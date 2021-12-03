def divisor(num):
    for i in range(18, num // 2 + 1):
        if num % i == 0 and i % 10 == 8:
            return i
    return 1


n = 500_000
len_ans = 0
while True:
    n += 1
    div = divisor(n)
    if div != 1:
        len_ans += 1
        print(n, div)
    if len_ans >= 5:
        break
