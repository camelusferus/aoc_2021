input = open("input/input_14.txt").read().split("\n\n")
rules = {element.split(" -> ")[0]: element.split(" -> ")[1] for element in input[1].split("\n")}
str_new = input[0]

for i in range(10):
    str_old = str_new
    str_new = ""
    for char in range(len(str_old)-1):
        str_new += str_old[char]
        if str_old[char:char+2] in rules.keys():
            str_new += rules[str_old[char:char+2]]
    str_new += str_old[-1]

occurrences = [str_new.count(a) for a in str_new]
occurrences.sort()

print(str(occurrences[-1]-occurrences[0]))