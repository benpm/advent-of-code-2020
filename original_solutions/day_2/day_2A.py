with open("input_2.txt") as f:
    valid = 0
    for line in f:
        if len(line) > 0:
            mincount = int(line.split(" ")[0].split("-")[0])
            maxcount = int(line.split(" ")[0].split("-")[1])
            letter = line.split(" ")[1][0]
            passwd = line.split(" ")[2]
            if mincount <= passwd.count(letter) <= maxcount:
                valid += 1
    print(valid)