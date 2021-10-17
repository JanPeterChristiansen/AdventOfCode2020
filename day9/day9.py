file = open("input.txt", "r")
numbers = file.read().split("\n")[0:-1]
numbers = [int(number) for number in numbers]

# %% part I


index = 25
while index < len(numbers):
    next_number = numbers[index]
    window = numbers[index-25:index]

    possible_numbers = []
    for i in range(len(window)-1):
        for j in range(i+1, len(window)):
            possible_numbers.append(window[i]+window[j])
    if next_number not in possible_numbers:
        break
    else:
        index += 1

print("Answer to part I: "+str(next_number))

# %% part II

invalid_number = next_number
index = 0
while index < len(numbers):
    j = index
    window = numbers[index:j]
    while sum(window) < invalid_number:
        j += 1
        window = numbers[index:j]
    if sum(window) == invalid_number:
        break
    else:
        index += 1

print("Answer for part II: "+str(max(window)+min(window)))
