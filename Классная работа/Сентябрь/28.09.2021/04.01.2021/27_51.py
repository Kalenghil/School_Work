import math
from pprint import pprint


def my_sort(a):
    a[0].sort()
    a[1].sort()


# file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\51\27-51b.txt"
file_path = r'27-51c.txt'
with open(file_path, 'r') as f:
    amount = int(f.readline())
    nums, diff = list(), math.inf
    summ = 0
    diffs = [list(), list()]
    even_counter = 0
    for i in range(amount):
        line = f.readline()
        print(line)
        b, a = sorted(list(map(int, line.split())))
        if abs(a - b) % 2 == 1:
            diff = min(abs(a - b), diff)
            diffs[a % 2].append(abs(a - b))
        summ += min(a, b)
        if min(a, b) % 2 == 0:
            even_counter += 1

my_sort(diffs)

odd_counter = amount - even_counter
print(even_counter, odd_counter)
pprint(diffs)
diff1, diff2 = 0, 0
print(summ)
if abs(even_counter - odd_counter) != 1:
    if summ % 2 == 0:
        if odd_counter > even_counter:
            print(summ)
        else:
            print(summ + diff)
    elif summ % 2 == 1:
        if odd_counter < even_counter:
            print(summ)
        else:
            print(summ + diff)
elif odd_counter - even_counter == 1:  # нечётных больше на 1
    if summ % 2 == 0:
        print(summ)
    else:
        diff1 = diffs[1][0]
        diff2 = diffs[0][0] + diffs[0][1]
        print(summ + min(diff1, diff2))
elif even_counter - odd_counter == 1:
    if summ % 2 == 1:
        print(summ)
    else:
        diff1 = diffs[0][0]
        diff2 = diffs[1][0] + diffs[1][1]
        print(summ + min(diff1, diff2))

# a: my) 62276  ans) 62276
# b: my) 190343719 ans) 190343719
