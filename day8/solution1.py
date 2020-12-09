
instructions = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        instructions.append(line.replace('\n', '').replace('+', '').split(' '))

def try_bootup(instructions):
    acc = 0
    instruction = 0
    visited = [0]
    while True:
        cmd, value = instructions[instruction]
        if cmd == 'nop':
            instruction += 1
        elif cmd == 'acc':
            acc += int(value)
            instruction += 1
        elif cmd == 'jmp':
            instruction += int(value)
        else:
            print(f"unknown command {cmd}")
        if instruction in visited:
            return acc, False
        if instruction >= len(instructions):
            return acc, True
        visited.append(instruction)

for i in range(len(instructions)):
    if instructions[i] == 'nop':
        ins_copy = instructions.copy()
        ins_copy[i][0] = 'jmp'
        acc, is_done = try_bootup(ins_copy)
        if is_done:
            print(acc)
    if instructions[i] == 'jmp':
        ins_copy = instructions.copy()
        ins_copy[i][0] = 'nop'
        acc, is_done = try_bootup(ins_copy)
        if is_done:
            print(acc)
