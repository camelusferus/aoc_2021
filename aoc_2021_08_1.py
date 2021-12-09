input = open("input/input_08.txt").readlines()

print( sum([1 for number in
              [number for numbers in
                [line.split("|")[1].split() for line in input ]
              for number in numbers ]
            if (number.__len__() != 5) & (number.__len__() != 6)])
       )