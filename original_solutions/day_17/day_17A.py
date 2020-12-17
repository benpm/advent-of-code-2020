import numpy as np
from copy import deepcopy

with open("input_17.txt") as input_file:
    d = (64, 64, 64)
    a = np.ndarray(d, dtype=np.int)
    a.fill(0)
    y = d[1] // 2
    z = d[2] // 2
    for line in [line.strip() for line in input_file]:
        x = d[0] // 2
        for c in line:
            a[z,y,x] = 1 if c == "#" else 0
            x += 1
        y += 1
    for i in range(6):
        print(i)
        _a = a.copy()
        for x in range(0, d[0]):
            for y in range(0, d[1]):
                for z in range(0, d[2]):
                    n = _a[z-1:z+2,y-1:y+2,x-1:x+2].sum() - _a[z,y,x]
                    # import pdb; pdb.set_trace()
                    if _a[z,y,x] == 1:
                        if not (n == 2 or n == 3):
                            a[z,y,x] = 0
                    else:
                        if n == 3:
                            a[z,y,x] = 1
    print(a.sum())