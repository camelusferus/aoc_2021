input = open("input/input_10.txt").readlines()
corresponding = {'{': '}', '[': ']', '(': ')', '<': '>'}
filling_costs = []

for line in input:
    open_chuncks = []
    filling_cost = 0
    corrupted = False
    for char in range(len(line)):
        if line[char] in corresponding.keys():
            open_chuncks.append(line[char])
        elif line[char] in corresponding.values() and corresponding[open_chuncks[-1]] == line[char]:
            open_chuncks.pop()
        elif line[char] == ')' or line[char] == ']' or line[char] == '}' or line[char] == '>':
            corrupted = True
            break

    if not corrupted and len(open_chuncks):
        while len(open_chuncks):
            filling_cost *= 5
            if open_chuncks[-1] == '(':
                filling_cost += 1
            elif open_chuncks[-1] == '[':
                filling_cost += 2
            elif open_chuncks[-1] == '{':
                filling_cost += 3
            elif open_chuncks[-1] == '<':
                filling_cost += 4
            open_chuncks.pop()
        filling_costs.append(filling_cost)

print(sorted(filling_costs)[len(filling_costs) // 2])
