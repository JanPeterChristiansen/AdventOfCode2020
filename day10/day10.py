file = open("input.txt", "r")
adapters = file.read().split("\n")[: -1]
adapters = [int(val) for val in adapters]
adapters.sort()
adapters.insert(0, 0)
adapters.append(max(adapters)+3)

diff = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]

one_jolt = diff.count(1)
three_jolt = diff.count(3)
print("Answer to part I: "+str(one_jolt*three_jolt))
