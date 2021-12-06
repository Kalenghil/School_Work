file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-243.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

check = max(list(filter(lambda x: x % 127 == 0, nums)))
ans = list()
for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if any(n > check for n in (a, b)) and any('31' in oct(n) for n in (a, b)):
		ans.append(a + b)

print(len(ans), min(ans))
