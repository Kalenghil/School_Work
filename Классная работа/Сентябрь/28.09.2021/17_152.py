file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt"
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))
counter = 0
ans = list()
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if ((abs(a) % 9 == 0 and oct(b)[-1] == '3' and abs(b) % 9 != 0)
            or (abs(b) % 9 == 0 and oct(a)[-1] == '3' and abs(a % 9 != 0))):
        counter += 1
        ans.extend((a, b))

print(counter, max(ans))
