input = open("input/input_06.txt").read()

inventory = [0] * 9
for fish in input.split(","):
    inventory[int(fish)] += 1

for days in range(256):
    inventory = [inventory[1],inventory[2],inventory[3],inventory[4],inventory[5],inventory[6],
                 inventory[0]+inventory[7],inventory[8], inventory[0]]

print(sum(inventory))
