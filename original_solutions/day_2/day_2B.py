with open("input_2.txt") as f:
    valid = 0
    for line in f:
        if len(line) > 0:
            a = int(line.split(" ")[0].split("-")[0]) - 1
            b = int(line.split(" ")[0].split("-")[1]) - 1
            letter = line.split(" ")[1][0]
            passwd = line.split(" ")[2]
            if int(passwd[a] == letter) ^ int(passwd[b] == letter):
                valid += 1
    print(valid)