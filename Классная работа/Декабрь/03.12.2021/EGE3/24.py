file_path = r'24__7nx5.txt'
with open(file_path, 'r') as f:
	s = f.readline()

counter = 1
max_counter = 0
for i in range(len(s) - 1):
	if s[i] != s[i + 1]:
		counter += 1
	else:
		max_counter = max(max_counter, counter)
		counter = 1

print(max_counter)
