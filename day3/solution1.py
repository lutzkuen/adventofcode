
with open('input.txt', 'r') as f:
    trees_map = [line.replace('\n', '') for line in f.readlines()]

position = 0

height = len(trees_map)

width = len(trees_map[0])

TREE = '#'

pos_x = 0
pos_y = 0

DELTA_X = 3
DELTA_Y = 1

num_trees = 0

while pos_y < height-1:
    pos_x = (pos_x + DELTA_X) % width
    pos_y += DELTA_Y
    print(pos_x)
    print(pos_y)
    print(trees_map[pos_y])
    if trees_map[pos_y][pos_x] == TREE:
        num_trees += 1

print(num_trees)
