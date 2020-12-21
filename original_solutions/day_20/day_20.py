from itertools import chain
import re
from collections import defaultdict
import math
from copy import deepcopy
import numpy as np

card_len = 0

N = 0
E = 1
S = 2
W = 3

def side2num(string):
    n = 0
    for i, c in enumerate(string):
        n |= int(c == "#") << i
    return n

def invert(n):
    global card_len
    v = 0
    for i in range(card_len):
        v |= ((n >> i) & 1) << (card_len - i - 1)
    return v

with open("input_20.txt") as input_file:
    t_cards = [card.split("\n") for card in input_file.read().split("\n\n")]
    card_len = len(t_cards[0][1].strip())
    card_imgs = dict()
    # generate dict [tmap] of all transformations of each tile [N,E,S,W] -> tile ID
    #   horizontal flip: swap N&S, invert E&W
    #   vertical flip: swap E&W, invert N&S
    #   rotate 0: nothing
    #   rotate 1: shift right 1, invert N&S
    #   rotate 2: rotate 1 x2
    #   rotate 3: rotate 1 x3
    tmap = dict()
    for t_card in t_cards:
        tileID = int(re.match(r"Tile (\d+):", t_card[0]).group(1))
        t_card = t_card[1:]
        og_card = np.array([list(line) for line in t_card])
        og_card[og_card == "#"] = 1
        og_card[og_card == "."] = 0
        og_card = og_card.astype(np.int)

        # Perform all transformations
        for i in range(2 * 2):
            cardt = og_card.copy()
            # Horizontal flip
            if i & 1 == 0:
                cardt = np.flipud(cardt)
            # Vertical flip
            if i & 2 == 0:
                cardt = np.fliplr(cardt)
            # Rotations
            for j in range(4):
                edges = (
                    int("".join(cardt[0].astype(str)), 2),
                    int("".join(cardt[:,-1].astype(str)), 2),
                    int("".join(cardt[-1].astype(str)), 2),
                    int("".join(cardt[:,0].astype(str)), 2)
                )
                card_imgs[edges] = cardt
                tmap[edges] = tileID
                cardt = np.rot90(cardt, -1)
    print("transforms:", len(tmap))
        
    # for each edge number, collect tileIDs that contain it
    occurences = defaultdict(set)
    for cardT, cardID in tmap.items():
        for edge in cardT:
            occurences[edge].add(cardID)
    # find edge numbers that are on the boundary: edges 
    bound_edges = set()
    for edge, cardIDs in occurences.items():
        if len(cardIDs) == 1:
            bound_edges.add(edge)
    print("bound edges:", len(bound_edges))

    # grid of card transforms
    g_len = int(math.sqrt(len(t_cards)))
    grid = [[None for _ in range(g_len)] for _ in range(g_len)]

    # find the corners
    corners = []
    for cardT, cardID in tmap.items():
        edges = [edge for edge in cardT if edge in bound_edges]
        if len(edges) == 2:
            corners.append((cardT, cardID))
            if len(edges) >= 3: print(cardT, cardID)
    print("corner transforms:", len(set([t for t, _ in corners])))
    print("corner card IDs:", len(set([i for _, i in corners])))
    print("-> part A:", math.prod(list(set([i for _, i in corners]))))

    # find the top-left corner candidates
    tl_corners = []
    for cardT, cardID in tmap.items():
        edges = [edge for edge in [cardT[N], cardT[W]] if edge in bound_edges]
        if len(edges) == 2:
            tl_corners.append((cardT, cardID))
    print("top-left corner transforms:", len(set([t for t, _ in tl_corners])))

    # cards with the same number on opposite sides
    for cardT, cardID in tmap.items():
        if cardT[N] == invert(cardT[E]):
            print(cardT, cardID)
        elif cardT[S] == invert(cardT[W]):
            print(cardT, cardID)

    # left-to-right top-to-bottom discover tiles
    #   for each undiscovered tile T,
    #   search through tdict for side numbers that exactly match neighbors opposite side (north->south, east->west),
    #   if neighbor is edge, then search the no match set instead of side number
    #   once found, tile ID added to grid, and all tdict entries with val=tileID are removed
    #   go through every possible top-left corner
    for tl_corner in tl_corners:
        grid = [[None for _ in range(g_len)] for _ in range(g_len)]
        grid[0][0] = tl_corner
        tmap_copy = deepcopy(tmap)
        # remove top-left corner
        for cardT, cardID in list(tmap_copy.items()):
            if cardID == tl_corner[1]:
                tmap_copy.pop(cardT)
        try:
            for row in range(g_len):
                for col in range(g_len):
                    if grid[row][col] != None:
                        continue
                    matches = []
                    for cardT, cardID in tmap_copy.items():
                        # check if neighbor's edges match
                        for d, p in enumerate([(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]):
                            # check neighbor for matching edge num
                            if 0 <= p[0] < g_len and 0 <= p[1] < g_len:
                                neighbor = grid[p[0]][p[1]]
                                # empty neighbor should not be boundary
                                if neighbor == None:
                                    continue
                                # check that opposite edge of neighbor card matches edge of current card
                                elif neighbor[0][(d + 2) % 4] != cardT[d]:
                                    break
                            # ensure that if tile is on edge, edge sides are in boundary edges set
                            elif cardT[d] not in bound_edges:
                                break
                        else:
                            matches.append((cardT, cardID))
                    if len(matches) != 1:
                        assert(False)
                    match = matches[-1]
                    # remove all the transforms for the found tile from the map
                    for cardT, cardID in list(tmap_copy.items()):
                        if cardID == match[1]:
                            tmap_copy.pop(cardT)
                    # set grid
                    grid[row][col] = match
        except AssertionError as e:
            continue
        else:
            # place the tiles
            img_len = g_len * (card_len - 2)
            a = np.ndarray((img_len, img_len), dtype=np.int)
            for row in range(g_len):
                for col in range(g_len):
                    a[row * (card_len - 2):(row + 1) * (card_len - 2),\
                      col * (card_len - 2):(col + 1) * (card_len - 2)] =\
                      card_imgs[grid[row][col][0]][1:-1,1:-1]
            # find sea monsters
            sm = """00000000000000000010 
                    10000110000110000111
                    01001001001001001000"""
            sm = np.array([list(l.strip()) for l in sm.split("\n")]).astype(np.int)
            sm_count = 0
            for row in range(img_len - sm.shape[0]):
                for col in range(img_len - sm.shape[1]):
                    if np.all(a[row:row+sm.shape[0], col:col+sm.shape[1]] & sm == sm):
                        sm_count += 1
            if sm_count > 0:
                print(" -> part B:", np.sum(a) - (sm_count * np.sum(sm)))