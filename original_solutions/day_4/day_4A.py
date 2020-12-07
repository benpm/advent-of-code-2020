with open("input_4.txt") as f:
    pps = ("".join([l for l in f])).split("\n\n")
    af = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    n = 0
    for pp in pps:
        fields = set([f.strip().split(":")[0] for f in pp.replace("\n", " ").split(" ")])
        print(fields)
        if fields == af or len(fields) > len(af):
            n += 1
    print(n)