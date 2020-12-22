def game(players):
    rounds = set()
    while len(players[0]) > 0 and len(players[1]) > 0:
        r = tuple(players[0] + [-1] + players[1])
        if r in rounds:
            return 0
        rounds.add(r)
        drawn = [players[0].pop(0), players[1].pop(0)]
        winner = 1
        if drawn[0] <= len(players[0]) and drawn[1] <= len(players[1]):
            winner = game([list(players[0])[:drawn[0]], list(players[1])[:drawn[1]]])
        elif drawn[0] > drawn[1]:
            winner = 0
        loser = int(not winner)
        players[winner].extend([drawn[winner], drawn[loser]])
    loser = 1
    if len(players[0]) == 0:
        loser = 0
    return int(not loser)

with open("input_22.txt") as input_file:
    players = [[], []]
    t_players = input_file.read().split("\n\n")
    players[0] = [int(x) for x in t_players[0].split("\n")[1:]]
    players[1] = [int(x) for x in t_players[1].split("\n")[1:]]
    winner = game(players)
    print("part B:", sum([v * (i + 1) for i, v in enumerate(reversed(players[winner]))]))