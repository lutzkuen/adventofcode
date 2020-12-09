
def get_instructions():
    instructions = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            instructions.append(line.replace('\n', '').replace('+', '').split(' '))
    return instructions

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
            # print(f"inf loop at {acc} {instruction}")
            return acc, False
        if instruction >= len(instructions):
            return acc, True
        visited.append(instruction)

instructions = get_instructions()

print(try_bootup(instructions))
for i in range(len(instructions)):
    instructions = get_instructions()
    if instructions[i][0] == 'nop':
        ins_copy = instructions.copy()
        ins_copy[i][0] = 'jmp'
        acc, is_done = try_bootup(ins_copy)
        if is_done:
            print(acc)
    if instructions[i][0] == 'jmp':
        ins_copy = instructions.copy()
        ins_copy[i][0] = 'nop'
        acc, is_done = try_bootup(ins_copy)
        if is_done:
            print(acc)
