input = open("input/input_11.txt").readlines()

flashes = 0

board = [[{"energy": int(field), "flashed": False} for field in line if field.isdigit()] for line in input]

neighbors = lambda x_base, y_base: [[x_neigh, y_neigh] for x_neigh in range(x_base - 1, x_base + 2) for y_neigh in range(y_base - 1, y_base + 2)
                                    if ((x_base != x_neigh or y_base != y_neigh) and
                                        (0 <= x_neigh < len(board[0])) and (0 <= y_neigh < len(board)))]

for step in range(100):
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[x][y]["energy"] += 1

    change = True
    while change:
        change = False
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[x][y]["energy"] > 9 and not board[x][y]["flashed"]:
                    board[x][y]["flashed"] = True
                    flashes += 1
                    change = True
                    for neighbor in neighbors(x, y):
                        board[neighbor[0]][neighbor[1]]["energy"] += 1

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[x][y]["flashed"]:
                board[x][y] = {"energy": 0, "flashed": False}

print(flashes)
