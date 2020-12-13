with open("../../original_solutions/input_13.txt") as input_file:
    _b = input_file.readlines()[1]
    bus_times = [(i, -1 if x == "x" else int(x)) for i,x in enumerate(_b.split(","))]
    i = 0
    while True:
        z = 1
        for k, bus in bus_times:
            if bus != -1:
                if i % bus != (bus - k) % bus:
                    break
                else:
                    z *= bus
        else:
            print(i)
            break
        i += z