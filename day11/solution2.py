
import code

with open("input.txt", "r") as f:
    seats = [list(line.replace('\n', '')) for line in f.readlines()]
print(''.join([''.join(seat_row) for seat_row in seats]).count('L'))

def count_characters(seats, i, j, ch):
    cnt = 0
    for dir_i in [-1, 0, 1]:
        for dir_j in [-1, 0, 1]:
            if dir_j == dir_i == 0:
                continue
            pos_i = i + dir_i
            pos_j = j + dir_j
            while True:
                if not (( 0 <= pos_i < len(seats)) and ( 0 <= pos_j < len(seats[0]))):
                    break
                if seats[pos_i][pos_j] == ch:
                    cnt += 1
                    break
                if seats[pos_i][pos_j] in ['L', '#']:
                    break
                pos_i += dir_i
                pos_j += dir_j
    return cnt

def do_step(seats):
    new_seats = [seat.copy() for seat in seats]
    change = False
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == '.':
                continue
            if seats[i][j] == 'L':
                if count_characters(seats, i, j, '#') == 0:
                    new_seats[i][j] = '#'
                    change = True
            if seats[i][j] == '#':
                # code.interact(banner='', local=locals())
                if count_characters(seats, i, j, '#') >= 5:
                    new_seats[i][j] = 'L'
                    change = True
    return new_seats, change

change = True
iteration = 0

while change:
    print(iteration)
    iteration += 1
    seats, change = do_step(seats)

print(''.join([''.join(seat_row) for seat_row in seats]).count('#'))
