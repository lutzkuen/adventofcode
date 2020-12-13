
import code
import math

# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def extended_gcd(a, b):
    lcm = abs(a*b) # all the periods are prime
    old_r, r = a, -b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s % lcm, old_t % lcm

def combine_buses(per_1, per_2, offset_1, offset_2):
        lcm = per_1 * per_2
        gcd = extended_gcd(per_1, per_2)
        offset = offset_2 + offset_1
        print(f"{gcd[1]*per_2*offset % lcm} - {gcd[0]*per_1*offset % lcm} = {offset}")
        earliest_match = (offset_1 + gcd[0]*per_1*offset) % lcm
        # code.interact(banner='', local=locals())
        return lcm, earliest_match

def reduce_constraints(constraints):
    new_constraints = []
    for i in range(1, len(constraints)):
        new_constraints.append(combine_buses(constraints[0][0], constraints[i][0], constraints[0][1], constraints[i][1]))
    return new_constraints
    

with open("input.txt", "r") as f:
    start_ts, bus_lines, _ = f.read().split('\n')

constraints = [(int(bus_line), int(depart_offset) % int(bus_line)) for bus_line, depart_offset in zip(bus_lines.split(','), range(len(bus_lines.split(',')))) if bus_line != "x"]

print(constraints)

period = constraints[0][0]
offset = constraints[0][1]
start_ts = 0
coffs = 0

# print(reduce_constraints(constraints))
# constraints = reduce_constraints(constraints)
# print(reduce_constraints(constraints))

for i in range(1, len(constraints)):
    # coffs += offset * constraints[i][0]
    period, offset = combine_buses(period, constraints[i][0], offset, constraints[i][1])
    print(f"{period} {offset}")
    # code.interact(banner='', local=locals())
earliest_match = offset

for bus_line, departure in constraints:
    print(f"{bus_line} {departure} {(earliest_match + departure) % bus_line}")


# mult = 1
# for bus_line, _ in constraints:
#     mult *= bus_line
# 
# print(mult)
# nums = [29, 41]
# lcm = nums[0] * nums[1]
# mult = extended_gcd(nums[0], nums[1])
# print(mult[0]*nums[0]*19 % lcm)
# print(mult[1]*nums[1]*19 % lcm)
# print(mult)
# print((mult[1]*29 + mult[0]*41) % 29)
# print((mult[1]*29 + mult[0]*41) % 41)
# print(mult[1]*29 + mult[0]*41)

# start_ts = 0
# is_valid = False
# 
# while not is_valid:
#     is_valid = True
#     for bus_line, depart_offset in constraints:
#         if start_ts % bus_line != depart_offset:
#             is_valid = False
#             print(f"{start_ts} {depart_offset} {bus_line}")
#             start_ts = int(math.ceil((start_ts + depart_offset) / bus_line) * bus_line)
#             break
# 
# 
# print(start_ts)
