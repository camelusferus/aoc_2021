input = [[int(field) for field in line if field.isdigit()] for line in open("input/input_09.txt").readlines()]
basins = []

for line in range(len(input)):
    for field in range(len(input[0])):
        if not field or input[line][field] < input[line][field - 1]:
            if not line or input[line][field] < input[line - 1][field]:
                if (len(input) - 1 == line) or input[line][field] < input[line + 1][field]:
                    if (len(input[0]) - 1 == field) or input[line][field] < input[line][field + 1]:
                        basin = [[False for a in range(len(input[0]))] for b in range(len(input))]
                        basin[line][field] = True
                        basins.append(basin)

for basin in range(len(basins)):
    change = True
    while change:
        change = False
        for line in range(len(input)):
            for field in range(len(input[0])):
                if basins[basin][line][field] or (input[line][field] == 9):
                    continue
                if (field and input[line][field] > input[line][field - 1] and basins[basin][line][field - 1]) \
                        or (line and input[line][field] > input[line - 1][field] and basins[basin][line - 1][field]) \
                        or (not (len(input[0]) - 1 == field) and input[line][field] > input[line][field + 1] and basins[basin][line][field + 1]) \
                        or (not (len(input) - 1 == line) and input[line][field] > input[line + 1][field] and basins[basin][line + 1][field]):
                    basins[basin][line][field] = True
                    change = True

result_basins = []
for x in basins:
    if x not in result_basins:
        result_basins.append(x)

sizes = sorted([len([field for fields in basin for field in fields if field]) for basin in result_basins], reverse=True)

print(str(sizes[0] * sizes[1] * sizes[2]))