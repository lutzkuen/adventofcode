
import numpy as np
import code
import math


EDGE_KINDS = ['top', 'bot', 'lef', 'rig', 'rtop', 'rbot', 'rlef', 'rrig']


class Tile:
    def __init__(self, content, tile_id):
        self.arr = np.array(content)
        self.pos = None
        self.tile_id = tile_id
        print(self.tile_id)
        print(self.arr)

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def get_edge(self, kind):
        if kind == 'top':
            return self.arr[0, :]
        elif kind == 'bot':
            return self.arr[-1, :]
        elif kind == 'lef':
            return self.arr[:, 0]
        elif kind == 'rig':
            return self.arr[:, -1]
        elif kind == 'rtop':
            return self.arr[0, ::-1]
        elif kind == 'rbot':
            return self.arr[-1, ::-1]
        elif kind == 'rlef':
            return self.arr[::-1, 0]
        elif kind == 'rrig':
            return self.arr[::-1, -1]

    def rotate(self):
        self.arr = np.rot90(self.arr)

    def flip_lr(self):
        self.arr = self.arr[::-1, :]

    def flip_ud(self):
        self.arr = self.arr[:, ::-1]

    def flip_match(self, kind, edge):
        for flipnum in range(4):
            if kind == 'lef':
                if np.all(self.arr[:, 0] == edge):
                    return True
                self.arr = self.arr[::-1, :]
                if np.all(self.arr[:, 0] == edge):
                    return True
            elif kind == 'top':
                if np.all(self.arr[0, :] == edge):
                    return True
                self.arr = self.arr[:, ::-1]
                if np.all(self.arr[0, :] == edge):
                    return True
            self.rotate()


