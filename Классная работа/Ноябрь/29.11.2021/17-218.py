file_path = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-4.txt'

with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
mean = sum(nums) / len(nums)

for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if (a < mean and b < mean) and (str(a)[-2:] == '19' or str(b)[-2:] == '19'):
		ans.append((a, b, a + b))

print(len(ans), max(ans, key=lambda x: x[2])[2])
