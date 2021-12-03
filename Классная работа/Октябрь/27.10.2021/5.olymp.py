import math

a = 50
two = list(map(lambda x: 2 ** x, range(a, -1, -1)))
three = list(map(lambda x: 3 ** x, range(a, -1, -1)))
five = list(map(lambda x: 5 ** x, range(a, -1, -1)))
inn = 100
ans = -math.inf
for num2 in two:
    for num3 in three:
        for num5 in five:
            temp = num2 * num3 * num5
            if temp <= inn:
                ans = max(ans, temp)

print(ans)
