from collections import defaultdict

file = open("input.txt", "r")
adapters = file.read().split("\n")[: -1]
adapters = [int(val) for val in adapters]
adapters.sort()
adapters.insert(0, 0)
adapters.append(max(adapters)+3)


# %%


difference = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]
print("Answer to part I: "+str(difference.count(1)*difference.count(3)))

# %% Copied from viliampucik
# https://github.com/viliampucik/adventofcode/blob/master/2020/10.py

# the only way to reach the next adapter is by using one that has a value
# at most 3 less than the one you try to reach.

# thus make an ordered list of ways to reach each value, starting at the first value
# the way to reach the next adapter is the sum of the ways to reach the previous 3

counts = defaultdict(int, {0: 1})
for a in adapters[1:]:
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

print("Answer to part II: "+str(counts[adapters[-1]]))
