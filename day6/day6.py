file = open("input.txt","r")
lines = file.read().split("\n\n")
groups = [" ".join(lines.split("\n")).split(" ") for lines in lines]
del groups[-1][-1]
chars = "abcdefghijklmnopqrstuvwxyz"


val = [0 for i in range(len(groups))]
for i,group in enumerate(groups):
    group = "".join(group)
    for char in chars:
        if not(group.find(char)==-1):
            val[i] += 1
            
print(sum(val))


val2 = [0 for i in range(len(groups))]
for i,group in enumerate(groups):
    l = len(group)
    group = "".join(group)
    for char in chars:
        if group.count(char)==l:
            val2[i] += 1

print(sum(val2))    
            



