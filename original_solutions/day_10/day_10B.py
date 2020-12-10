from collections import defaultdict

adapters = []
goes_to = defaultdict(lambda: [0, set()])

def f(i):
    if i >= len(adapters):
        return
    j = adapters[i]
    for out in goes_to[j][1]:
        goes_to[out][0] += goes_to[j][0]
    f(i + 1)

with open("input_10.txt") as input_file:
    adapters = [int(line.strip()) for line in input_file]
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    # populate sets of goes_to
    for i in range(len(adapters)):
        j = i + 1
        while j < len(adapters) and adapters[j] - adapters[i] <= 3:
            goes_to[adapters[i]][1].add(adapters[j])
            j += 1
    # one way to get to 0
    goes_to[0][0] = 1
    f(0)
    print(list(goes_to.values())[-1][0])