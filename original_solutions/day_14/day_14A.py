from collections import defaultdict
import enum
import re

with open("input_14.txt") as input_file:
    mem = defaultdict(int)
    for inp in [f for f in input_file.read().split("mask = ") if f]:
        lines = [s.strip() for s in inp.split("\n") if s]
        mask = lines[0]
        print(mask)
        for M in lines[1:]:
            addr = int(re.match(r"mem\[(\d+)\] = (\d+)", M).group(1))
            val = bin(int(re.match(r"mem\[(\d+)\] = (\d+)", M).group(2)))[2:]
            out = 0
            for i, m in enumerate(mask):
                v = 0
                if i >= len(mask) - len(val):
                    # if addr == 7:
                    #     import pdb; pdb.set_trace()
                    v = int(val[len(val) - (len(mask) - i)])
                if m != "X":
                    v = int(m)
                out |= v << (len(mask) - i - 1)
            mem[addr] = out
    s = 0
    for m in mem.values():
        s += m
    print(s)