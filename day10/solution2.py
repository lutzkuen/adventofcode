
import numpy as np
import code

with open('input.txt', 'r') as f:
    JOLTS = sorted([int(line.replace('\n', '')) for line in f.readlines()])

TABLET_JOLT = max(JOLTS)

print(JOLTS)
DIFFS = ''.join([str(i) for i in [JOLTS[0]] + [i-j for i, j in zip(JOLTS[1:], JOLTS[:-1])] + [3]]).split('3')
print(DIFFS)
print(max([len(part) for part in DIFFS]))
print([len(part) for part in DIFFS])

def combinations_by_len(l):
    if l == 0:
        return 1
    if l == 1:
        return 1
    if l == 2:
        return 2
    if l == 3:
        return 4
    if l == 4:
        return 7
    if l == 5:
        return 12

m = 1
for part in DIFFS:
    m *= combinations_by_len(len(part))

print(m)

