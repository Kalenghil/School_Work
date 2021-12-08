file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-47.txt'
# file_name = r'test_47.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	nums = list(map(int, f.readlines()))

step = 100
ranges = list(range(step, amount, step))
nums.sort()
limits = [(nums[ranges[i] - 1], nums[ranges[i]]) for i in range(len(ranges))]
means = list()
for i in range(len(nums)):
	for j in range(i + 1, len(nums)):
		a, b = nums[i], nums[j]
		means.append((a + b) / 2)
ans = list()
for mean in means:
	for i in range(len(limits)):
		if limits[i][0] < mean <= limits[i][1]:
			ans.append(i)
print(len(ans), ranges[max(ans)])
