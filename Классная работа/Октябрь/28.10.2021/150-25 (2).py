def is_prime(num):
    for i in range(2, int(num ** 0.5) + 2):
        if num % i == 0:
            return False
    return True


f = open('output2.csv', 'w')


# prime_nums = list(filter(is_prime, range(1, 10000)))
# powers_of_two = list(map(lambda x: 2 ** x, range(1, 10)))
ans = list()
for num in range(105_000_000, 115_000_001):
    temp = num
    while temp % 2 == 0:
        temp //= 2
    temp2 = temp ** 0.25
    if int(temp2) == temp2 and is_prime(temp2):
        print(num, temp, file=f, sep=';')
        print(num, temp2, temp, num // temp)
f.close()
