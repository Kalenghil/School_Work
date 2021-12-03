with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\КЕГЭ_демо 2022_проект\Доп. файлы\Задание 26\26.txt", 'r') as f:
    memory_size, files_amount = list(map(int, f.readline().split()))
    files = sorted(list(map(int, f.readlines())))
    f.close()

max_file = 0
summ = 0

for i in range(files_amount):
    if summ + files[i] > memory_size:
        index = i
        break
    max_file = files[i]
    summ += max_file

for i in range(index + 1, files_amount):
    if summ - max_file + files[i] < memory_size:
        summ = summ - max_file + files[i]
        max_file = files[i]
    else:
        break
print(index, max_file)
