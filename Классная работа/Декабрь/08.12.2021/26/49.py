file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-49.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	nums = list(map(int, f.readlines()))

counter = 0
ans = 0
median = sorted(nums)[amount // 2 - 1]
for i in range(amount - 1):
	for j in range(i + 1, amount):
		mean = (nums[i] + nums[j]) // 2
		if mean < median:
			counter += 1
			ans = max(ans, mean)

print(counter, ans)
