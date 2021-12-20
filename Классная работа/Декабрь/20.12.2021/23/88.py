def func(start, end):
	if start == end:
		return 1
	if start > end:
		return 0
	return func(start + 1, end) + func(start + 3, end) + func(start * 2, end)


print(func(1, 4) * func(4, 9) * func(9, 13))
