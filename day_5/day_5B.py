with open("input_5.txt") as f:
    seats = set()
    for l in f:
        l = l.strip()
        low = 0
        high = 127
        for c in l[:7]:
            if c == "F":
                high = (low + high) // 2
            else:
                low = (low + high) // 2
        row = high
        low = 0
        high = 7
        for c in l[7:]:
            if c == "L":
                high = (low + high) // 2
            else:
                low = (low + high) // 2
        col = high
        seat = row * 8 + col
        seats.add(seat)
    for i in range(1, max(seats)):
        if (i not in seats) and (i-1 in seats) and (i+1 in seats):
            print(i)
