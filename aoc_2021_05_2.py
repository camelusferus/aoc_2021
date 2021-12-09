input = open("input/input_05.txt").readlines()

field = {}

for line in input:
    start_x = int(line.split()[0].split(",")[0])
    start_y = int(line.split()[0].split(",")[1])
    end_x = int(line.split()[2].split(",")[0])
    end_y = int(line.split()[2].split(",")[1])
    if start_x == end_x or start_y == end_y:
        if start_x > end_x or start_y > end_y:
            start_x, end_x, start_y, end_y = end_x, start_x, end_y, start_y
        for (x, y) in ((x, y) for x in range(start_x, end_x + 1) for y in range(start_y, end_y + 1)):
            if (str(x) + "," + str(y)) in field.keys():
                field[str(x) + "," + str(y)] += 1
            else:
                field[str(x) + "," + str(y)] = 1
    elif abs(end_y - start_y) == abs(end_x - start_x):
        if start_x > end_x:
            start_x, end_x, start_y, end_y = end_x, start_x, end_y, start_y
        for (x,y) in [(start_x + a, start_y + a * (end_y - start_y) // (end_x - start_x)) for a in range(end_x - start_x + 1)]:
            if (str(x) + "," + str(y)) in field.keys():
                field[str(x) + "," + str(y)] += 1
            else:
                field[str(x) + "," + str(y)] = 1

print(sum([1 for point in field if field[point] > 1]))
