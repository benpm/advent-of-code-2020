import numpy as np
import copy

def clamp(i, mi, ma):
    return max(min(i, ma), mi)

with open("input_11.txt") as input_file:
    a = [[c for c in line.strip()] for line in input_file]
    rows = len(a)
    cols = len(a[0])
    print(rows, cols)
    schange = True
    occupied = 0
    steps = 0
    while schange:
        schange = False
        occupied = 0
        aa = copy.deepcopy(a)
        for r in range(rows):
            for c in range(cols):
                adj = []
                for rr in range(max(r-1, 0), min(r+2, rows)):
                    for cc in range(max(c-1, 0), min(c+2, cols)):
                        if rr != r or cc != c:
                            adj.append(aa[rr][cc])
                if aa[r][c] == "L":
                    if adj.count("#") == 0:
                        a[r][c] = "#"
                        schange = True
                elif aa[r][c] == "#":
                    occupied += 1
                    if adj.count("#") >= 4:
                        a[r][c] = "L"
                        schange = True
        steps += 1
    print(occupied)
