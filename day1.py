data = []
for line in open('input.txt', 'r').readlines():
    data.append(line.strip())

## Part 1
for i in range(len(data)):
    for j in range(len(data)):
        if (int(data[i]) + int(data[j])) == 2020:
            print("Product of two entries whose sum is 2020:")
            print(int(data[i]) * int(data[j]))

## Part 2
for i in range(len(data)):
    for j in range(len(data)):
        if (int(data[i]) + int(data[j])) > 2020:
            continue
        for k in range(len(data)):
            if (int(data[i]) + int(data[j]) + int(data[k])) == 2020:
                print("Product of three entries whose sum is 2020:")
                print(int(data[i]) * int(data[j]) * int(data[k]))