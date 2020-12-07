import re
from collections import defaultdict

holding_rules: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)

def find_holders_of(search_for: str, search_from: str, result: set[str]):
    for held in holding_rules[search_from]:
        find_holders_of(search_for, held[1], result)
        if held[1] in result or held[1] == search_for:
            result.add(search_from)

def bags_within(bag_color: str):
    i = 1
    for held in holding_rules[bag_color]:
        i += held[0] * bags_within(held[1])
    return i

with open("../../original_solutions/day_7/input_7.txt") as input_file:
    for line in [line.strip() for line in input_file]:
        holding_bag = re.search(r"(\w+ \w+) bags", line).group(1)
        if "contain no other bags" not in line:
            for held_str in line.split("contain")[1].split(", "):
                held = re.search(r"(\d+) (\w+ \w+) bag", held_str)
                holding_rules[holding_bag].append((int(held.group(1)), held.group(2)))
    result: set[str] = set()
    for bag_color in list(holding_rules.keys()):
        find_holders_of("shiny gold", bag_color, result)
    print("part A:", len(result))
    print("part B:", bags_within("shiny gold") - 1)