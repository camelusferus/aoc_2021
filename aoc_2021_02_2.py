file = open("input/input_02.txt")

horizontal = 0
depth = 0
aim = 0

for line in file.readlines():
    if line.split()[0] == "forward":
        horizontal = horizontal + int(line.split()[1])
        depth = depth + aim * int(line.split()[1])
    elif line.split()[0] == "down":
        aim = aim + int(line.split()[1])
    elif line.split()[0] == "up":
        aim = aim - int(line.split()[1])

res = horizontal * depth

print(res)