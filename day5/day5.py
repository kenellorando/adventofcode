import math

data = []
for line in open("input.txt", 'r').readlines():
    data.append(line.strip())

# Part 1
manifest = []
row, column = 0, 0
for assignment in data:
    upper, lower = 127, 0
    for character in assignment[0:6]:
        if character == "F":
            upper = (upper - lower) // 2 + lower
        if character == "B":
            lower = (upper - lower + 1) // 2 + lower
    for character in assignment[6]:
        if character == "F":
            row = lower
        if character == "B":
            row = upper   

    upper, lower = 7, 0
    for character in assignment[7:9]:
        if character == "L":
            upper = (upper - lower) // 2 + lower
        if character == "R":
            lower = (upper - lower + 1) // 2 + lower
    for character in assignment[9]:
        if character == "L":
            column = lower
        if character == "R":
            column = upper  

    manifest.append((row*8)+column)
print("Part 1", sorted(manifest)[-1])

# Part 2
for i in range(len(manifest[1:len(manifest)-1])):
    if sorted(manifest)[i+1] != sorted(manifest)[i] + 1:
        print("Part 2", sorted(manifest)[i]+1)
