def check(a):
	return (a % 3 == 0) and (a % 5 != 0) and (a % 11 != 0) and (a % 19 != 0)


file_path = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-1.txt'

with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
mean = sum(nums) / len(nums)

for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if (a < mean or b < mean) and (check(a) or check(b)):
		ans.append((a, b, a + b))

print(len(ans), max(ans, key=lambda x: x[2])[2])
