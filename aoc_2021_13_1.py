input = open("input/input_13.txt").read()

points = [[int(a.split(",")[0]),int(a.split(",")[1])] for a in input.split("\n\n")[0].split("\n")]
turns = [[a.split()[2].split("=")[0],int(a.split()[2].split("=")[1])] for a in input.split("\n\n")[1].split("\n")]

turn = turns[0]
for point in range(len(points)):
    if turn[0] == "x":
        if points[point][0] > turn[1]:
            points[point][0] = points[point][0] - (points[point][0] - turn[1])*2
    else:
        if points[point][1] > turn[1]:
            points[point][1] = points[point][1] - (points[point][1] - turn[1])*2

result_points = []
[result_points.append(x) for x in points if x not in result_points]

print(len(result_points))