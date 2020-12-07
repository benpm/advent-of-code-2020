from os import PathLike
import re

def func(can_contain, k, l):
    for i in can_contain[k]:
        if "shiny gold" in i[1]:
            l.add(k)
    for kk in can_contain[k]:
        func(can_contain, kk[1], l)
        if kk[1] in l:
            l.add(k)

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
    l = set()
    for k in can_contain.keys():
        func(can_contain, k, l)
    print(len(l))