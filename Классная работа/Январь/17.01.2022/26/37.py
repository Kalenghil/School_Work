file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-k6.txt'
with open(file_name, 'r') as f:
		n, amount = list(map(int, f.readline().split()))
		bags = list(map(lambda x: tuple(map(int, x.split())), f.readlines()))

our_bags = sorted(bags, key=lambda x: (x[1] // x[0], -x[0]))[:amount]
print(our_bags)
print(sum(list(zip(*our_bags))[0]), max(our_bags, key=lambda x: x[0])[0])
