input = open("input/input_12.txt").readlines()

vertices = [(line.split("-")[0], line.strip().split("-")[1]) for line in input]
paths = [0]


def find_paths (end, vertices, cur_path, paths):
    if cur_path[-1] == end:
        paths[0] += 1
        return

    for item in [key for item in vertices if cur_path[-1] in item for key in item]:
        if item != cur_path[-1] and (item.isupper() or item not in cur_path):
            find_paths(end, vertices, cur_path + [item],paths)


find_paths("end", vertices, ["start"], paths)

print(paths[0])