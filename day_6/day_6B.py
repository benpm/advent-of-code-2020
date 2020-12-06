with open("input_6.txt") as f:
    groups = ("".join([l for l in f])).split("\n\n")
    n = 0
    for group in groups:
        m = {}
        answers = []
        a = [f.strip() for f in group.replace("\n", " ").split(" ")]
        for c in a:
            for cc in c:
                if cc in m.keys():
                    m[cc] += 1
                else:
                    m[cc] = 1
        t = 0
        for c in m.values():
            if c == len(a):
                t += 1
        n += t
    print(n)