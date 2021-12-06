file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-1.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
mean = sum(nums) / len(nums)
for i in range(len(nums) - 2):
	a, b, c = nums[i:i + 3]
	if any(n < mean for n in (a, b, c)) and any(n % 3 == 0 for n in (a, b, c)):
		ans.append(a + b + c)

print(len(ans), max(ans))
