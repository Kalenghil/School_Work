f = open(r'C:\Users\Bosnian\Documents\GitHub\School_Work\Материалы\27data\72\27-72a.txt')
n = int(f.readline())
s = 0
k71 = [0]*71
count = 0
for i in range(n):
    x = int(f.readline())
    s+=x
    if s%71==0:
        count += k71[0]+1
    else:
        count += k71[s%71]
    k71[s%71]+=1
print(count)
