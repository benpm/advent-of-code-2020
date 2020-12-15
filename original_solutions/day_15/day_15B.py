from collections import defaultdict

with open("input_15.txt") as input_file:
    last_spoken = defaultdict(int)
    k = [int(x) for x in input_file.readline().split(",")]
    v = set()
    spoken = 0
    for i in range(len(k)):
        spoken = k[i]
        last_spoken[spoken] = i
        if i < len(k) - 1:
            v.add(spoken)
    for i in range(len(k), 30000000):
        l = spoken
        if spoken not in v:
            v.add(spoken)
            spoken = 0
        else:
            spoken = i - 1 - last_spoken[spoken]
        last_spoken[l] = i - 1
    print(spoken)
        