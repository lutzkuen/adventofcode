with open('input.txt', 'r') as f:
    numbers = [int(line.replace('\n', '')) for line in f.readlines()]

print(numbers)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(f"{numbers[i]} {numbers[j]} {numbers[i]*numbers[j]}")
