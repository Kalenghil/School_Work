file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-48.txt'
# file_name = r'test_47.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	nums = list(map(int, f.readlines()))

diffs = dict()
means = list()
for i in range(len(nums)):
	for j in range(i + 1, len(nums)):
		a, b = nums[i], nums[j]
		if (a + b) % 2 == 0:
			mean = (a + b) // 2
			diffs[mean + 5] = mean
			diffs[mean - 5] = mean

ans = list()
for num in nums:
	if num in diffs:
		ans.append(diffs[num])
print(ans)
