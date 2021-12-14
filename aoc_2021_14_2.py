input = open("input/input_14.txt").read().split("\n\n")
rules = {element.split(" -> ")[0]: element.split(" -> ")[1] for element in input[1].split("\n")}
polymer = {}

for index in range(len(input[0])-1):
    if input[0][index:index + 2] in polymer.keys():
        polymer[input[0][index:index + 2]] += 1
    else:
        polymer[input[0][index:index + 2]] = 1

for i in range(40):
    old_polymer = polymer
    polymer = {}
    for piece in old_polymer:
        if piece[0]+rules[piece] in polymer.keys():
            polymer[piece[0]+rules[piece]] += old_polymer[piece]
        else:
            polymer[piece[0]+rules[piece]] = old_polymer[piece]
        if rules[piece]+piece[1] in polymer.keys():
            polymer[rules[piece]+piece[1]] += old_polymer[piece]
        else:
            polymer[rules[piece]+piece[1]] = old_polymer[piece]

occurrences = {}
for key in polymer.keys():
    if key[0] in occurrences:
        occurrences[key[0]] += polymer[key]
    else:
        occurrences[key[0]] = polymer[key]
    if key[1] in occurrences:
        occurrences[key[1]] += polymer[key]
    else:
        occurrences[key[1]] = polymer[key]

occurrences[input[0][0]] += 1
occurrences[input[0][-1]] += 1
occurrences_values = list(occurrences.values())
occurrences_values.sort()

print(str((occurrences_values[-1]-occurrences_values[0]) // 2))