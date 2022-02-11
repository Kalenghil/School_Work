s = '8' * 69
while '222' in s or '8888' in s:
    if '222' in s:
        s = s.replace('22', '8', 1)
    else:
        s = s.replace('888', '2', 1)

print(s)