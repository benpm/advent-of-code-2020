import re
with open("input_12.txt") as input_file:
    wN = 1
    wE = 10
    N = 0
    E = 0
    dmap = {"N":[1,0],"W":[0,-1],"S":[-1,0],"E":[0,1]}
    ds = ["N","E","S","W"]
    d = 1
    for line in [line.strip() for line in input_file]:
        g = re.search(r"([A-Z]+)(\d+)", line).group(1)
        n = int(re.search(r"([A-Z]+)(\d+)", line).group(2))
        if g == "F":
            N += wN * n
            E += wE * n
        elif g == "L":
            for i in range(n // 90):
                t = wE
                wE = -wN
                wN = t
        elif g == "R":
            for i in range(n // 90):
                t = wE
                wE = wN
                wN = -t
        else:
            wN += dmap[g][0] * n
            wE += dmap[g][1] * n
        # print(wE, wN, E, N)
    print(N, E, abs(N) + abs(E))
