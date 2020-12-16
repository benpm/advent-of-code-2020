import re
from collections import defaultdict
from math import prod
with open("input_16.txt") as input_file:
    secs = input_file.read().split("\n\n")
    fields = dict()
    for line in secs[0].split("\n"):
        f = re.match("(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)
        fields[f.group(1)] = ((int(f.group(2)), int(f.group(3))), (int(f.group(4)), int(f.group(5))))
    myticket = [int(s) for s in secs[1].split("\n")[1].split(",")]
    tickets = secs[2].split("\n")[1:]
    #
    valid_tickets = []
    for line in secs[2].split("\n")[1:]:
        if len(line) == 0:
            continue
        ticket = [int(s) for s in line.split(",")]
        valid_ticket = True
        for n in ticket:
            valid_field = False
            for name, f in fields.items():
                if f[0][0] <= n <= f[0][1] or f[1][0] <= n <= f[1][1]:
                    valid_field = True
            if not valid_field:
                valid_ticket = False
                break
        if valid_ticket:
            valid_tickets.append(ticket)
    #
    field_pos = defaultdict(list)
    for i in range(len(fields)):
        for name, c in fields.items():
            for ticket in valid_tickets:
                if not (c[0][0] <= ticket[i] <= c[0][1] or c[1][0] <= ticket[i] <= c[1][1]):
                    break
            else:
                field_pos[name].append(i)
    while sum([(len(f) - 1) for _,f in field_pos.items()]) > 0:
        for _,f in field_pos.items():
            if len(f) == 1:
                for _,h in field_pos.items():
                    if len(h) > 1 and f[0] in h:
                        h.remove(f[0])
    print(prod([myticket[f[0]] for name,f in field_pos.items() if "departure" in name]))
