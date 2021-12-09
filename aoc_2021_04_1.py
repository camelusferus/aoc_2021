input_blocks = open("input/input_04.txt").read().split("\n\n")

drawn_numbers = input_blocks[0].split(",")

bingo_fields = [[line.split() for line in input_blocks[i].split("\n")] for i in range(1,input_blocks.__len__())]

for number in drawn_numbers:
    for bingo_field in range(bingo_fields.__len__()):
        for line in range(5):
            for field in range(5):
                if int(bingo_fields[bingo_field][line][field]) == int(number):
                    bingo_fields[bingo_field][line][field] = "-1"

        if ["-1"] * 5 in bingo_fields[bingo_field] or ('-1', '-1', '-1', '-1', '-1') in list(zip(*bingo_fields[bingo_field])):
            print(str(int(sum([sum([int(field) for field in line if field != "-1"]) for line in bingo_fields[bingo_field]])) * int(number)))
            exit()
