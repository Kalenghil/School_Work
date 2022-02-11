for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                s = int(not x or y or (not z and w))
                if s == 0:
                    print(f'w: {w}; x: {x}; y: {y}; z: {z}; ans: {s}')
