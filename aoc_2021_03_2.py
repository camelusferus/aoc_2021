lines = open("input/input_03.txt").readlines()

oxygen_lines = lines
co2_lines = lines

line_length = len(lines[0])-1

# oxygen
for i in range(line_length):
    count = 0
    for line in oxygen_lines:
        count = count + (int(line[i]) * 2 - 1)

    if count < 0:
        oxygen_lines = [line for line in oxygen_lines if not int(line[i])]
    else:
        oxygen_lines = [line for line in oxygen_lines if int(line[i])]

    if not len(oxygen_lines) - 1:
        break

# CO2
for i in range(line_length):
    count = 0
    for line in co2_lines:
        count = count + (int(line[i]) * 2 - 1)

    if count < 0:
        co2_lines = [line for line in co2_lines if int(line[i])]
    else:
        co2_lines = [line for line in co2_lines if not int(line[i])]

    if not len(co2_lines) - 1:
        break

print(str(int(oxygen_lines[0],2)*int(co2_lines[0],2)))
