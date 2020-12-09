import code

passports = []

with open('input.txt', 'r') as f:
    passport = dict()
    for line in f.readlines():
        if line == '\n':
            passports.append(passport)
            passport = dict()
        else:
            for key, value in [pair.split(':') for pair in line.replace('\n', '').split(' ')]:
                passport[key] = value

REQUIRED_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
]

def is_valid(passport):
    for field  in REQUIRED_FIELDS:
        if field not in passport.keys():
            return False
    print(passport)
    return True

# code.interact(banner='', local=locals())

print(len([passport for passport in passports if is_valid(passport)]))

