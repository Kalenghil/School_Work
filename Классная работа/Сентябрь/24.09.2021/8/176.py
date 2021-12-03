from itertools import product
alphabet = 'СЧИТАЙ'
words = list(map(''.join, product(alphabet, repeat=4)))
words = list(filter(lambda x: x.count('А') <= 1, words))
print(len(words))
