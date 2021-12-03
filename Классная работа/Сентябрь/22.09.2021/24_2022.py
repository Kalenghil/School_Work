import re

with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\КЕГЭ_демо 2022_проект\Доп. файлы\Задание 24\24.txt", 'r') as f:
    s = re.split(r'P+P', f.readline())
    f.close()


ans = max(s, key=lambda x: len(x))
print(ans)
print(len(ans) + 1 if ans == s[0] or ans == s[-1] else len(ans) + 2)
