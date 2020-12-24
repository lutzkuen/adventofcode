
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

hs = HexSolve("test_input.txt")
assert hs.make_moves() == 10

hs = HexSolve("input.txt")
print(hs.make_moves())
