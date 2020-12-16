
rules = dict()

with open("rules.txt", "r") as f:
    for line in f.readlines():
        rule_name = line.split(':')[0]
        rules[rule_name] = []
        for rng in line.split(':')[1].replace('\n', '').replace(' ', '').split('or'):
            low_value, high_value = rng.split('-')
            rules[rule_name].append({
                'low_value': int(low_value),
                'high_value': int(high_value),
            })

# print(rules)

with open("tickets.txt", "r") as f:
    tickets = [[int(line_part) for line_part in line.replace('\n', '').split(',')] for line in f.readlines()]

error_rate = 0
for ticket in tickets:
    for number in ticket:
        is_valid = False
        for rule in rules.keys():
            for rule_part in rules[rule]:
                if rule_part['low_value'] <= number <= rule_part['high_value']:
                    is_valid = True
                    break
            if is_valid:
                break
        if not is_valid:
            error_rate += number

print(error_rate)

