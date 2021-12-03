file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt"
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))
counter = 0
ans = list()
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if a < b:
        ans.append(abs(a - b))

print(len(ans), min(ans))