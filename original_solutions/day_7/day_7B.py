import re

def func(can_contain, k):
    i = 1
    for c in can_contain[k]:
        i += int(c[0]) * func(can_contain, c[1])
    return i

with open("input_7.txt") as f:
    can_contain = {}
    for l in f:
        l = l.strip()
        container = re.search(r"(\w+ \w+) bags", l.split("contain")[0]).group(1)
        if "contain no other bags" in l:
            can_contain[container] = []
        else:
            if container not in can_contain.keys():
                can_contain[container] = []
            for c in l.split("contain")[1].split(", "):
                s = re.search(r"(\d+) (\w+ \w+) bag", c)
                can_contain[container].append((s.group(1), s.group(2)))
    print(func(can_contain, "shiny gold") - 1)