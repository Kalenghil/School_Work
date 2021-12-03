def summ(a):
    return (a * (a - 1)) // 2


# with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\14\27-14a.txt", 'r') as f_27a:
#     _, nums_a = f_27a.readline(), list(map(int, f_27a.readlines()))
#     f_27a.close()


with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\14\27-14b.txt", 'r') as f_27b:
    _, nums_b = f_27b.readline(), list(map(int, f_27b.readlines()))
    f_27b.close()


nums = nums_b
remainders = [0] * 12
answ = 0
for num in nums:
    print(num)
    remainders[num % 12] += 1
for i in range(1, 6):
    answ += (remainders[i] * remainders[12 - i])
answ += summ(remainders[0])
answ += summ(remainders[6])
print(answ)
