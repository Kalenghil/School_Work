num = 60
s = ''
while s != '221':
	num += 1
	s = '1' * num
	while '111' in s:
		s = s.replace('111', '2', 1)
		s = s.replace('222', '1', 1)
print(num)
