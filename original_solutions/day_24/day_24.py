from collections import defaultdict
import re
from copy import deepcopy
import tqdm
with open("input_24.txt") as input_file:
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
    for i in tqdm.trange(100):
        gg = deepcopy(g)
        for k, v in gg.items():
            for pp in [(2, 0), (-2, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
                p = (k[0] + pp[0], k[1] + pp[1])
                if p not in g.keys():
                    g[p] = True
        gg = deepcopy(g)
        for k, v in gg.items():
            n = 0
            for pp in [(2, 0), (-2, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
                p = (k[0] + pp[0], k[1] + pp[1])
                if p in gg.keys() and gg[p] == False:
                    n += 1
            if v == False and (n == 0 or n > 2):
                g[k] = True
            if v == True and (n == 2):
                g[k] = False
    s = 0
    for k, v in g.items():
        if not v:
            s += 1
    print(s)
