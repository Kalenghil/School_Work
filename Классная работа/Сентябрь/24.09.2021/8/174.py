from itertools import product
alphabet = 'КАЛИЙ'
words = list(map(''.join, product(alphabet, repeat=6)))
words = list(filter(lambda x: (x.count('Й') <= 1
    and x[0] != 'Й'
    and x[-1] != 'Й'
    and x.count('ИЙ') == 0
    and x.count('ЙИ') == 0), words))
print(len(words))
