
with open("input_10.txt") as input_file:
    ads = [int(line.strip()) for line in input_file]
    ads.sort()
    ads.append(ads[-1] + 3)
    b = 0
    d = [0, 0, 0]
    for a in ads:
        d[a - b - 1] += 1
        b = a
    print(d[0] * d[2])