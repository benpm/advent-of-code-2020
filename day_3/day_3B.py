def f(r, d):
    with open("input_3.txt") as f:
        i = 0
        trees = 0
        lines = [line for line in f]
        print(len(lines))
        for x in range(d, len(lines), d):
            line = lines[x]
            i = (i + r) % (len(line) - 1)
            if line[i] == "#":
                trees += 1
        return trees

print(f(1, 1),f(3, 1),f(5, 1),f(7, 1),f(1, 2))
print(f(1, 1) * f(3, 1) * f(5, 1) * f(7, 1) * f(1, 2))