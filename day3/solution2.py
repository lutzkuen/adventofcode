
with open('input.txt', 'r') as f:
    trees_map = [line.replace('\n', '') for line in f.readlines()]

position = 0

height = len(trees_map)

width = len(trees_map[0])

TREE = '#'


prod = 1

for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    pos_x = 0
    pos_y = 0
    num_trees = 0
    while pos_y < height-1:
        pos_x = (pos_x + delta_x) % width
        pos_y += delta_y
        print(pos_x)
        print(pos_y)
        print(trees_map[pos_y])
        if trees_map[pos_y][pos_x] == TREE:
            num_trees += 1
    
    print(num_trees)
    prod *= num_trees

print(prod)
