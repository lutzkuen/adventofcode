

groups = []

with open('input.txt', 'r') as f:
    group = ''
    for line in f.readlines():
        if line == '\n':
            groups.append(set(group.replace('\n', '')))
            group = ''
        else:
            group += line

# [print(len(group)) for group in groups]
print(sum([len(group) for group in groups]))
