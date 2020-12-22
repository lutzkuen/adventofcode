
import code

class Blocksim:

    def __init__(self):
        self.active_cubes = []
        y = 0
        z = 0
        w = 0
        with open("input.txt", "r") as f:
            for line in f.readlines():
                x = 0
                for box in line.replace('\n', ''):
                    if box == '#':
                        self.active_cubes.append({'x': x, 'y': y, 'z': z, 'w': w})
                    x += 1
                y += 1
        print(self.active_cubes)

    def print_state(self):
        xmin = min([box['x'] for box in self.active_cubes])
        xmax = max([box['x'] for box in self.active_cubes])+1
        ymin = min([box['y'] for box in self.active_cubes])
        ymax = max([box['y'] for box in self.active_cubes])+1
        zmin = min([box['z'] for box in self.active_cubes])
        zmax = max([box['z'] for box in self.active_cubes])+1
        for z in range(zmin, zmax):
            print(f"z = {z}")
            for y in range(ymin, ymax):
                line = ''
                for x in range(xmin, xmax):
                    _, is_occupied = self.get_box_neighbors(x, y, z)
                    if is_occupied:
                        line += '#'
                    else:
                        line += '.'
                print(line)
                print('-----------------------------')

    def get_box_neighbors(self, x, y, z, w):
        neigs = 0
        is_occupied = False
        for box in self.active_cubes:
            if abs(x - box['x']) > 1:
                continue
            if abs(y - box['y']) > 1:
                continue
            if abs(z - box['z']) > 1:
                continue
            if abs(w - box['w']) > 1:
                continue
            if abs(box['x'] - x) < 0.5 and abs(box['y'] - y) < 0.5 and abs(box['z'] - z) < 0.5 and abs(box['w'] - w) < 0.5:
                is_occupied = True
            # else:
            #     print(f"{x} {y} {z} has neighbor {box}")
            # code.interact(banner='', local=locals())
            neigs += 1
        return neigs, is_occupied

    def run_cycle(self):
        new_cubes = []
        xmin = min([box['x'] for box in self.active_cubes])-1
        xmax = max([box['x'] for box in self.active_cubes])+2
        ymin = min([box['y'] for box in self.active_cubes])-1
        ymax = max([box['y'] for box in self.active_cubes])+2
        zmin = min([box['z'] for box in self.active_cubes])-1
        zmax = max([box['z'] for box in self.active_cubes])+2
        wmin = min([box['w'] for box in self.active_cubes])-1
        wmax = max([box['w'] for box in self.active_cubes])+2
        # print(self.active_cubes)
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                for z in range(zmin, zmax):
                    for w in range(wmin, wmax):
                        neigs, is_occupied = self.get_box_neighbors(x, y, z, w)
                        if neigs == 3 and not is_occupied:
                            # print(f"unoccupied field {x} {y} {z} with neighbors")
                            # code.interact(banner='', local=locals())
                            new_cubes.append({'x': x, 'y': y, 'z': z, 'w': w})
                        if int(neigs) in [3, 4] and is_occupied:
                            # print(f"occupied field {x} {y} {z} with neighbors")
                            # code.interact(banner='', local=locals())
                            new_cubes.append({'x': x, 'y': y, 'z': z, 'w': w})
        self.active_cubes = new_cubes
        print(f"finished, there are {len(self.active_cubes)} cubes")
        

bs = Blocksim()
for i in range(6):
    # bs.print_state()
    # code.interact(banner='', local=locals())
    bs.run_cycle()
