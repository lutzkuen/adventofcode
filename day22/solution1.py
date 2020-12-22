
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
        print(self.deck1)
        print(self.deck2)

    def finalize_game(self):
        score = 0
        for i,k in enumerate(self.deck1[::-1]):
            score += (i+1)*k
        for i,k in enumerate(self.deck2[::-1]):
            score += (i+1)*k
        return score

    def play_game(self):
        turn_num = 0
        while True:
            if len(self.deck1) == 0 or len(self.deck2) == 0:
                return self.finalize_game()
            if self.deck1[0] > self.deck2[0]:
                self.deck1.append(self.deck1.pop(0))
                self.deck1.append(self.deck2.pop(0))
            elif self.deck2[0] > self.deck1[0]:
                self.deck2.append(self.deck2.pop(0))
                self.deck2.append(self.deck1.pop(0))
            turn_num += 1
            print(f"{turn_num} {len(self.deck1)} {len(self.deck2)}")
            

sp = SpaceCards("test_input.txt")
assert sp.play_game() == 306

sp = SpaceCards("input.txt")
print(sp.play_game())
