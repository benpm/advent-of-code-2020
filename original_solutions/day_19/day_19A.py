from collections import defaultdict

with open("input_19.txt", "r") as f:
    rules, inp = f.read().split("\n\n")
    rules = [l.strip() for l in rules.split("\n")]
    rules = sorted(rules, key=lambda x: int(x.split(": ")[0]))

    inp = [f" {' '.join(l.strip())} " for l in inp.split("\n")]

rRules = {}
dRules = {}
for rule in rules:
    r, oR = rule.split(": ")
    oR = oR.split(" | ")

    for o in oR:
        ins = [v.replace('"', '') for v in o.split(" ")]
        rRules[f" {' '.join(ins)} "] = f' {r} '
        dRules[f" {r} "] = f" {' '.join(ins)} "


parses = set()
doesnt = set()
skipped = defaultdict(int)
iters = 0
def parse(string, depth=0):
    global iters

    if string == " 0 ":
        return True
    if string in parses:
        return True
    if string in doesnt:
        skipped[string] += 1
        if skipped[string] % 8 == 0:
            print(skipped[string], string) 
        return False
    
    for k, v in rRules.items():
        if k not in string:
            continue
        
        inds = [i for i, _ in enumerate(string) if string.startswith(k, i)]
        for i in inds:
            nStr = string[:i] + v + string[i+len(k):]
            ret = parse(nStr, depth + 1)
            if ret == True:
                parses.add(nStr)
                parses.add(string)
                return True
            else:
                doesnt.add(nStr)
    
    return False

aInd = rRules[' a '][1:-1]
bInd = rRules[' b '][1:-1]
for ind, i in enumerate(inp):
    i = i.replace("a", aInd)
    i = i.replace("b", bInd)
    inp[ind] = i


count = 0
for i in inp:
    parse(i)
    print(skipped, i, i in parses)
    skipped = 0

print(count)