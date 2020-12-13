
with open("input_13.txt") as input_file:
    t = int(input_file.readline())
    _bt = input_file.readline()
    bt = [int(x) for x in _bt.split(",") if x != "x"]
    bts = []
    mb = 9999999999999999999
    mi = 0
    for bus in bt:
        i = 0
        while i * bus < t:
            i += 1
        if i * bus < mb:
            mi = bus
        mb = min(mb, i * bus)
    print(mi * (mb-t))