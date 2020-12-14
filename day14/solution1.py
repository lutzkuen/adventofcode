
import code

mem = dict()
mask = None

with open("input.txt", "r") as f:
    for line in f.readlines():
        if 'mask' in line:
            mask = line.split(' = ')[1].replace('\n', '')
            mask = mask[::-1]
        else:
            print(line)
            address, value = line.replace('\n', '').split(' = ')
            address = int(address.replace('mem[', '').replace(']', ''))
            value = int(value)
            value_bin = bin(value)[2:]
            value_bin = value_bin[::-1]
            print(value_bin)
            print(mask)
            new_value_bin = ''
            for i in range(len(mask)):
                if mask[i] == 'X':
                    if i < len(value_bin):
                        new_value_bin += value_bin[i]
                    else:
                        new_value_bin += '0'
                else:
                    new_value_bin += mask[i]
            print(new_value_bin)
            mem[address] = int(new_value_bin[::-1], 2)
            print(mem[address])
            # code.interact(banner='', local=locals())

print(sum([mem[address] for address in mem.keys()]))

