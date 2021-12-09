input = [[int(field) for field in line if field.isdigit()] for line in open("input/input_09.txt").readlines()]

risk = 0

for line in range(len(input)):
    for field in range(len(input[line])):
        if not field or input[line][field] < input[line][field - 1]:
            if not line or input[line][field] < input[line - 1][field]:
                if (len(input) - 1 == line) or input[line][field] < input[line + 1][field]:
                    if (len(input[line]) - 1 == field) or input[line][field] < input[line][field + 1]:
                        risk += 1 + input[line][field]

print(risk)