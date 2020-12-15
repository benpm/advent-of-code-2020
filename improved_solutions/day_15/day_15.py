with open("../../original_solutions/day_15/input_15.txt") as input_file:
    last_spoken = dict()
    first_spoken = [int(x) for x in input_file.readline().split(",")]
    spoken = first_spoken[0]
    for i in range(0, 2020):
        prev = spoken
        if i < len(first_spoken):
            spoken = first_spoken[i]
        elif spoken not in last_spoken.keys():
            spoken = 0
        else:
            spoken = i - 1 - last_spoken[spoken]
        last_spoken[prev] = i - 1
    print(spoken)