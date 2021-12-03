from math import inf

file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt"
amount = 0
min_sum = inf
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        if b > a:
            amount += 1
            min_sum = min(min_sum, abs(a - b))
print(amount, min_sum)
