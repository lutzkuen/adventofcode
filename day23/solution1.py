
import code

INPUT = "362981754"
TEST_INPUT = "389125467"
TEST_RESULT = "67384529"


class CrabGame:
    def __init__(self, input_str):
        self.state = [int(i) for i in list(input_str)]

    def do_turn(self):
        print(self.state)
        cut_section = []
        for _ in range(3):
            cut_section.append(self.state.pop(1))
        is_done = False
        next_number = self.state[0]-1
        while not is_done:
            if next_number not in self.state:
                if next_number > min(self.state):
                    next_number -= 1
                else:
                    next_number = max(self.state)
            else:
                is_done = True
        ins_idx = self.state.index(next_number)
        for i,k in enumerate(cut_section):
            self.state.insert(i+1+ins_idx, k)
        self.state.append(self.state.pop(0))
        print(self.state)
        # code.interact(banner='', local=locals())

    def get_sorting_after_one(self):
        st = ''.join([str(k) for k in self.state])
        pt1, pt2 = st.split("1")
        return pt2+pt1

cg = CrabGame(TEST_INPUT)

for _ in range(100):
    cg.do_turn()
print(cg.get_sorting_after_one())
assert cg.get_sorting_after_one() == TEST_RESULT


cg = CrabGame(INPUT)
for _ in range(100):
    cg.do_turn()
print(cg.get_sorting_after_one())
