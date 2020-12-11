import numpy as np
import copy

with open("input_11.txt") as input_file:
    a = [[c for c in line.strip()] for line in input_file]
    rows = len(a)
    cols = len(a[0])
    print(rows, cols)
    schange = True
    occupied = 0
    steps = 0
    dirs = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
    while schange:
        schange = False
        occupied = 0
        aa = copy.deepcopy(a)
        for r in range(rows):
            for c in range(cols):
                adj = []
                ddirs = [1] * 8
                i = 0
                while sum(ddirs) > 0:
                    i += 1
                    for j in range(len(dirs)):
                        if ddirs[j] == 1:
                            rr = r + dirs[j][0] * i
                            cc = c + dirs[j][1] * i
                            if 0 <= rr < rows and 0 <= cc < cols:
                                v = aa[rr][cc]
                                if v != ".":
                                    adj.append(v)
                                    ddirs[j] = 0
                            else:
                                ddirs[j] = 0
                if aa[r][c] == "L":
                    if adj.count("#") == 0:
                        a[r][c] = "#"
                        schange = True
                elif aa[r][c] == "#":
                    occupied += 1
                    if adj.count("#") >= 5:
                        a[r][c] = "L"
                        schange = True
        steps += 1
        print(steps)
    print(occupied)
