with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\КЕГЭ_демо 2021\Файлы\Задание 24\24.txt", 'r') as f:
    s = f.readline()
    f.close()

max_length = 0
counter = 1
for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    if a != b:
        counter += 1
    else:
        max_length = max(max_length, counter)
        counter = 1

print(max_length)
