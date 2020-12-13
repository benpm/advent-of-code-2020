from math import ceil, floor
from copy import deepcopy

def part_A(depart_time: int, bus_times: dict[int, int]):
    bus = min([(p, ceil(depart_time / p) * p) for p in bus_times.values()], key=lambda v: v[1])
    return bus[0] * (bus[1] - depart_time)

def part_B(bus_times: dict[int, int]):
    bus_times = deepcopy(bus_times)
    i = -1; seq_period = 1
    while len(bus_times) > 0:
        i += seq_period
        for bus_seqn, bus_period in list(bus_times.items()):
            if i % bus_period == (bus_period - bus_seqn) % bus_period:
                seq_period *= bus_times.pop(bus_seqn)
    return i

with open("../../original_solutions/day_13/input_13.txt") as input_file:
    depart_time = int(input_file.readline())
    _b = input_file.readline()
    bus_times = {i: int(x) for i, x in enumerate(_b.split(",")) if x != "x"}
    print(part_A(depart_time, bus_times))
    print(part_B(bus_times))