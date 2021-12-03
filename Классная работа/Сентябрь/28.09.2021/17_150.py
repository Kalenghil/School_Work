file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt"
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))
ans = list()
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if (abs(a) % 7 == 0 and abs(b) % 17 != 0) or (abs(b) % 7 == 0 and abs(a) % 17 != 0):
        ans.append(a + b)

print(len(ans), min(ans))
