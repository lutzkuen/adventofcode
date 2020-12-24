
# import code
# import cProfile
import numpy as np

INPUT = "362981754"
TEST_INPUT = "389125467"
TEST_RESULT = 149245887792

class Cup:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def set_next(self, n):
        self.next = n
    
    def get_next(self):
        return self.next


class CrabGame:
    def __init__(self, input_str):
        self.cup_by_value = dict()
        self.current = None
        self.last = None
        for i in list(input_str):
            new_cup = Cup(int(i))
            self.cup_by_value[int(i)] = new_cup
            if not self.current:
                self.current = new_cup
            if self.last:
                self.last.set_next(new_cup)
            self.last = new_cup
        for i in range(10, 1_000_001):
            new_cup = Cup(i)
            self.cup_by_value[i] = new_cup
            self.last.set_next(new_cup)
            self.last = new_cup
        self.last.set_next(self.current)
        # self.current_pointer = 0

    def do_turn(self):
        cs_first = self.current.get_next()
        cs_last = cs_first.get_next().get_next()
        self.current.set_next(cs_last.get_next())
        cut_section = [cs_first.val, cs_first.get_next().val, cs_last.val]
        is_done = False
        next_number = self.current.val-1
        while not is_done:
            if next_number in cut_section or next_number < 1:
                if next_number > 1:
                    next_number -= 1
                else:
                    next_number = 1_000_000
            else:
                is_done = True
        ptr = self.cup_by_value[next_number]
        cs_last.set_next(ptr.get_next())
        ptr.set_next(cs_first)
        self.current = self.current.get_next()

    def run_game(self, num_turns):
        for _ in range(num_turns):
            self.do_turn()

    def get_solution_2(self):
        result = 1
        ptr = self.cup_by_value[1]
        result *= ptr.get_next().val
        result *= ptr.get_next().get_next().val
        return result

    def get_sorting_after_one(self):
        st = ''.join([str(k) for k in self.state])
        pt1, pt2 = st.split("1")
        return pt2+pt1

cg = CrabGame(TEST_INPUT)

for _ in range(10_000_000):
    if _ % 100_000 == 0:
        print(f"turn {_}")
    cg.do_turn()
print(cg.get_solution_2())
assert cg.get_solution_2() == TEST_RESULT


cg = CrabGame(INPUT)
for _ in range(10_000_000):
    if _ % 100_000 == 0:
        print(f"turn {_}")
    cg.do_turn()
print(cg.get_solution_2())
