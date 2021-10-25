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
# rules apply simultaneously


def change_seats(seats):
    new_seats = deepcopy(seats)
    changes = 0
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if not seat == ".":  # if not floor
                if seat == "L":  # empty

                    if seats[i][j-2:j+1].count("#") + seats[i-1][j-2:j+1].count("#") + seats[i+1][j-2:j+1].count("#") == 0:
                        new_seats[i][j] = "#"
                        changes += 1

                elif seat == "#":  # occupied

                    if seats[i][j-2:j+1].count("#") + seats[i-1][j-2:j+1].count("#") + seats[i+1][j-2:j+1].count("#") >= 4:
                        new_seats[i][j] = "L"
                        changes += 1

    return new_seats, changes


new_seats, changes = change_seats(seats)
while changes > 0:
    new_seats, changes = change_seats(new_seats)

print("Answer to part I: "+str(sum([row.count("#") for row in new_seats])))
