file_path = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-243.txt'

with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
max_num = max(filter(lambda x: x % 71 == 0, nums))
for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if (a < max_num and b < max_num) and (a % 13 == 0 or b % 13 == 0):
		ans.append((a, b, a + b))

print(len(ans), min(ans, key=lambda x: x[2])[2])
