file = open("input.txt", "r")
lines = file.read().split("\n")
del lines[-1]
numbers = list(map(int, lines))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                a = numbers[i]
                b = numbers[j]
                c = numbers[k]
print(a, b, c, a+b+c)
