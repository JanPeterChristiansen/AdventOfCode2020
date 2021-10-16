import re
file = open("input.txt", "r")
lines = file.read().split("\n\n")
PassPorts = [" ".join(lines.split("\n")).split(" ") for lines in lines]
del PassPorts[-1][-1]


def validation(Pass):
    valid = -7
    reg1 = re.compile("[0-9a-f]")
    reg2 = re.compile("[0-9]")
    for element in Pass:
        ID = element.split(":")[0]
        value = element.split(":")[1]
        if ID == "byr" and len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
            valid += 1
        elif ID == "iyr" and len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
            valid += 1
        elif ID == "eyr" and len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
            valid += 1
        elif ID == "hgt":
            if value[-2::] == "cm" and int(value[0:-2]) >= 150 and int(value[0:-2]) <= 193:
                valid += 1
            elif value[-2::] == "in" and int(value[0:-2]) >= 59 and int(value[0:-2]) <= 76:
                valid += 1
        elif ID == "hcl" and value[0] == "#" and len(value) == 7:
            if reg1.match(value[1::]):
                valid += 1
        elif ID == "ecl" and (value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"):
            valid += 1
        elif ID == "pid" and len(value) == 9:
            if reg2.match(value):
                valid += 1
    if valid == 0:
        return 1
    else:
        return 0


valid = 0
for Pass in PassPorts:
    if len(Pass) == 8:
        valid += validation(Pass)
    elif len(Pass) == 7:
        cid = 0
        for element in Pass:
            cid += element.find("cid")+1
        if cid == 0:
            valid += validation(Pass)
