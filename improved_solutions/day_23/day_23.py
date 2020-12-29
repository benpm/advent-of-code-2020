from tqdm import tqdm

def play(cups, turns):
    maxcup = max(cups)
    curr = list(cups)[0]
    for i in tqdm(range(turns)):
        removed = (cups[curr], cups[cups[curr]], cups[cups[cups[curr]]])
        cups[curr] = cups[removed[-1]]
        dest = curr - 1
        while dest <= 0 or dest in removed:
            dest -= 1
            if dest <= 0:
                dest = maxcup
        cups[dest], cups[removed[-1]] = removed[0], cups[dest]
        curr = cups[curr]

with open("../../original_solutions/day_23/input_23.txt") as input_file:
    cup_list = [int(i) for i in input_file.read().strip()]

    cups = {cup_list[i]:cup_list[(i+1) % len(cup_list)] for i in range(len(cup_list))}
    play(cups, 100)
    j = cups[1]
    l = []
    while j != 1:
        l.append(str(j))
        j = cups[j]
    print("part A:", "".join(l))

    cup_list += list(range(max(cup_list)+1, 1_000_000+1))
    cups = {cup_list[i]:cup_list[(i+1) % len(cup_list)] for i in range(len(cup_list))}
    play(cups, 10_000_000)
    print("part B:", cups[1] * cups[cups[1]])
