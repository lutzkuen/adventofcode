with open('input.txt', 'r') as f:
    passwords = [{'from': int(line.split('-')[0]), 'to': int(line.split('-')[1].split(' ')[0]), 'char': line.split(':')[0][-1], 'pass': line.split(': ')[1].replace('\n', '')} for line in f.readlines()]

def is_valid(pass_dict):
    num = 0
    try:
        num += pass_dict['pass'][pass_dict['from']-1].count(pass_dict['char'])
    except Exception as e:
        print(str(e))
    try:
        num += pass_dict['pass'][pass_dict['to']-1].count(pass_dict['char'])
    except Exception as e:
        print(str(e))
    print(pass_dict)
    print(num)
    if num == 1:
        return True
    return False

num_valids = len([pass_dict for pass_dict in passwords if is_valid(pass_dict)])
print(num_valids)

