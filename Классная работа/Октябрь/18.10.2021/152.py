from math import inf

file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt"
amount = 0
min_sum = -inf
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        if ((a % 9 == 0 and oct(a)[-1] == '3' and b % 9 != 0)
                or (b % 9 == 0 and oct(b)[-1] == '3' and a % 9 != 0)):
            amount += 1
            min_sum = max(min_sum, a, b)
print(amount, min_sum)
