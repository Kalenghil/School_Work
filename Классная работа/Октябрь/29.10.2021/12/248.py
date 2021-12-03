k = 0
ans = 0
for i in range(71, 91):
	s = '1' * i
	while '111' in s:
		s = s.replace('111', '22', 1)
		s = s.replace('222', '11', 1)
	print(s, i, s.count('1'))
	if k < s.count('1'):
		k = s.count('1')
		ans = i
print(k, ans)
