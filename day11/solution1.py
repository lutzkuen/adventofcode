
import code

with open("input.txt", "r") as f:
    seats = [list(line.replace('\n', '')) for line in f.readlines()]
print(''.join([''.join(seat_row) for seat_row in seats]).count('L'))

def count_characters(seats, i, j, ch):
    cnt = 0
    for ii in range(max(i-1, 0), min(i+2, len(seats))):
        for jj in range(max(j-1, 0), min(j+2, len(seats[0]))):
            if ii == i and jj == j:
                continue
            if seats[ii][jj] == ch:
                cnt += 1
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
                if count_characters(seats, i, j, '#') >= 4:
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
