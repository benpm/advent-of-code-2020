with open("input_6.txt") as f:
    groups = ("".join([l for l in f])).split("\n\n")
    n = 0
    for group in groups:
        answers = set()
        a = [f.strip() for f in group.replace("\n", " ").split(" ")]
        for c in a:
            for cc in c:
                answers.add(cc)
        n += len(answers)
    print(n)