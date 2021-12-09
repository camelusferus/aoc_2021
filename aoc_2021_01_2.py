file = open("input/input_01.txt")

increments = 0
countdown = 3

for line in file.readlines():
    if countdown < 1: point_minus_three = point_minus_two
    if countdown < 2: point_minus_two = point_minus_one
    if countdown < 3: point_minus_one = point
    point = int(line)
    if countdown < 1:
        old_sum = point_minus_three + point_minus_two + point_minus_one
        new_sum = point_minus_two + point_minus_one + point
        if old_sum < new_sum:
            increments = increments + 1
    countdown = countdown - 1

print(increments)
