
with open("input_22.txt") as input_file:
    t_players = input_file.read().split("\n\n")
    players = [[], []]
    players[0] = [int(x) for x in t_players[0].split("\n")[1:]]
    players[1] = [int(x) for x in t_players[1].split("\n")[1:]]
    r = 1
    while len(players[0]) > 0 and len(players[1]) > 0:
        winner = 1
        if players[0][0] > players[1][0]:
            winner = 0
        loser = int(not winner)
        players[winner].extend(reversed(sorted([players[0][0], players[1][0]])))
        players[winner].pop(0)
        players[loser].pop(0)
        r += 1
    loser = 1
    if len(players[0]) == 0:
        loser = 0
    winner = int(not loser)
    print("part A:", sum([v * (i + 1) for i, v in enumerate(reversed(players[winner]))]))