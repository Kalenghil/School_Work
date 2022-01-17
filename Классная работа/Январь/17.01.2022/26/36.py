file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-j8.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	goods = list(map(int, f.readlines()))

goods.sort()
fst = sum(goods[:int(amount * 0.7)]) * 0.7 + sum(goods[int(amount * 0.7):]) * 0.6
snd = sum(goods[:int(amount * 0.5)]) * 0.6 + sum(goods[int(amount * 0.5):]) * 0.65

