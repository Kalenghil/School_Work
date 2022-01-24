file_name = r''
sums = list()
ams = list()
with open(file_name, 'r') as f:
	amount, k = list(map(int, f.readline()))
	counter = 0
	for _ in range(amount):
		num = int(f.readline())
		nums.append(num)
		if num < 0 and str(num)[-1] == '3':
			counter += 1
		ams.append(counter)