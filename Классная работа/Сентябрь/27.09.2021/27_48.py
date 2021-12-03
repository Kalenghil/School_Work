import math

file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\48\27-48b.txt"
with open(file_path, 'r') as f:
    amount = int(f.readline())
    nums, diff = list(), math.inf
    summ = 0
    even_counter = 0
    for i in range(amount):
        s = f.readline().split()
        a, b = list(map(int, s))
        if abs(a - b) % 2 == 1:
            diff = min(abs(a - b), diff)
        summ += max(a, b)
        if (a + b) % 2 == 0:
            even_counter += 1

odd_counter = amount - even_counter
print(even_counter, odd_counter)
if summ % 2 == 0:
    if odd_counter > even_counter:
        print(summ - diff)
    else:
        print(summ)
elif summ % 2 == 1:
    if odd_counter < even_counter:
        print(summ - diff)
    else:
        print(summ)

# 411037387 411037387
# 117046 117046
