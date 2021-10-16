import math as m

file = open("input.txt","r")
tiles = file.read().split("\n")
del tiles[-1]

slope = [3, 1]
N = len(tiles)
M = len(tiles[0])
crash = [0,0,0,0,0]

for i in range(N):
    if tiles[i][(3*i)%M] == "#":
        crash[0] += 1

for i in range(N):
    if tiles[i][i%M] == '#':
        crash[1] += 1
        
for i in range(N):
    if tiles[i][(5*i)%M] == '#':
        crash[2] += 1
        
for i in range(N):
    if tiles[i][(7*i)%M] == '#':
        crash[3] += 1

for i in range(0,N,2):
    if tiles[i][m.floor((1/2*i)%M)] == '#':
        crash[4] += 1

print(crash)
print(m.prod(crash))