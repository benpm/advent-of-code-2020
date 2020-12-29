from collections import defaultdict
import re
from copy import deepcopy
import tqdm
with open("../../original_solutions/day_24/input_24.txt") as input_file:
    g = defaultdict(lambda: True)
    for line in [line.strip() for line in input_file]:
        dirs = re.findall(r"e|se|sw|w|nw|ne", line)
        p = [0, 0]
        for d in dirs: # nw w sw e e
            if d == "e":
                p[0] += 2
            elif d == "w":
                p[0] -= 2
            elif d == "sw":
                p[1] += 1
                p[0] -= 1
            elif d == "nw":
                p[1] -= 1
                p[0] -= 1
            elif d == "se":
                p[1] += 1
                p[0] += 1
            elif d == "ne":
                p[1] -= 1
                p[0] += 1
        g[tuple(p)] = not g[tuple(p)]
    s = 0
    for k, v in g.items():
        if not v:
            s += 1
    print(s)
    A = g
    B = defaultdict(lambda: True)
    for i in tqdm.trange(100):
        A, B = B, A
        for k, v in A.items():
            for pp in [(2, 0), (-2, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
                p = (k[0] + pp[0], k[1] + pp[1])
                if p not in A.keys():
                    B[p] = True
        for k, v in A.items():
            n = 0
            for pp in [(2, 0), (-2, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
                p = (k[0] + pp[0], k[1] + pp[1])
                if p in A.keys() and A[p] == False:
                    n += 1
            if v == False and (n == 0 or n > 2):
                B[k] = True
            if v == True and (n == 2):
                B[k] = False
    s = 0
    for k, v in B.items():
        if not v:
            s += 1
    print(s)
