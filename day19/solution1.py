
import re

def replace_in_rule(rule, key, value):
    if '||' in rule:
        lpart, rpart = rule.split('||')
        outrule = f"{replace_in_rule(lpart, key, value)} | {replace_in_rule(rpart, key, value)}"
    else:
        outrule = ''
        for num in rule.split(' '):
            if str(key) == num:
                outrule += f" {value}"
            else:
                outrule += f" {num}"
        outrule = outrule[1:]
    return outrule

def has_key(rule, key):
    if '||' in rule:
        lpart, rpart = rule.split('||')
        return has_key(lpart, key) or has_key(rpart, key)
    else:
        for part in rule.split(' '):
            if part == str(key):
                return True
    return False

class RulesDict:
    def __init__(self, filename):
        rules = dict()
        with open(filename, "r") as f:
            for line in f.readlines():
                if len(line) < 2:
                    continue
                if line[1] not in ["a", "b"]:
                    rule_num = int(line.split(':')[0])
                    rule_val = line.split(':')[1].replace('\n', '')
                    rules[rule_num] = rule_val.replace('"', '').replace('|', '||')

        is_replaced = False
        replaced = []
        while not is_replaced:
            # first find a rule that has no references anymore
            is_replaced = True
            for key in rules.keys():
                if key in replaced:
                    continue
                if not re.search('\d', rules[key]):
                    is_replaced = False
                    for other_key in rules.keys():
                        if other_key == key:
                            continue
                        print(f"{key} -> {other_key}")
                        if has_key(rules[other_key], key):
                            print(f"Replacing {key} {rules[key]}")
                            print(rules[other_key])
                            # rules[other_key] = rules[other_key].replace(f" {key} ", f" {rules[key]} ")
                            rules[other_key] = replace_in_rule(rules[other_key], key, rules[key])
                            print(rules[other_key])
                            if not re.search('\d', rules[other_key]):
                                rules[other_key] = f"({rules[other_key].replace(' ', '')})"
                    replaced.append(key)
        print(rules)
        self.rerule = f"^{rules[0].replace(' ', '')}$"
        print(self.rerule)

    def match_file(self, filename):
        matches = 0
        with open(filename, "r") as f:
            for line in f.readlines():
                if len(line) < 2:
                    continue
                if line[1] not in ["a", "b"]:
                    continue
                if re.search(self.rerule, line.replace('\n', '')):
                    print(f"matching {line}")
                    matches += 1
        return matches


rd = RulesDict("test_input.txt")

matches = rd.match_file("test_input.txt")
assert matches == 2

rdr = RulesDict("input.txt")
print(rdr.match_file("input.txt"))
