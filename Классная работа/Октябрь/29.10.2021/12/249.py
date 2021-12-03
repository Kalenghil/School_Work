k = 999999
ans = 0
for i in range(101, 131):
	s = '1' * i
	while '1111' in s:
		s = s.replace('1111', '2', 1)
		s = s.replace('22', '11', 1)
	print(s, i, s.count('1'))
	if k > s.count('1'):
		k = s.count('1')
		ans = i
print(k, ans)
