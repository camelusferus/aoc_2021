file = open("input/input_02.txt")

horizontal = 0
depth = 0

for line in file.readlines():
    if line.split()[0] == "forward":
        horizontal = horizontal + int(line.split()[1])
    elif line.split()[0] == "down":
        depth = depth + int(line.split()[1])
    elif line.split()[0] == "up":
        depth = depth - int(line.split()[1])

res = horizontal * depth

print(res)