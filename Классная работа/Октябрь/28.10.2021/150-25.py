from test import powers_of_two, prime_nums


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 2):
        if num % i == 0:
            return False
    return True


f = open('output2.csv', 'w')


# prime_nums = list(filter(is_prime, range(1, 10000)))
# powers_of_two = list(map(lambda x: 2 ** x, range(1, 10)))
ans = list()
for prime in prime_nums:
    for power in powers_of_two:
        temp = prime ** 4 * power
        if 105_000_000 <= temp <= 115_000_000:
            if temp not in ans:
                print(temp, prime ** 4, power, sep=';', file=f)
                ans.append(temp)
                print(temp)
f.close()
