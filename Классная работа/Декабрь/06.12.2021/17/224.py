file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-4.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
mean = sum(nums) / len(nums)
for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if (a < mean or b < mean) and ('5' not in str(a) or '5' not in str(b)):
		ans.append(a + b)

print(len(ans), min(ans))
