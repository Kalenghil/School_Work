file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-1.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = list()
mean = sum(nums) / len(nums)
for i in range(len(nums) - 2):
	a, b, c = nums[i:i + 3]
	if any(n < mean for n in (a, b, c)) and (((str(a)[-1] == '4') + (str(b)[-1] == '4') + (str(c)[-1] == '4')) > 1):
		ans.append(a + b + c)

print(len(ans), max(ans))
