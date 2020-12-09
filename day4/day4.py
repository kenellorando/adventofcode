import re

data = []
for line in open("input.txt", 'r').readlines():
    data.append(line.strip())

fields = ['byr', 'iyr', 'eyr', 'hcl', 'ecl', 'pid', 'hgt']
passport = ""
count = 0

## Part 1

for i in range(len(data)):
    passport += data[i]
    if i+1 < len(data):
        if data[i+1] == "":
            valid = 0
            for field in fields:
                if field in passport:
                    valid += 1
            if valid == 7:
                count += 1
            passport = ""
    else: 
        valid = 0
        for field in fields:
            if field in passport:
                valid += 1
        if valid == 7:
            count += 1
        passport = ""

print("Part 1", count)


## Part 2
count = 0

def validate(passport):
    global count
    passport = passport.strip().split(' ')
    verified = 0
    for field in passport:
        check = field.split(':', 1)
        if check[0] == 'byr':
            if int(check[1]) >= 1920 and int(check[1]) <= 2002:
                verified += 1
        if check[0] == 'iyr':
            if int(check[1]) >= 2010 and int(check[1]) <= 2020:
                verified += 1
        if check[0] == 'eyr':
            if int(check[1]) >= 2020 and int(check[1]) <= 2030:
                verified += 1
        if check[0] == 'hgt':
            if "cm" in check[1]:
                if int(check[1].strip('cm')) >= 150 and int(check[1].strip('cm')) <= 193:
                    verified += 1
            if "in" in check[1]:
                if int(check[1].strip('in')) >= 59 and int(check[1].strip('in')) <= 76:
                    verified += 1
        if check[0] == 'hcl':
            if check[1][0] == "#":
                if re.match("[a-z0-9]*$", check[1].strip("#")):
                    verified += 1
        if check[0] == 'ecl':
            colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if check[1] in colors:
                verified += 1
        if check[0] == 'pid':
            if len(check[1]) == 9:
                verified += 1

    if verified == 7:
        count += 1


for i in range(len(data)):
    passport += data[i] + " "
    if i+1 < len(data):
        if data[i+1] == "":
            valid = 0
            for field in fields:
                if field in passport:
                    valid += 1
            if valid == 7:
                validate(passport)
            passport = ""
    else: 
        valid = 0
        for field in fields:
            if field in passport:
                valid += 1
        if valid == 7:
            validate(passport)
        passport = ""

print("Part 2", count)