import code
import re

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
    if not ( 1920 <= int(passport['byr']) <= 2002 ):
        return False
    if not ( 2010 <= int(passport['iyr']) <= 2020 ):
        return False
    if not ( 2020 <= int(passport['eyr']) <= 2030 ):
        return False
    if passport['hgt'][-2:] not in ['cm', 'in']:
        return False
    if passport['hgt'][-2:] == 'cm':
        if not ( 150 <= int(passport['hgt'][:-2]) <= 193 ):
            return False
    if passport['hgt'][-2:] == 'in':
        if not ( 59 <= int(passport['hgt'][:-2]) <= 76 ):
            return False
    if not re.search('^#[0-9a-f]{6}$', passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.search('^[0-9]{9}$', passport['pid']):
        return False
    print(passport)
    return True

# code.interact(banner='', local=locals())

print(len([passport for passport in passports if is_valid(passport)]))

