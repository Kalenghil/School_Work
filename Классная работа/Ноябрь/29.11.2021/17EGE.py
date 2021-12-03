from pprint import pprint

file_path = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17.txt'

with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))

max_num = max(list(filter(lambda x: x % 3 == 0, nums)))

ans = list()
counter = 0
for i in range(len(nums) - 1):
	a, b = nums[i: i + 2]
	if (a % 3 == 0 or b % 3 == 0) and a + b < max_num:
		counter += 1
		ans.append((a, b))

pprint(ans)
print(counter)
