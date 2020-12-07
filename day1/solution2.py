with open('input.txt', 'r') as f:
    numbers = [int(line.replace('\n', '')) for line in f.readlines()]

print(numbers)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(len(numbers)):
            if i == k:
                continue
            if j == k:
                continue
            if numbers[k] + numbers[i] + numbers[j] == 2020:
                print(f"{numbers[i]} {numbers[j]} {numbers[k]} {numbers[i]*numbers[j]*numbers[k]}")