class Puzzle:

    def __init__(self, filename):
        self.tiles = []
        with open(filename, "r") as f:
            tile_id = None
            for line in f.readlines():
                if 'Tile' in line:
                    tile_id = int(line.replace('\n', '').split(' ')[1].replace(':', ''))
                    content = []
                elif len(line) < 3:
                    self.tiles.append(Tile(content, tile_id))
                else:
                    content.append(list(line.replace('\n', '')))
            self.tiles.append(Tile(content, tile_id))
        # print(self.tiles)

    def get_corners(self):
        # there must be exactly 4 corner tiles
        mult = 1
        for tile_1 in self.tiles:
            matches = 0
            for tile_2 in self.tiles:
                if tile_1.tile_id == tile_2.tile_id:
                    continue
                for e1 in EDGE_KINDS:
                    for e2 in EDGE_KINDS:
                        if np.all(tile_1.get_edge(e1) == tile_2.get_edge(e2)):
                            matches += 1
            if matches == 4:
                print(tile_1.tile_id)
                mult *= tile_1.tile_id
            # else:
            #     print(f"{tile_1.tile_id} {matches}")
        print(mult)
        return mult

    def get_tile_by_id(self, tile_id):
        for tile in self.tiles:
            if tile.tile_id == tile_id:
                return tile

    def get_first_corner(self):
        # there must be exactly 4 corner tiles
        mult = 1
        for tile_1 in self.tiles:
            matches = 0
            for tile_2 in self.tiles:
                if tile_1.tile_id == tile_2.tile_id:
                    continue
                for e1 in EDGE_KINDS:
                    for e2 in EDGE_KINDS:
                        if np.all(tile_1.get_edge(e1) == tile_2.get_edge(e2)):
                            matches += 1
            if matches == 4:
                return tile_1.tile_id

    def get_tile_by_pos(self, row, col):
        for tile in self.tiles:
            if not tile.pos:
                continue
            r,c = tile.pos
            if r == row and c == col:
                return tile

    def get_matching_tile(self, cond_1, cond_2):
        for tile in self.tiles:
            # print(tile.tile_id)
            if tile.pos:
                continue
            for rotnum in range(4):
                tile.rotate()
                for flipudnum in range(2):
                    tile.flip_ud()
                    for fliplrnum in range(2):
                        tile.flip_lr()
                        is_candidate = True
                        if len(cond_1) == 0:
                            for tile_1 in self.tiles:
                                if tile_1.pos:
                                    continue
                                if tile_1.tile_id == tile.tile_id:
                                    continue
                                for e1 in EDGE_KINDS:
                                    if np.all(tile_1.get_edge(e1) == tile.get_edge('lef')):
                                        is_candidate = False
                        else:
                            if not np.all(cond_1 == tile.arr[:, 0]):
                                is_candidate = False
                        if not is_candidate:
                            continue
                        if len(cond_2) == 0:
                            for tile_1 in self.tiles:
                                if tile_1.pos:
                                    continue
                                if tile_1.tile_id == tile.tile_id:
                                    continue
                                for e1 in EDGE_KINDS:
                                    if np.all(tile_1.get_edge(e1) == tile.get_edge('top')):
                                        is_candidate = False
                        else:
                            if not np.all(cond_2 == tile.arr[0, :]):
                                is_candidate = False
                        if not is_candidate:
                            continue
                        return tile
                

    def get_tile_matches(self, side, exclude_tile_id):
        for tile_1 in self.tiles:
            if tile_1.tile_id == exclude_tile_id:
                continue
            for ekind in EDGE_KINDS:
                edge = tile_1.get_edge(ekind)
                if np.all(edge == side):
                    return tile_1.tile_id
        return None

    def all_set(self):
        for tile in self.tiles:
            if not tile.pos:
                return False
        return True
    
    def solve_puzzle(self): 
        # first_corner_id = self.get_first_corner()
        # first_tile = self.get_tile_by_id(first_corner_id)
        gridsize = int(round(math.sqrt(len(self.tiles))))
        tile_size = 0
        for row in range(1, gridsize+1):
            for col in range(1, gridsize+1):
                print(f"{row} {col}")
                if col == 1:
                    cond_1 = []
                else:
                    l_tile = self.get_tile_by_pos(row, col-1)
                    cond_1 = l_tile.arr[:, -1]
                if row == 1:
                    cond_2 = []
                else:
                    r_tile = self.get_tile_by_pos(row-1, col)
                    cond_2 = r_tile.arr[-1, :]
                next_tile = self.get_matching_tile(cond_1, cond_2)
                if not next_tile:
                    code.interact(banner='', local=locals())
                next_tile.set_pos((row, col))
                tile_size = next_tile.arr[0].size
                print(f"{next_tile.tile_id} {row} {col}")
                print(next_tile.arr)
        sol_size = (tile_size-2)*gridsize
        sol_tile = np.zeros((sol_size, sol_size))
        for row in range(1, gridsize+1):
            for col in range(1, gridsize+1):
                tile = self.get_tile_by_pos(row, col)
                for i in range(tile_size-2):
                    for j in range(tile_size-2):
                        target_i = (tile_size-2)*(row-1)+i
                        target_j = (tile_size-2)*(col-1)+j
                        if tile.arr[i+1, j+1] == '#':
                            # code.interact(banner='', local=locals())
                            sol_tile[target_i, target_j] = 1
        print(sol_tile)
        sea_monster = np.zeros((3, 20))
        sea_monster[0,18] = 1
        sea_monster[1,0] = 1
        sea_monster[1,5] = 1
        sea_monster[1,6] = 1
        sea_monster[1,11] = 1
        sea_monster[1,12] = 1
        sea_monster[1,17] = 1
        sea_monster[1,18] = 1
        sea_monster[1,19] = 1
        sea_monster[2,1] = 1
        sea_monster[2,4] = 1
        sea_monster[2,7] = 1
        sea_monster[2,10] = 1
        sea_monster[2,13] = 1
        sea_monster[2,16] = 1
        print(sea_monster)
        monster_parts = 0
        for rotation in range(4):
            sol_tile = np.rot90(sol_tile)
            for flip_up in range(2):
                sol_tile = sol_tile[:, ::-1]
                for flip_lr in range(2):
                    sol_tile = sol_tile[::-1, :]
                    for i in range(sol_size-3):
                        for j in range(sol_size-20):
                            sub_monster = 0
                            is_monster = True
                            for k in range(3):
                                for l in range(20):
                                    if sea_monster[k, l] == 1 and sol_tile[i+k, j+l] != 1:
                                        is_monster = False
                                        sub_monster = 0
                                        break
                                    elif sea_monster[k, l] == 1 and sol_tile[i+k, j+l] == 1:
                                        sub_monster += 1
                            if is_monster:
                                # code.interact(banner='', local=locals())
                                monster_parts += sub_monster
        return int(round(np.sum(np.sum(sol_tile)) - monster_parts/2))


p = Puzzle("test_input.txt")
parts = p.solve_puzzle()
assert parts == 273
# assert p.get_corners() == 20899048083289
# 
p2 = Puzzle("input.txt")
print(p2.solve_puzzle())
