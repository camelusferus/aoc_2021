input = open("input/input_10.txt").readlines()
corresponding = {'{': '}', '[': ']', '(': ')', '<': '>'}
badness = 0

for line in input:
    open_chuncks = []
    for char in line:
        if char in corresponding.keys():
            open_chuncks.append(char)
        elif char in corresponding.values() and corresponding[open_chuncks[-1]] == char:
            open_chuncks.pop()
        elif char == ')':
            badness += 3
            break
        elif char == ']':
            badness += 57
            break
        elif char == '}':
            badness += 1197
            break
        elif char == '>':
            badness += 25137
            break

print(badness)
