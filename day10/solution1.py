
import numpy as np

with open('input.txt', 'r') as f:
    jolts = np.array(sorted([int(line.replace('\n', '')) for line in f.readlines()]))

diffs = np.append(jolts[1:] - jolts[:-1], [jolts[0], 3])

print(diffs)

print(sum(diffs == 1)*sum(diffs == 3))
