

groups = []

with open('input.txt', 'r') as f:
    group = None
    is_new = True
    text = ''
    for line in f.readlines():
        if line == '\n':
            groups.append(group)
            print(text)
            print(group)
            print(len(group))
            print('--------------------------------------')
            group = None
            is_new = True
            text = ''
        else:
            text += line
            if is_new:
                group = set(line.replace('\n', ''))
                is_new = False
            else:
                group = group.intersection(set(line.replace('\n', '')))

# [print(len(group)) for group in groups]
print(sum([len(group) for group in groups]))

