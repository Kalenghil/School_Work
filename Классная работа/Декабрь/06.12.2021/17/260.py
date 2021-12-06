file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-257.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

ends_with_four = list(filter(lambda x: str(x)[-1] == '4', nums))
check = max(ends_with_four) + min(ends_with_four)
ans = list()
for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if a + b < check:
		ans.append(a + b)

print(len(ans), max(ans))
