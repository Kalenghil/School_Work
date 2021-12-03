from itertools import product, permutations
alphabet = '0123456789'
ans = list()
number_of_digits = 5
list_of_nums = list(map(''.join, permutations(alphabet[:number_of_digits + 1])))
ans = list(filter(lambda s: len(set(s)) == len(list(s)
                  and s[0] != '0'
                  and int(s) % 5 == 0
                  and all((int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 != 0)
                          or (int(s[i]) % 2 != 0 and int(s[i + 1]) % 2 == 0)
                          for i in range(3)), list_of_nums)))
print(len(ans))
