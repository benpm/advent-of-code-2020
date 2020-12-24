import re
from itertools import product
from pprint import pp
from copy import deepcopy
import pandas as pd
from collections import defaultdict

rules = defaultdict(set)
with open("input_19.txt") as input_file:
    t_rules, t_words = [s.split("\n") for s in input_file.read().split("\n\n")]

# process input
for t_rule in t_rules:
    m = re.findall(r"\d+", t_rule)
    if len(m) == 1:
        keys = re.search(r"[\"](.)[\"]", t_rule).groups(1)
    elif "|" in t_rule and len(m) == 3:
        keys = (m[1], m[2])
    else:
        keys = tuple([tuple(m[i : i+2]) for i in range(1, len(m), 2)])
    for key in keys:
        if len(key) == 1:
            rules[key[0]].add(m[0])
        else:
            rules[key].add(m[0])

pp(rules)
# fix grammar to be CNF
# while True:
#     nr = deepcopy(rules)
#     for k, vals in nr.items():
#         if type(k) == int:
#             rules.pop(k)
#             for v in vals:
#                 for kk, vv in nr.items():
#                     if type(kk) == tuple and v in kk:
#                         rules.pop(kk)
#                         nk = [(k if ik == v else ik) for ik in kk]
#                         rules[tuple(nk)] = vv
#                     elif 
#             break
#     else:
#         break
# pp(rules)

# validate the strings
valid = 0
for word in [t.strip() for t in t_words]:
    l = len(word)
    m = [[set() for _ in range(l)] for _ in range(l)]
    print(word)
    for r in range(l):
        for c in range(l - r):
            if r == 0:
                m[r][c] = set().union(rules[word[c]], *[rules[z] for z in rules[word[c]]])
            else:
                for j in range(r):
                    m[r][c].update(*[rules[p] for p in product(m[j][c], m[r-j-1][c+j+1]) if p in rules])
    # pd.DataFrame(m).to_csv("matrix.csv")
    # exit()
    if "0" in m[-1][0]:
        valid += 1
print("valid:", valid)