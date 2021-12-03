import math
from functools import reduce


def mult(*args):
    return reduce(lambda x, y: x * y, args)


filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
max_sum = -math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    summ = a + b + c
    if mult(a, b, c) % 7 == 0 and str(summ)[-1] == '5':
        amount += 1
        max_sum = max(max_sum, summ)
print(amount, max_sum)
