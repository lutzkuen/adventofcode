
bag_rules = dict()

def get_containing_bags(bag_rules, bag_name):
    containing_bags = []
    for bag_rule in bag_rules.keys():
        # print([bag_name for _, bag_name in bag_rules[bag_rule]])
        if bag_name in [bag_name for _, bag_name in bag_rules[bag_rule]]:
            print(f"{bag_rule} {bag_rules[bag_rule]}")
            containing_bags.append(bag_rule)
            containing_bags += get_containing_bags(bag_rules, bag_rule)
    return containing_bags
        

with open('input.txt', 'r') as f:
    for line in f.readlines():
        holding_bag, holded_bags = line.replace('.\n', '').replace('bags', 'bag').split(' contain ')
        if holding_bag in bag_rules.keys():
            raise Exception('Duplicate rule')
        bag_rules[holding_bag] = [(count, bag_name) for count, bag_name in [(part.split(' ')[0], ' '.join(part.split(' ')[1:])) for part in holded_bags.split(', ')]]

print(len(set(get_containing_bags(bag_rules, 'shiny gold bag'))))
