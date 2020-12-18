import re

def groups(l):
    n = 0
    op = ""
    i = 0
    while i < len(l):
        if l[i] == "(":
            o = groups(l[i+1:])
            if op == "*":
                n *= o[0]
            elif op == "+":
                n += o[0]
            elif op == "":
                n = o[0]
            i += o[1]
        elif l[i] == ")":
            return (n, i + 1)
        else:
            try:
                x = int(l[i])
                if op:
                    if op == "*":
                        n *= x
                    elif op == "+":
                        n += x
                else:
                    n = x
            except:
                op = l[i]
        i += 1
    return (n, len(l) - 1)

with open("input_18.txt") as input_file:
    s = 0
    for line in [line.strip() for line in input_file.readlines()]:
        l = re.findall(r"(\d+|\*|\+|\(|\)) ?", line)
        s += groups(l)[0]
    print(s)
