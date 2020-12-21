import re
from collections import defaultdict
import math
from copy import deepcopy
import numpy as np

N = 0; E = 1; S = 2; W = 3
tmap = dict()       # map from (N,E,S,W) edge numbers to tile IDs
tile_imgs = dict()  # map from (N,E,S,W) edge numbers to tiles

# Sea monster as array of zeroes and ones
sm = """00000000000000000010 
        10000110000110000111
        01001001001001001000"""
sm = np.array([list(l.strip()) for l in sm.split("\n")]).astype(np.int)

# Process input
with open("../../original_solutions/day_20/input_20.txt") as input_file:
    t_tiles = [tile.split("\n") for tile in input_file.read().split("\n\n")]
    tile_len = len(t_tiles[0][1].strip())
    for t_tile in t_tiles:
        tileID = int(re.match(r"Tile (\d+):", t_tile[0]).group(1))
        og_tile = np.array([list(line) for line in t_tile[1:]])
        og_tile[og_tile == "#"] = 1
        og_tile[og_tile == "."] = 0
        og_tile = og_tile.astype(np.int)

        # Perform all transformations on card, adding to dictionaries
        for i in range(2 * 2):
            tile = og_tile.copy()
            # Horizontal flip
            if i & 1 == 0:
                tile = np.flipud(tile)
            # Vertical flip
            if i & 2 == 0:
                tile = np.fliplr(tile)
            # Rotations
            for j in range(4):
                edges = (
                    int("".join(tile[0].astype(str)), 2),
                    int("".join(tile[:,-1].astype(str)), 2),
                    int("".join(tile[-1].astype(str)), 2),
                    int("".join(tile[:,0].astype(str)), 2)
                )
                tile_imgs[edges] = tile
                tmap[edges] = tileID
                tile = np.rot90(tile, -1)
    
# Count number of tile transformations that have each edge
occurences = defaultdict(int)
for tileT, tileID in tmap.items():
    for edge in tileT:
        occurences[edge] += 1
# find edge numbers that are on the boundary
bound_edges = set()
for edge, n in occurences.items():
    if n == 4: # must be 4 different transformations of the same tile
        bound_edges.add(edge)

# grid of tile transforms
g_len = int(math.sqrt(len(t_tiles)))

# find the corners
corners = []
for tileT, tileID in tmap.items():
    edges = [edge for edge in tileT if edge in bound_edges]
    if len(edges) == 2:
        corners.append((tileT, tileID))
        if len(edges) >= 3: print(tileT, tileID)
print(" -> part A:", math.prod(list(set([i for _, i in corners]))))

# Find the top-left corner candidates
tl_corners = []
for tileT, tileID in corners:
    if tileT[N] in bound_edges and tileT[W] in bound_edges:
        tl_corners.append((tileT, tileID))

# Place the rest of the tiles, starting with top-left corner, for each possible top-left corner
# This will generate all possible transformations of the image!
for tl_corner in tl_corners:
    grid = [[None for _ in range(g_len)] for _ in range(g_len)]
    grid[0][0] = tl_corner
    tmap_copy = deepcopy(tmap)
    # Remove top-left corner from map
    for tileT, tileID in list(tmap_copy.items()):
        if tileID == tl_corner[1]:
            tmap_copy.pop(tileT)
    # Place the tiles
    for row in range(g_len):
        for col in range(g_len):
            if grid[row][col] != None:
                continue
            match = None
            for tileT, tileID in tmap_copy.items():
                # check if neighbor's edges match this tile's edges
                for d, p in enumerate([(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]):
                    # check neighbor for matching edge num
                    if 0 <= p[0] < g_len and 0 <= p[1] < g_len:
                        neighbor = grid[p[0]][p[1]]
                        # empty neighbor should not be boundary
                        if neighbor == None:
                            continue
                        # check that opposite edge of neighbor tile matches edge of current tile
                        elif neighbor[0][(d + 2) % 4] != tileT[d]:
                            break
                    # ensure that if tile is on edge, edge sides are in boundary edges set
                    elif tileT[d] not in bound_edges:
                        break
                else:
                    match = (tileT, tileID)
                    break
            # remove all the transforms for the found tile from the map
            for tileT, tileID in list(tmap_copy.items()):
                if tileID == match[1]:
                    tmap_copy.pop(tileT)
            # set grid
            grid[row][col] = match

    # Place the tiles
    img_len = g_len * (tile_len - 2)
    img = np.ndarray((img_len, img_len), dtype=np.int)
    for row in range(g_len):
        for col in range(g_len):
            # Place the transformed tile into the image without the borders
            img[row * (tile_len - 2):(row + 1) * (tile_len - 2),
                col * (tile_len - 2):(col + 1) * (tile_len - 2)] =\
                tile_imgs[grid[row][col][0]][1:-1,1:-1]

    # find sea monsters
    sm_count = 0
    for row in range(img_len - sm.shape[0]):
        for col in range(img_len - sm.shape[1]):
            if np.all(img[row:row+sm.shape[0], col:col+sm.shape[1]] & sm == sm):
                sm_count += 1
    if sm_count > 0:
        print(" -> part B:", np.sum(img) - (sm_count * np.sum(sm)))
        break