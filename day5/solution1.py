test_string = 'FBFBBFFRLR'

def get_seat_position(seat_code):
    row = 0
    for i in range(7):
        if seat_code[6-i] == 'B':
            row += 2**i
    seat = 0
    for i in range(3):
        if seat_code[9-i] == 'R':
            seat += 2**i
    seat_id = row * 8 + seat
    return row, seat, seat_id

print(get_seat_position(test_string))

with open('input.txt', 'r') as f:
    print(max([seat_id for row, seat, seat_id in [get_seat_position(line.replace('\n', '')) for line in f.readlines()]]))
