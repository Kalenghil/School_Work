import math
from pprint import pprint

file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\45\27-45b.txt"
sum1, sum2, sum3 = 0, 0, 0
flag = False
difA = ((math.inf, 0), (math.inf, 0))
difB = ((math.inf, 0), (math.inf, 0))
with open(file_path, 'r') as f:
    amount = int(f.readline())
    for i in range(amount):
        line = f.readline()
        a, b, c = sorted(list(map(int, line.split())), reverse=True)
        sum1 += a
        sum2 += b
        sum3 += c
        if (a - b) % 2 == 1:
            flag = True
        if (a - c) % 2 == 1:
            temp = a - c
            if (b - c) % 2 == 1:
                temp = b - c
            if difA[0][0] > temp:
                difA = ((temp, i - 1), difA[0])
            elif difA[0][1] > temp:
                difA = (difA[0], (temp, i - 1))
        if (b - c) % 2 == 1:
            temp = b - c
            if difB[0][0] > temp:
                difB = ((temp, i - 1), difB[0])
            elif difB[1][0] > temp:
                difB = (difB[0], (temp, i - 1))


print(sum1, sum2, sum3)
print(flag, difA, difB, sep='\n')

if (sum1 % 2 == 1) and (sum2 % 2 == 1):
    print(sum3)
elif (sum1 % 2 == 0) and (sum2 % 2 == 0):
    if flag:
        print(sum3)
    else:
        if difA[0][1] != difB[0][1]:
            print(sum3 + difA[0][0] + difB[0][0])
        else:
            print(sum3 + min(
                difA[0][0] + difB[1][0],
                difA[1][0] + difB[0][0]))
elif (sum1 % 2 == 0):
    print(sum3 + difA[0][0])
elif (sum2 % 2 == 0):
    print(sum3 + difB[0][0])
