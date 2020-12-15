
with open("input.txt", "r") as f:
    numbers = f.read().replace('\n', '').split(',')


spoken = [int(num) for num in numbers[::-1]]

while len(spoken) < 2020:
    last_number = spoken[0]
    try:
        prev_occurence = spoken[1:].index(last_number)+1
    except Exception as e:
        prev_occurence = 0
    spoken.insert(0, prev_occurence)

print(spoken)

