def is_prime(num):
    for i in range(2, int(num ** 0.5) + 2):
        if num % i == 0:
            return False
    return True


prime_nums = list(filter(is_prime, range(1, 100000)))
nums = list(map(lambda x: (x, x ** 3, x ** 4), prime_nums))
for num in nums:
    if 525784203 <= num[2] <= 728943762:
        print(num)
