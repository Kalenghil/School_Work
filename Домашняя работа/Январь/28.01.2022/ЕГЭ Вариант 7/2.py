for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = int(not x or y or (not z and w))
                if a == 0:
                    print(f'x:{x}, y:{y}, z:{z}, w:{w}: a{a}')

