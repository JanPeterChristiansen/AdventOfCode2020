file = open("input.txt", "r")
lines = file.read().split("\n")
del lines[-1]

row = [i for i in range(128)]
column = [i for i in range(8)]
rows = [row for i in range(len(lines))]
columns = [column for i in range(len(lines))]


def split(arr, m):
    if m == "F" or m == "L":
        return arr[:len(arr)//2]
    elif m == "B" or m == "R":
        return arr[len(arr)//2::]


for i in range(len(lines)):
    for j in range(7):
        rows[i] = split(rows[i], lines[i][j])
    for k in range(3):
        columns[i] = split(columns[i], lines[i][k+7])

rows = list(map(lambda s: s[0], rows))
columns = list(map(lambda s: s[0], columns))
seatID = [rows[i]*8+columns[i] for i in range(len(lines))]
print(max(seatID))


seatID.sort()
for i in range(len(seatID)-1):
    if not(seatID[i]+1 == seatID[i+1]):
        MySeatID = seatID[i]+1

print(MySeatID)
