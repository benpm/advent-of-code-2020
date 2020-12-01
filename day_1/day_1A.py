with open("input_1A.txt") as f:
    a = [int(l) for l in f]
    for i in a:
        for j in a:
            for k in a:
                if i + j + k == 2020:
                    print(i * j * k)
                    exit()