from collections import defaultdict
import enum
import re

with open("input_14.txt") as input_file:
    mem = defaultdict(int)
    for inp in [f for f in input_file.read().split("mask = ") if f]:
        lines = [s.strip() for s in inp.split("\n") if s]
        mask = lines[0]
        for M in lines[1:]:
            orig_addr = bin(int(re.match(r"mem\[(\d+)\] = (\d+)", M).group(1)))[2:]
            val = int(re.match(r"mem\[(\d+)\] = (\d+)", M).group(2))
            out_addr = ""
            for i, m in enumerate(mask):
                v = "0"
                if i >= len(mask) - len(orig_addr):
                    v = orig_addr[len(orig_addr) - (len(mask) - i)]
                if m != "0":
                    v = m
                out_addr += v
            for i in range(0, 2**out_addr.count("X")):
                x = [c for c in out_addr]
                k = 0
                for j, f in enumerate(out_addr):
                    if f == "X":
                        x[j] = str((i >> k) & 1)
                        k += 1
                mem[int("".join(x), 2)] = val
    s = 0
    for m in mem.values():
        s += m
    print(s)