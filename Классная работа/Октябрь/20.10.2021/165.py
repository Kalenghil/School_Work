import math
from functools import reduce


def mult(*args):
    return reduce(lambda x, y: x * y, args)


filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
min_av = math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    summ = a + b + c
    if (any(num % 12 == 0 for num in (a, b, c))
            and all(num % 3 == 0 for num in (a, b, c))):
        amount += 1
        min_av = min(min_av, summ / 3)

print(amount, min_av)
