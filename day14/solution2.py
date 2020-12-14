
import code

mem = dict()
mask = None

def get_range_from_string(new_address_bin):
    chars = list(new_address_bin)
    
    

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
            address_bin = bin(address)[2:]
            address_bin = address_bin[::-1]
            print(address_bin)
            print(mask)
            new_address_bins = ['']
            for i in range(len(mask)):
                if mask[i] == 'X':
                    new_addresses_to_append = []
                    for k in range(len(new_address_bins)):
                        new_address_copy = new_address_bins[k]
                        new_address_copy += '0'
                        new_addresses_to_append.append(new_address_copy)
                        new_address_bins[k] += '1'
                    new_address_bins += new_addresses_to_append
                elif mask[i] == '1':
                    for k in range(len(new_address_bins)):
                        new_address_bins[k] += '1'
                else:
                    for k in range(len(new_address_bins)):
                        if i < len(address_bin):
                            new_address_bins[k] += address_bin[i]
                        else:
                            new_address_bins[k] += '0'
            print(new_address_bins)
            for new_address_bin in new_address_bins:
                # print(new_address_bin)
                mem[int(new_address_bin[::-1], 2)] = value
                # print(mem[address])
            # code.interact(banner='', local=locals())

print(sum([mem[address] for address in mem.keys()]))

