with open("input_8.txt") as input_file:
    acc = 0
    ip = 0
    instrs = [[line.strip(), 0] for line in input_file]
    while True:
        if instrs[ip][1] > 0:
            break
        instr = instrs[ip][0].split(" ")[0]
        val = int(instrs[ip][0].split(" ")[1])
        instrs[ip][1] += 1
        if instr == "acc":
            acc += val
            ip += 1
        elif instr == "jmp":
            ip += val
        elif instr == "nop":
            ip += 1
    print(acc)