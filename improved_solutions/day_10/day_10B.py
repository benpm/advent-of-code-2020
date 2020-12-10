with open("../../original_solutions/day_10/input_10.txt") as input_file:
    adapters = sorted([0] + [int(line.strip()) for line in input_file])
    nways_to_reach = [1] + [0] * (len(adapters) - 1)
    for i in range(len(adapters)):
        j = i + 1
        while j < len(adapters) and adapters[j] - adapters[i] <= 3:
            nways_to_reach[j] += nways_to_reach[i]
            j += 1
    print(nways_to_reach[-1])