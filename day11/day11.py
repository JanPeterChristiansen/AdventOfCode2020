from copy import deepcopy

file = open("input.txt", "r")
rows = file.read().split("\n")[:-1]
seats = [[seat for seat in row] for row in rows]
seats.append(["."]*len(seats[0]))
seats.insert(0, ["."]*len(seats[0]))
for i in range(len(seats)):
    seats[i].insert(0, ".")
    seats[i].append(".")

# %% Part I


def change_seats(seats):
    new_seats = deepcopy(seats)
    changes = 0
    for i in range(1, len(seats)):
        for j in range(1, len(seats[0])):
            if not seats[i][j] == ".":  # if not floor
                if seats[i][j] == "L":  # empty

                    if seats[i][j-1:j+2].count("#") + seats[i-1][j-1:j+2].count("#") + seats[i+1][j-1:j+2].count("#") == 0:
                        new_seats[i][j] = "#"
                        changes += 1

                elif seats[i][j] == "#":  # occupied

                    if seats[i][j-1].count("#") + seats[i][j+1].count("#") + seats[i-1][j-1:j+2].count("#") + seats[i+1][j-1:j+2].count("#") >= 4:
                        new_seats[i][j] = "L"
                        changes += 1

    return new_seats, changes


new_seats, changes = change_seats(seats)
while changes > 0:
    new_seats, changes = change_seats(new_seats)
    print(changes)

print("Answer to part I: "+str(sum([row.count("#") for row in new_seats])))

# %% Part II


def change_seats_part2(seats):
    new_seats = deepcopy(seats)
    changes = 0

    for i in range(1, len(seats)):
        for j in range(1, len(seats[0])):
            if not seats[i][j] == ".":  # if not floor
                if seats[i][j] == "L":  # empty

                    pass
                    # check line of sight == 0

                elif seats[i][j] == "#":  # occupied

                    pass
                    # check line of sight >= 5

    return new_seats, changes


def line_of_sight(seats, pos, direction):
    # pos: position tuple [x,y]
    # directions: 0=up, 1=upright, 2=right, 3=downright,
    #             4=down, 5=downleft, 6=left, 7=upleft
    x = pos[0]
    y = pos[1]
    N = len(seats)  # number of rows
    M = len(seats[0])  # number of columns
    occupied = False
    if direction == 0:
        for i in range(1, x):
            if seats[x-i][y] == "#":
                occupied = True
    elif direction == 1:
        for i in range(1, N-x):
            for j in range(1, M-y):
                if i == j:
                    if seats[x+i][y+j] == "#":
                        occupied = True
    elif direction == 2:
        for i in range(1, M-x):
            if seats[x][y+i]:
                occupied = True
    elif direction == 3:
        pass
    elif direction == 4:
        pass
    elif direction == 5:
        pass
    elif direction == 6:
        pass
    elif direction == 7:
        pass

    return occupied
