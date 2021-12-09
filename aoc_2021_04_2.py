input_blocks = open("input/input_04.txt").read().split("\n\n")

drawn_numbers = input_blocks[0].split(",")

bingo_fields = [[line.split() for line in input_blocks[i].split("\n")] for i in range(1,input_blocks.__len__())]

worst_field_state = 0

for bingo_field in range(bingo_fields.__len__()):
    for number in range(drawn_numbers.__len__()):
        for line in range(5):
            for field in range(5):
                if int(bingo_fields[bingo_field][line][field]) == int(drawn_numbers[number]):
                    bingo_fields[bingo_field][line][field] = "-1"

        if ["-1"] * 5 in bingo_fields[bingo_field] or ('-1', '-1', '-1', '-1', '-1') in list(zip(*bingo_fields[bingo_field])):
            if worst_field_state < number:
                worst_field_state = number
                worst_field_value = int(sum([sum([int(field) for field in line if field != "-1"]) for line in bingo_fields[bingo_field]])) * int(drawn_numbers[number])
            break

print (worst_field_value)
