
import regex
import code

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
    print(rule)
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
                if not regex.match('.*\d.*', rules[key]):
                    is_replaced = False
                    for other_key in rules.keys():
                        if other_key == key:
                            continue
                            # print(f"{key} -> {other_key}")
                        if has_key(rules[other_key], key):
                            # print(f"Replacing {key} {rules[key]}")
                            # code.interact(banner='', local=locals())
                            # print(rules[other_key])
                            # rules[other_key] = rules[other_key].replace(f" {key} ", f" {rules[key]} ")
                            rules[other_key] = replace_in_rule(rules[other_key], key, rules[key])
                            # print(rules[other_key])
                            if not regex.match('.*\d.*', rules[other_key]):
                                rules[other_key] = f"({rules[other_key].replace(' ', '')})"
                    replaced.append(key)
        # print(rules)
        for srule in [8, 11]:
            # get the rule number
            # rules[srule] = rules[srule].replace(str(srule), '(?1)')
            rules[srule] = f"({rules[srule].replace(' ', '')})"
            rules[0] = rules[0].replace(str(srule), rules[srule])
            # lpart, _ = rules[0].split(str(srule))
            # cnt = lpart.count('(')
            if srule == 8:
                cnt = 1
            else:
                cnt = 292
            rules[0] = rules[0].replace(str(srule), f"(?{cnt})")
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
                if regex.match(self.rerule, line.replace('\n', '')):
                    print(f"matching {line}")
                    matches += 1
                # else:
                #     print(line)
                #     code.interact(banner='', local=locals())
        return matches


# rd = RulesDict("test_input2.txt")
# 
# matches = rd.match_file("test_input2.txt")
# assert matches == 12

rdr = RulesDict("input2.txt")
print(rdr.match_file("input2.txt"))
