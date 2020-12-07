import re
from collections import defaultdict

holding_rules: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)

def bags_within(bag_color):
    i = 1
    for rule in holding_rules[bag_color]:
        i += rule[0] * bags_within(rule[1])
    return i

with open("../../original_solutions/day_7/input_7.txt") as input_file:
    for line in [line.strip() for line in input_file]:
        holding_bag = re.search(r"(\w+ \w+) bags", line).group(1)
        if "contain no other bags" not in line:
            for held_str in line.split("contain")[1].split(", "):
                held = re.search(r"(\d+) (\w+ \w+) bag", held_str)
                holding_rules[holding_bag].append((int(held.group(1)), held.group(2)))
    print(bags_within("shiny gold") - 1)