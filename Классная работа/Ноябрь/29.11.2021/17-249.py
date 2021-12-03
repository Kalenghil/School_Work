file_path = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-243.txt'

with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
max_num = max(list(filter(lambda x: x % 211 == 0, nums)))
for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if (a > max_num or b > max_num) and (str(a).count('1') != 0 or str(b).count('1') != 0):
		ans.append((a, b, a + b))

print(len(ans), min(ans, key=lambda x: x[2]))
