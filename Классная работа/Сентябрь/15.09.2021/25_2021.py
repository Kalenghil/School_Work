def divisors(num):
    divisors = list()
    for i in range(2, int(num**0.5) + 2):
        if num % i == 0:
            divisors.append(i)
    return divisors, len(divisors)


for i in range(174_457, 174_506):
    tmp, len_tmp = divisors(i)
    if (len_tmp == 1 and i // tmp[0] != tmp[0]):
        print(tmp[0], i // tmp[0])
    elif (len_tmp == 2 and tmp[0] * tmp[1] == i):
        print(tmp[0], tmp[1])
