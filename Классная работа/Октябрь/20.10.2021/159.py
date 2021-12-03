import math

filename = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-3.txt"
max_sum = -math.inf
amount = 0
with open(filename, 'r') as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    summ, mult = a + b, a * b
    if summ % 3 == 0 and summ % 6 != 0 and str(mult)[-1] == '8':
        amount += 1
        max_sum = max(max_sum, summ)
print(amount, max_sum)
