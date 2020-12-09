
with open("input_9.txt") as input_file:
    pream_size = 25
    pream = []
    for n in [int(line) for line in input_file]:
        if len(pream) <= pream_size:
            pream.append(n)
            continue
        pream.append(n)
        pream.pop(0)
        s = False
        for i, v in enumerate(pream):
            for vv in pream[i:]:
                if v + vv == n:
                    s = True
        if not s:
            print(n)
            break