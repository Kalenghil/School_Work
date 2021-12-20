def func(start, end):
	if start == end:
		return 1
	if start > end or start == 6:
		return 0
	return func(start + 2, end) + func(start * 3, end)


print(func(1, 25) * func(25, 63))
