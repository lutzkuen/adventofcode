
import code
import math

with open("input.txt", "r") as f:
    instructions = [line.replace('\n', '') for line in f.readlines()]

pos = [0, 0, 1, -10]


def do_instruction(instruction, pos):
    if instruction[0] == 'N':
        pos[2] += int(instruction.replace('N', ''))
    elif instruction[0] == 'S':
        pos[2] -= int(instruction.replace('S', ''))
    elif instruction[0] == 'W':
        pos[3] += int(instruction.replace('W', ''))
    elif instruction[0] == 'E':
        pos[3] -= int(instruction.replace('E', ''))
    elif instruction[0] == 'F':
        mult = int(instruction.replace('F', ''))
        pos[0] += mult * pos[2]
        pos[1] += mult * pos[3]
    elif instruction[0] == 'R':
        angle = - math.pi * float(instruction.replace('R', '')) / 180
        pos = [pos[0], pos[1], pos[2] * math.cos(angle) - pos[3] * math.sin(angle), pos[2] * math.sin(angle) + pos[3] * math.cos(angle)]
        pos[2] = int(round(pos[2]))
        pos[3] = int(round(pos[3]))
    elif instruction[0] == 'L':
        angle = math.pi * float(instruction.replace('L', '')) / 180
        pos = [pos[0], pos[1], pos[2] * math.cos(angle) - pos[3] * math.sin(angle), pos[2] * math.sin(angle) + pos[3] * math.cos(angle)]
        pos[2] = int(round(pos[2]))
        pos[3] = int(round(pos[3]))
    return pos

for ins in instructions:
    print(ins)
    pos = do_instruction(ins, pos)
    print(pos)
    # code.interact(banner='', local=locals())

print(abs(pos[0]) + abs(pos[1]))
