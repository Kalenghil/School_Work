from itertools import product, permutations
alphabet = 'САКУРА'
words = list(map(''.join, product(alphabet, repeat=5)))
words = list(set(filter(lambda x:
                    x.count('А') <= 1
                    and x.count('У') <= 1, words)))
print(len(words))
