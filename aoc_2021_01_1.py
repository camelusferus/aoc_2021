file = open("input/input_01.txt")

old = sum([int(number) for number in file.readlines()])
increments = 0

for line in file.readlines():
    new = int(line)
    if (new > old):
        increments = increments + 1
    old = new

print(increments)
