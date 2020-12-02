data = []
for line in open("input.txt", 'r').readlines():
    data.append(line.strip())

## Part 1
valid = 0
for i in range(len(data)):
    minimum = int(data[i].split(':', 2)[0].split(' ', 2)[0].split('-',2)[0])
    maximum = int(data[i].split(':', 2)[0].split(' ', 2)[0].split('-',2)[1].strip())
    character = data[i].split(':', 2)[0].split(' ', 1)[1].strip()
    password = data[i].split(':', 2)[1].strip()

    if password.count(character) >= minimum and password.count(character) <= maximum:
        valid += 1

print(valid)


## Part 2
valid = 0
for i in range(len(data)):
    firstPosition = int(data[i].split(':', 2)[0].split(' ', 2)[0].split('-',2)[0])
    secondPosition = int(data[i].split(':', 2)[0].split(' ', 2)[0].split('-',2)[1].strip())
    character = data[i].split(':', 2)[0].split(' ', 1)[1].strip()
    password = data[i].split(':', 2)[1].strip()

    if password[firstPosition-1] == character or password[secondPosition-1] == character:
        if password[firstPosition-1] == character and password[secondPosition-1] == character:
            continue
        valid += 1

print(valid)