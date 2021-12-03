file_name = r'17__7nxc.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

ans = []
for i in range(len(nums) - 1):
	a, b = nums[i:i + 2]
	if (a > 1000 and (a % 6 == 0 or a % 7 == 0)) or (b > 1000 and (b % 6 == 0 and b % 7 == 0)):
		ans.append((a, b, a * b))

print(len(ans), max(ans, key=lambda x: x[2]))
