with open("input_8.txt") as input_file:
    instrs = [[line.strip(), 0] for line in input_file]
    c = 0
    for c in range(len(instrs)):
        acc = 0
        ip = 0
        for instr in instrs:
            instr[1] = 0
        while ip < len(instrs):
            if instrs[ip][1] > 0:
                break
            instr = instrs[ip][0].split(" ")[0]
            val = int(instrs[ip][0].split(" ")[1])
            instrs[ip][1] += 1
            if ip == c:
                if instr == "jmp":
                    instr = "nop"
                elif instr == "nop":
                    instr = "jmp"
            if instr == "acc":
                acc += val
                ip += 1
            elif instr == "jmp":
                ip += val
            elif instr == "nop":
                ip += 1
        else:
            print(acc)