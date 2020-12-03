with open("input_3.txt") as f:
    i = 0
    trees = 0
    lines = [line for line in f]
    for line in lines[1:]:
        i = (i + 3) % (len(line) - 1)
        if line[i] == "#":
            trees += 1
    print(trees)