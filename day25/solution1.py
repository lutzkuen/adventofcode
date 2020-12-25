TEST_CARD = 5764801
TEST_DOOR = 17807724

CARD = 1717001
DOOR = 523731

MOD = 20201227

def solve_duo(card, door, mod):
    card_mult = 0
    card_check = 1
    while card_check != card:
        card_check *= 7
        card_check %= mod
        card_mult += 1
    door_mult = 0
    door_check = 1
    while door_check != door:
        door_check *= 7
        door_check %= mod
        door_mult += 1
    ec = 1
    for _ in range(door_mult):
        ec *= card
        ec %= mod
    ec_check = 1
    for _ in range(card_mult):
        ec_check *= door
        ec_check %= mod
    assert ec == ec_check
    return card_mult, door_mult, ec


cm, dm, ec = solve_duo(TEST_CARD, TEST_DOOR, MOD)

print(f"{cm} {dm} {ec}")
assert cm == 8
assert dm == 11
assert ec == 14897079

print(solve_duo(CARD, DOOR, MOD))
