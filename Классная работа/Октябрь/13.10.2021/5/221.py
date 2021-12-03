import pprint

a = list()
for i in range(900, 1000):
	temp = sorted(str(i))
	fst = temp[0] + temp[1]
	snd = temp[2] + temp[1]
	if int(snd) - int(fst) == 70:
		a.append(i)
pprint.pprint(list(enumerate(a)))
