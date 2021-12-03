def f(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	return f(n - 1) + g(n - 2)


def g(n):
	if n == 1:
		return 2
	elif n == 2:
		return 3
	elif n == 3:
		return 4
	return g(n - 2) + g(n - 3)


print(f(7) + g(5))
