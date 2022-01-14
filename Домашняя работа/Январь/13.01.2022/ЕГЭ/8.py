from itertools import product


alphabet = 'АВОРТ'
words = list(map(lambda x: ''.join(x), list(product(alphabet, repeat=4))))
print(words)
print(words.index('ТАРА') + 1)
 