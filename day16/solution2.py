
import code

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

print(rules)

with open("tickets.txt", "r") as f:
    tickets = [[int(line_part) for line_part in line.replace('\n', '').split(',')] for line in f.readlines()]

valid_tickets = []
error_rate = 0
for ticket in tickets:
    ticket_valid = True
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
            ticket_valid = False
            break
    if ticket_valid:
        valid_tickets.append(ticket)

ordered_fields = []

departure_positions = []

rule_keys = list(rules.keys())

taken_positions = dict()
taken_pos_list = []

while len(taken_positions.keys()) < len(rules.keys()):
    # print(f"looking for candidates for {next_pos}")
    for try_key in rule_keys[::-1]:
        allowed_positions = []
        if try_key in taken_positions.keys():
            continue
        for try_position in range(len(rules.keys())):
            if try_position in taken_pos_list:
                continue
            # print(f"checking {try_key}")
            is_valid = True
            for ticket in valid_tickets:
                any_valid = False
                for rule in rules[try_key]:
                    if rule['low_value'] <= ticket[try_position] <= rule['high_value']:
                        any_valid = True
                if not any_valid:
                    # print(f"value {ticket[next_pos]} does not match rule {rule}. it was in {ticket}")
                    # code.interact(banner='', local=locals())
                    is_valid = False
                    break
                if is_valid == False:
                    break
            if is_valid:
                allowed_positions.append(try_position)
        if len(allowed_positions) == 1:
            next_pos = allowed_positions[0]
            taken_positions[try_key] = next_pos
            taken_pos_list.append(next_pos)
            if "departure" in try_key:
                departure_positions.append(next_pos)
            ordered_fields.append(try_key)
            print(taken_positions)
            break
        else:
            print(f"{try_key} saw {len(allowed_positions)} positions")

print(departure_positions)

with open("myticket.txt", "r") as f:
    myticket = [int(num) for num in f.read().replace('\n', '').split(',')]

mult = 1
for k in departure_positions:
    mult *= myticket[k]

print(mult)
