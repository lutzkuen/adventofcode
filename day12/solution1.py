
with open("input.txt", "r") as f:
    instructions = [line.replace('\n', '') for line in f.readlines()]

pos = [0, 0, 90]


def do_instruction(instruction, pos):
    if instruction[0] == 'N':
        pos[0] += int(instruction.replace('N', ''))
    elif instruction[0] == 'S':
        pos[0] -= int(instruction.replace('S', ''))
    elif instruction[0] == 'W':
        pos[1] += int(instruction.replace('W', ''))
    elif instruction[0] == 'E':
        pos[1] -= int(instruction.replace('E', ''))
    elif instruction[0] == 'F':
        if pos[2] == 90:
            pos[1] -= int(instruction.replace('F', ''))
        elif pos[2] == 270:
            pos[1] += int(instruction.replace('F', ''))
        elif pos[2] == 0:
            pos[0] += int(instruction.replace('F', ''))
        elif pos[2] == 180:
            pos[0] -= int(instruction.replace('F', ''))
    elif instruction[0] == 'R':
        pos[2] += int(instruction.replace('R', ''))
        pos[2] = pos[2] % 360
    elif instruction[0] == 'L':
        pos[2] -= int(instruction.replace('L', ''))
        pos[2] = pos[2] % 360
    return pos

for ins in instructions:
    pos = do_instruction(ins, pos)
    print(pos)

print(abs(pos[0]) + abs(pos[1]))
