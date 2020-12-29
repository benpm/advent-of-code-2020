import tqdm
with open("input_25.txt") as input_file:
    card_pub = int(input_file.readline())
    door_pub = int(input_file.readline())
    ekeys = []

    for key in [card_pub, door_pub]:
        sn = 7
        k = 1
        for i in tqdm.trange(1, 10000000):
            k = (k * sn) % 20201227
            if k == key:
                break
        else:
            continue
        print(key, "subject number=", sn, "loop size=", i)
        ekeys.append((sn, i))
    k = 1
    for i in range(0, ekeys[1][1]):
        k = (k * card_pub) % 20201227
    print(k)
    
