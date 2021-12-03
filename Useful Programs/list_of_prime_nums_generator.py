def is_prime(num):
	for i in range(2, int(num ** 0.5) + 2):
		if num % i == 0:
			return False
	return True


a = [2]
for j in range(2, int(input()) + 1):
	if is_prime(j):
		a.append(j)
print(a)
