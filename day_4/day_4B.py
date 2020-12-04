with open("input_4.txt") as f:
    pps = ("".join([l for l in f])).split("\n\n")
    n = 0
    for pp in pps:
        fields = [f.strip() for f in pp.replace("\n", " ").split(" ")]
        validfields = 0
        for f in fields:
            if len(f) == 0:
                continue
            valid = False
            name = f.split(":")[0]
            v = f.split(":")[1]
            if name == "byr":
                valid = len(v) == 4 and int(v) >= 1920 and int(v) <= 2002
            elif name == "iyr":
                valid = len(v) == 4 and int(v) >= 2010 and int(v) <= 2020
            elif name == "eyr":
                valid = len(v) == 4 and int(v) >= 2020 and int(v) <= 2030
            elif name == "hgt":
                if "cm" in v:
                    vv = int(v.split("cm")[0])
                    valid = vv >= 150 and vv <= 193
                elif "in" in v:
                    vv = int(v.split("in")[0])
                    valid = vv >= 59 and vv <= 76
            elif name == "hcl":
                valid = (v[0] == "#") and (len(v) == 7)
                for c in v[1:]:
                    valid = (valid) and (c in "0123456789abcdef")
            elif name == "ecl":
                valid = v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            elif name == "pid":
                valid = (len(v) == 9)
                for c in v[1:]:
                    valid = (valid) and (c in "0123456789")
            if valid:
                validfields += 1
        if validfields >= 7:
            n += 1
    print(n)