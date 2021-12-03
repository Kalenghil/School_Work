import math


def mult(*args):
    ans = 1
    for num in args:
        ans *= num
    return ans


filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
min_dif = math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    summ = a + b + c
    if (sorted([a, b, c]) == [a, b, c]):
        amount += 1
        min_dif = min(min_dif, max(a, b, c) - min(a, b, c))

print(amount, min_dif)
