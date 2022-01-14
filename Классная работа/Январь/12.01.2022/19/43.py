turns = list()


def f(n, player=0):
	if n > 45:
		return n, player
	turns.append(f(n + 2, player + 1))
	turns.append(f(n * 3, player + 1))


for i in range(1, 45):
	f(i)
	turns = list(filter(lambda x: x is not None, turns))
	turns.sort(key=lambda x: x[1])
	print(i, turns[:20])
