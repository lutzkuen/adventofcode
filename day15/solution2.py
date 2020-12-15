
import code

class NumKeeper:
    def __init__(self):
        self.nums = dict()
        self.last_num = None
        self.it = 0
    
    def add_num(self, number):
        if number in self.nums.keys():
            p_turn = self.nums[number]['p_turn']
            self.nums[number] = {
                'p_turn': self.it,
                'q_turn': p_turn
            }
        else:
            self.nums[number] = {
                'p_turn': self.it,
                'q_turn': -1
            }
        self.last_num = number
        # code.interact(banner='', local=locals())
        self.it += 1

    def get_latest_num(self):
        if self.nums[self.last_num]['q_turn'] < 0:
            return 0
        else:
            return self.nums[self.last_num]['p_turn'] - self.nums[self.last_num]['q_turn']

    def do_turn(self):
        self.add_num(self.get_latest_num())

    def get_it(self):
        return self.it
        

with open("input.txt", "r") as f:
    numbers = f.read().replace('\n', '').split(',')

num_keeper = NumKeeper()

[num_keeper.add_num(int(num)) for num in numbers]

while num_keeper.get_it() < 30000000:
    num_keeper.do_turn()
    if num_keeper.get_it() % 100000 == 0:
        print(f"{num_keeper.get_it()} {num_keeper.nums[num_keeper.last_num]}")
    if num_keeper.get_it() >= 29999997:
        print(f"{num_keeper.get_it()} {num_keeper.nums[num_keeper.last_num]}")

print(num_keeper.last_num)
print(num_keeper.get_latest_num())

