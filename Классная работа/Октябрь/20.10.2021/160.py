import math

filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
min_mult = math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    summ, mult = a + b, a * b
    if summ % 7 == 0 and mult > 0:
        amount += 1
        min_mult = min(min_mult, mult)
print(amount, min_mult)
