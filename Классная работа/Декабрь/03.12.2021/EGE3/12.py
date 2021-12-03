s = '1' * 39 + '2' * 14
while '11' in s or '2' in s:
	while '12' in s:
		s = s.replace('12', '11', 1)
	if '11' in s:
		s = s.replace('11', '2', 1)
	elif '2' in s:
		s = s.replace('2', '0', 1)
print(s)
print(s.count('0'))
