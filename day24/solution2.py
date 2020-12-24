
import code

class HexSolve:
    def __init__(self, filename):
        self.black_tiles = []
        with open(filename, "r") as f:
            self.moves = [line.replace('\n', '') for line in f.readlines()]
        
    def make_moves(self):
        for _move in self.moves:
            row = 0
            col = 0
            move = _move
            while len(move) > 0:
                print(f"{row} {col} {move}")
                if move[0] == 'e':
                    col += 1
                    move = move[1:]
                elif move[0] == 'w':
                    col -= 1
                    move = move[1:]
                elif move[:2] == 'se':
                    if row % 2 == 0:
                        row -= 1
                    else:
                        row -= 1
                        col += 1
                    move = move[2:]
                elif move[:2] == 'sw':
                    if row % 2 == 0:
                        row -= 1
                        col -= 1
                    else:
                        row -= 1
                    move = move[2:]
                elif move[:2] == 'nw':
                    if row % 2 == 0:
                        row += 1
                        col -= 1
                    else:
                        row += 1
                    move = move[2:]
                elif move[:2] == 'ne':
                    if row % 2 == 0:
                        row += 1
                    else:
                        row += 1
                        col += 1
                    move = move[2:]
                else:
                    code.interact(banner='', local=locals())
            pos = (row, col)
            if pos in self.black_tiles:
                self.black_tiles.remove(pos)
            else:
                self.black_tiles.append(pos)
        return len(self.black_tiles)

    def print_grid(self):
        row_min = min([row for row, _ in self.black_tiles])-2
        row_max = max([row for row, _ in self.black_tiles])+2
        col_min = min([col for _, col in self.black_tiles])-2
        col_max = max([col for _, col in self.black_tiles])+2
        for row in range(row_min, row_max):
            row_str = ''
            for col in range(col_min, col_max):
                is_black = False
                for tile_row, tile_col in self.black_tiles:
                    if tile_row == row and tile_col == col:
                        is_black = True
                if row % 2 != 0:
                    row_str += ' '
                if is_black:
                    row_str += 'X'
                else:
                    row_str += 'O'
                if row % 2 == 0:
                    row_str += ' '
            print(row_str)

    def run_day(self):
        new_black_tiles = []
        row_min = min([row for row, _ in self.black_tiles])-2
        row_max = max([row for row, _ in self.black_tiles])+2
        col_min = min([col for _, col in self.black_tiles])-2
        col_max = max([col for _, col in self.black_tiles])+2
        for row in range(row_min, row_max):
            for col in range(col_min, col_max):
                if (row, col) in new_black_tiles:
                    continue
                is_black = False
                for tile_row, tile_col in self.black_tiles:
                    if tile_row == row and tile_col == col:
                        is_black = True
                        break
                num_neigs = 0
                for tile_row, tile_col in self.black_tiles:
                    if tile_row == row and tile_col == col:
                        continue
                    if abs(col - tile_col) <= 1 and row == tile_row:
                        num_neigs += 1
                    elif abs(row - tile_row) <= 1 and col == tile_col:
                        num_neigs += 1
                    elif row % 2 == 0 and col - 1 == tile_col and abs(row - tile_row) <= 1:
                        num_neigs += 1
                    elif row % 2 != 0 and col + 1 == tile_col and abs(row - tile_row) <= 1:
                        num_neigs += 1
                # if row == -3 and col == -3:
                #     code.interact(banner='', local=locals())
                if 1 <= num_neigs <= 2 and is_black:
                    new_black_tiles.append((row, col))
                elif num_neigs == 2 and not is_black:
                    new_black_tiles.append((row, col))
        self.black_tiles = new_black_tiles
        return len(self.black_tiles)
        

hs = HexSolve("test_input.txt")
assert hs.make_moves() == 10
hs.print_grid()
for _ in range(100):
    num_black = hs.run_day()
    print(f"{_} {num_black}")
    # hs.print_grid()
    if _ == 0:
        assert num_black == 15
    if _ == 1:
        assert num_black == 12
print(num_black)
assert num_black == 2208

hs = HexSolve("input.txt")
print(hs.make_moves())
for _ in range(100):
    num_black = hs.run_day()
    print(f"{_} {num_black}")
print(num_black)
