def f(start, end):
	if start == end:
		return 1
	if start > end:
		return 0
	return f(start + 2, end) + f(start * 2, end)


print(f(2, 40))
