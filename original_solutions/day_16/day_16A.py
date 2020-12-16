import re
with open("input_16.txt") as input_file:
    secs = input_file.read().split("\n\n")
    fields = dict()
    for line in secs[0].split("\n"):
        f = re.match("(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)
        fields[f.group(1)] = ((int(f.group(2)), int(f.group(3))), (int(f.group(4)), int(f.group(5))))
    myticket = [int(s) for s in secs[1].split("\n")[1].split(",")]
    err = 0
    valid_tickets = []
    for line in secs[2].split("\n")[1:]:
        if len(line) == 0:
            continue
        ticket = [int(s) for s in line.split(",")]
        valid_ticket = True
        for n in ticket:
            valid = False
            for name, f in fields.items():
                if f[0][0] <= n <= f[0][1] or f[1][0] <= n <= f[1][1]:
                    valid = True
            if not valid:
                valid_ticket = False
                err += n
        if valid_ticket:
            valid_tickets.append(ticket)
    print(err, len(valid_tickets))