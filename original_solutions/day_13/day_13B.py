
with open("input_13.txt") as input_file:
    input_file.readline()
    _bustimes = input_file.readline()
    bustimes = [(i, -1 if x == "x" else int(x)) for i,x in enumerate(_bustimes.split(","))]
    i = 0
    while i >= 0:
        z = 1
        for k, bus in bustimes:
            if bus != -1:
                if i % bus != (bus - k) % bus:
                    break
                else:
                    z *= bus
        else:
            break
        i += z
    print(i)