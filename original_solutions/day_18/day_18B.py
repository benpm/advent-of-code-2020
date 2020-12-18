import re
from math import prod

def groups(l):
    v = []
    i = 0
    while i < len(l):
        if l[i] == "(":
            o = groups(l[i+1:])
            v.append(o[0])
            i += o[1]
        elif l[i] == ")":
            return (v, i + 1)
        else:
            try:
                v.append(int(l[i]))
            except:
                v += l[i]
        i += 1
    return (v, len(l) - 1)

def calc(g):
    n = 0
    gg = []
    op = ""
    # import pdb; pdb.set_trace()
    for c in g:
        if type(c) == list:
            if op == "+":
                n += calc(c)
            else:
                n = calc(c)
        elif type(c) == int:
            if op == "+":
                n += c
            else:
                n = c
        elif c == "*":
            gg.append(n)
            n = 0
            op = ""
        else:
            op = c
    gg.append(n)
    return prod(gg)

with open("input_18.txt") as input_file:
    s = 0
    for line in [line.strip() for line in input_file.readlines()]:
        s += calc(groups(re.findall(r"(\d+|\*|\+|\(|\)) ?", line))[0])
    print(s)

