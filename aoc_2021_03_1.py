file = open("input/input_03.txt")

indexes = list()

for line in file.readlines():
    if not len(indexes):
        indexes = [ int(0) ] * (len(line))
    for x in range(len(line)-1):
        indexes[x] = indexes[x] + (int(line[x]) * 2 - 1)

gamma = 0
epsilon = 0

for x in range(len(indexes)):
    gamma = gamma * 2 + ( indexes[x] < 0 )
    epsilon = epsilon * 2 + ( indexes[x] > 0 )

print( epsilon * gamma / 4 )