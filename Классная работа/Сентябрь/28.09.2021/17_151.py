file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt"
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))
counter = 0
ans = list()
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if (abs(a) % 3 == 0 and abs(a) % 10 == 6) or (abs(b) % 3 == 0 and abs(b) % 10 == 6):
        counter += 1
        ans.extend((a, b))

print(counter, min(ans))
