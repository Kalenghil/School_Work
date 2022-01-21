# -*- coding: utf-8 -*-

from re import findall

file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\Варианты\Вариант 5-2022_ш\24__8lro.txt'
with open(file_name, 'r', encoding='utf-8') as f:
	s = f.readline().strip()

a = findall(r'В+Ь', s)
print(len(max(a, key=len)) - 1)
