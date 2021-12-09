input = open("input/input_06.txt").read()

fishs = [int(number) for number in input.split(",")]

for days in range(80):
    for fish in range(len(fishs)):
        if fishs[fish]:
            fishs[fish] -= 1
        else:
            fishs[fish] = 6
            fishs.append(8)

print(len(fishs))