file = open("input.txt","r")
lines = file.read().split("\n")
del lines[-1]

lower = []
upper = []
id = []
password = []

for i,val in enumerate(lines):
    lower.append(val.split("-")[0])
    upper.append(val.split(" ")[0])
    id.append(val.split(": ")[0])
    password.append(val.split(": ")[1])

for i,val in enumerate(upper):
    upper[i] = val.split("-")[1]
    
for i,val in enumerate((id)):
    id[i] = val.split(" ")[1]

lower = list(map(int,lower))
upper = list(map(int,upper))
    
valid = []

for i,val in enumerate(password):
    nr = val.count(id[i])
    if nr >= lower[i] and nr <= upper[i]:
        valid.append(1)
    else:
        valid.append(0)
        
print(sum(valid))

valid2 = []
for i,val in enumerate(password):
    one = val[lower[i]-1]
    two = val[upper[i]-1]
    
    if (one==id[i]) ^ (two==id[i]):
        valid2.append(1)
    else:
        valid2.append(0)
        
print(sum(valid2))