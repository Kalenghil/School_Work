s = '5' * 150
while '5555' in s:
	if '5555' in s:
		s = s.replace('5555', '33', 1)
	if '333' in s:
		s = s.replace('333', '5', 1)
print(s)
