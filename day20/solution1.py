
import numpy as np


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


p = Puzzle("test_input.txt")
assert p.get_corners() == 20899048083289

p2 = Puzzle("input.txt")
print(p2.get_corners())
