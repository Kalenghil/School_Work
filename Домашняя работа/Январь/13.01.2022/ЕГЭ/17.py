file_name = r'C:\Users\Bosnian\Documents\GitHub\School_Work\Материалы\Варианты\Вариант 102-2022с\17.txt'
with open(file_name, 'r') as f:
    nums = list(map(int, f.readlines()))


ans = list()
for i in range(len(nums) - 1):
    a, b = nums[i:i + 2]
    if (a % 5 == 0 or b % 5 == 0) and ((a + b) % 7 == 0):
        ans.append(a + b)

print(len(ans), max(ans))
