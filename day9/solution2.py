import itertools

with open('input.txt', 'r') as f:
    numbers = [int(line.replace('\n', '')) for line in f.readlines()]

for i in range(25, len(numbers)):
    if numbers[i] not in [i+j for i, j in itertools.product(numbers[(i-25):i], numbers[(i-25):i])]:
        print(f"{i} {numbers[i]}")
        target_number = numbers[i]
        break

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if target_number == sum(numbers[i:j]):
            print(f"{min(numbers[i:j]) + max(numbers[i:j])}")
