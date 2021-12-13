input = open("input/input_13.txt").read()

points = [[int(a.split(",")[0]),int(a.split(",")[1])] for a in input.split("\n\n")[0].split("\n")]
turns = [[a.split()[2].split("=")[0],int(a.split()[2].split("=")[1])] for a in input.split("\n\n")[1].split("\n")]

for turn in turns:
    max_x = max_y = 0
    for point in range(len(points)):
        if turn[0] == "x":
            if points[point][0] > turn[1]:
                points[point][0] = points[point][0] - (points[point][0] - turn[1])*2
        else:
            if points[point][1] > turn[1]:
                points[point][1] = points[point][1] - (points[point][1] - turn[1])*2
        if points[point][0] > max_x:
            max_x = points[point][0]
        if points[point][1] > max_y:
            max_y = points[point][1]

for y in range(max_y + 1):
    print("".join(["█" if [x,y] in points else " " for x in range(max_x + 1)]))
