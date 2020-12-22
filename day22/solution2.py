
import code

class SpaceCards:
    def __init__(self, filename):
        self.deck1 = []
        self.deck2 = []
        pnum = None
        with open(filename, "r") as f:
            for line in f.readlines():
                if "Player" in line:
                    pnum = int(line.replace("Player ", "").split(":")[0])
                else:
                    try:
                        if pnum == 1:
                            self.deck1.append(int(line.replace("\n", "")))
                        elif pnum == 2:
                            self.deck2.append(int(line.replace("\n", "")))
                    except:
                        pass
        # print(self.deck1)
        # print(self.deck2)

    def recursive_subgame(self, _deck1, _deck2, configs):
        deck1 = _deck1.copy()
        deck2 = _deck2.copy()
        print("Recursive game")
        print(deck1)
        print(deck2)
        if len(deck2) == 0:
            return 1
        if len(deck1) == 0:
            return 2
        # if deck1[0] >= len(deck1) or deck2[0] >= len(deck2):
        # code.interact(banner='', local=locals())
        while len(deck1) > 0 and len(deck2) > 0:
            checksum = ','.join(['deck1']+[str(d) for d in deck1]+['deck2']+[str(d) for d in deck2])
            if checksum in configs:
                return 1
            configs.append(checksum)
            if deck1[0] > deck2[0]:
                deck1.append(deck1.pop(0))
                deck1.append(deck2.pop(0))
            elif deck2[0] > deck1[0]:
                deck2.append(deck2.pop(0))
                deck2.append(deck1.pop(0))
        if len(deck2) == 0:
            return 1
        if len(deck1) == 0:
            return 2
        # code.interact(banner='', local=locals())
        print(deck1)
        print(deck2)
        return self.recursive_subgame(deck1, deck2, configs)
        # else:
        #     return self.recursive_subgame([c for c in deck1[1:(deck1[0]+1)]], [c for c in deck2[1:(deck2[0]+1)]], [])
    

    def finalize_game(self, is_stall_win=False):
        score = 0
        for i,k in enumerate(self.deck1[::-1]):
            score += (i+1)*k
        if is_stall_win:
            return score
        for i,k in enumerate(self.deck2[::-1]):
            score += (i+1)*k
        return score

    def play_game(self):
        turn_num = 0
        while True:
            if len(self.deck1) == 0 or len(self.deck2) == 0:
                return self.finalize_game()
            if self.deck1[0] >= len(self.deck1) or self.deck2[0] >= len(self.deck2):
                if self.deck1[0] > self.deck2[0]:
                    winner = 1
                if self.deck2[0] > self.deck1[0]:
                    winner = 2
            else:
                winner = self.recursive_subgame([c for c in self.deck1[1:(self.deck1[0]+1)]], [c for c in self.deck2[1:(self.deck2[0]+1)]], [])
            # code.interact(banner='', local=locals())
            if winner == 1:
                self.deck1.append(self.deck1.pop(0))
                self.deck1.append(self.deck2.pop(0))
            elif winner == 2:
                self.deck2.append(self.deck2.pop(0))
                self.deck2.append(self.deck1.pop(0))
            turn_num += 1
            print(self.deck1)
            print(self.deck2)
            print(f"{turn_num} {len(self.deck1)} {len(self.deck2)}")
            

# sp = SpaceCards("test_input.txt")
# print(sp.play_game())
# assert sp.play_game() == 291

sp = SpaceCards("input.txt")
print(sp.play_game())
