file_path = r'test_file_6.txt'
ans = list()
with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))


counter = 0
for i in range(len(nums) - 1):
	a, b = nums[i], nums[i + 1]
	if a != b:
		counter += 1
	elif counter != 0:
		ans.append(counter + 1)
		counter = 0
ans.append(counter + 1)

max_len = max(ans)
print(max_len, len(list(filter(lambda x: x == max_len, ans))))