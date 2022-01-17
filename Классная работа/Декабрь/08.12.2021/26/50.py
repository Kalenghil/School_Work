import math

file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-50.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	nums = list(map(int, f.readlines()))

counter = 0
ans = math.inf
nums.sort(reverse=True)
median = nums[amount // 2]
quarter_median = nums[amount // 4]
for i in range(amount - 1):
	for j in range(i + 1, amount):
		mean = (nums[i] + nums[j]) // 2
		if median < mean < quarter_median:
			counter += 1
			ans = min(ans, mean)

print(counter, ans)
