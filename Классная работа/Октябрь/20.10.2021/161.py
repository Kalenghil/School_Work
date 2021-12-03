import math

filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
max_av = -math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    summ, mult = a + b, a * b
    if summ % 2 == 0 and str(summ) != '6':
        amount += 1
        max_av = max(max_av, summ / 2)
print(amount, max_av)
