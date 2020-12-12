import re
with open("input_12.txt") as input_file:
    N = 0
    E = 0
    dmap = {"N":[1,0],"W":[0,-1],"S":[-1,0],"E":[0,1]}
    ds = ["N","E","S","W"]
    d = 1
    for line in [line.strip() for line in input_file]:
        g = re.search(r"([A-Z]+)(\d+)", line).group(1)
        n = int(re.search(r"([A-Z]+)(\d+)", line).group(2))
        if g == "F":
            N += dmap[ds[d]][0] * n
            E += dmap[ds[d]][1] * n
        elif g == "L":
            d = (d - (n // 90) ) % 4
        elif g == "R":
            d = (d + (n // 90) ) % 4
        else:
            N += dmap[g][0] * n
            E += dmap[g][1] * n
    print(N, E, abs(N) + abs(E))
