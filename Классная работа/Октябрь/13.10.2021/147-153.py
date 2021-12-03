a = 5 * 36**7 + 6**10 - 36
p = 3
s = ''
while a:
	s = str(a % p) + s
	a = a // p
print(s, s.count('2'))