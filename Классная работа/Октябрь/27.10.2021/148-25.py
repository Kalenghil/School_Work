def is_prime(num):
    for i in range(2, int(num ** 0.5) + 2):
        if num % i == 0:
            return False
    return True


f = open('output.csv', 'w')

prime_nums = list(filter(is_prime, range(1, 10000)))
ans = list()
for fst in prime_nums:
    for snd in prime_nums:
        temp = fst * snd * 2
        if 113_000_000 <= temp <= 114_000_000 and fst == snd:
            if temp not in ans:
                print(temp, temp // max(fst, snd), sep=';', file=f)
                ans.append(temp)
                print(temp)
f.close()
