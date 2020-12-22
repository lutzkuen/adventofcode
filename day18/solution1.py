
import code

def eval_line(line):
    print(line)
    if '(' in line:
        # as long as there are brackets we need to split first
        lb = -1
        rb = -1
        leftpart = ''
        inner = ''
        bopen = False
        bdone = False
        for c in line:
            if c == '(' and not bdone:
                if bopen:
                    leftpart += '(' + inner
                    inner = ''
                bopen = True
            elif c == ')' and bopen == True and not bdone:
                bdone = True
                # print('eval inner part')
                # code.interact(banner='', local=locals())
                leftpart += eval_line(inner)
            elif bopen == True and not bdone:
                inner += c
            else:
                leftpart += c
        return eval_line(leftpart)
    else:
        # only arithmetics left, do the thing
        res = None
        op_buffer = ''
        first_num = True
        next_op = None
        # print("eval easy part")
        # code.interact(banner='', local=locals())
        for c in line:
            # code.interact(banner='', local=locals())
            if c == '+':
                if next_op:
                    print(f"{res} {next_op} {op_buffer}")
                    res = eval(str(res) + next_op + op_buffer)
                else:
                    res = int(op_buffer)
                op_buffer = ''
                next_op = '+'
            elif c == '*':
                if next_op:
                    print(f"{res} {next_op} {op_buffer}")
                    res = eval(str(res) + next_op + op_buffer)
                else:
                    res = int(op_buffer)
                op_buffer = ''
                next_op = '*'
            else:
                op_buffer += c
                # print(f"{res} {next_op} {c}")
                # if next_op == '+':
                #     res += int(c)
                # elif next_op == '*':
                #     # print(c)
                #     res *= int(c)
        # print(f"{res} {next_op} {op_buffer}")
        res = eval(str(res) + next_op + op_buffer)
        # print(res)
        # code.interact(banner='', local=locals())
        return str(res).replace(' ', '')


test_line = '2+3*(2+2)'

assert int(eval_line(test_line)) == 20

test_line = '2+3*((2+2)+3)'

assert int(eval_line(test_line)) == 35

print(int(eval_line(test_line)))
test_line = '2*3+(4*5)'
assert int(eval_line(test_line)) == 26

test_line = '5+(8*3+9+3*4*3)'
assert int(eval_line(test_line)) == 437

test_line = '5*9*(7*3*3+9*3+(8+6*4))'
assert int(eval_line(test_line)) == 12240

test_line = '((2+4*9)*(6+9*8+6)+6)+2+4*2'
assert int(eval_line(test_line)) == 13632

res_sum = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        res_sum += int(eval_line(line.replace('\n', '').replace(' ', '')))
print(res_sum)

