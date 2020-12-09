
with open("input_9.txt") as input_file:
    r = 85848519
    vals = [int(line) for line in input_file]
    for i, v in enumerate(vals):
        s = 0
        j = i
        for vv in vals[i:]:
            s += vv
            if s == r:
                print(min(vals[i:j+1]) + max(vals[i:j+1]))
                exit()
            j += 1