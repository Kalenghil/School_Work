from itertools import product

alphabet = 'НРДО'
words = list(map(''.join, product(alphabet, repeat=4)))

print(words.index('ДРОН') + 1)
	