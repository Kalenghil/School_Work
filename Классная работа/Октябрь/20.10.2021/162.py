import math

filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
min_av = math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    summ, mult = a + b, a * b
    if mult % 2 != 0 and (summ / 2) % 7 == 0:
        amount += 1
        min_av = min(min_av, summ / 2)
print(amount, min_av)
