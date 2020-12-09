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
    seat_ids = [seat_id for _, _, seat_id in [get_seat_position(line.replace('\n', '')) for line in f.readlines()]]

for seat_id in range(1,818):
    if seat_id not in seat_ids and seat_id-1 in seat_ids and seat_id+1 in seat_ids:
        print(f"Your seat is {int(seat_id/8)}, {seat_id%8} with id {seat_id}")
