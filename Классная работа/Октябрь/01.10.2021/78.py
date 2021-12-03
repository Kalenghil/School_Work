from itertools import product

alphabet = "АИОУЭ"
words = list(map(''.join, product(alphabet, repeat=4)))
print(words.index('ИААЭ') + 1)
