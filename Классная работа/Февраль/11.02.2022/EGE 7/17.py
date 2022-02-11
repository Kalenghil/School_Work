file_name = r'D:\WORK\11 класс\Макиевский Кирилл\School_Work\Материалы\Варианты\Вариант 7-2022_ш\17__9p3p.txt'
with open(file_name, 'r') as f:
    amount = int(f.readline())
    nums = list(map(int, f.readlines()))


ans = list()
for i in range(amount - 1):
    a, b = nums[i: i + 2]
    if a * b % 153 == 0:
        ans.append(int(a + b / 2))

print(len(ans), min(ans))
