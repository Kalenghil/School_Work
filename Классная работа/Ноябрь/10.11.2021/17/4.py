file_path = r'test_file_1.txt'
ans = list()
with open(file_path, 'r') as f:
	nums = list(map(int, f.readlines()))


counter = 0
for num in nums:
	if num % 3 != 0:
		counter += 1
	elif counter != 0:
		ans.append(counter)
		counter = 0
ans.append(counter)

max_len = max(ans)
print(max_len, len(list(filter(lambda x: x == max_len, ans))))