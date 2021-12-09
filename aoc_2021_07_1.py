input = open("input/input_07.txt").read()

crabs = [int(x) for x in input.split(",")]
best_fuel = crabs.__len__() ** 2

for a in range(min(crabs),max(crabs)+1):
    fuel = sum ([abs(crab - a) for crab in crabs])
    if (fuel < best_fuel):
        best_fuel = fuel

print(best_fuel)