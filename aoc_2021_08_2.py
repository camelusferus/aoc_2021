input = open("input/input_08.txt").readlines()

result = 0

for line in input:
    descriptive = line.split("|")[0].split()

    detections = {}

    detections[1] = [ number for number in descriptive if len(number) == 2][0]
    descriptive.remove(detections[1])
    detections[4] = [ number for number in descriptive if len(number) == 4][0]
    descriptive.remove(detections[4])
    detections[7] = [ number for number in descriptive if len(number) == 3][0]
    descriptive.remove(detections[7])
    detections[8] = [ number for number in descriptive if len(number) == 7][0]
    descriptive.remove(detections[8])
    detections[3] = [ number for number in descriptive if (len(number) == 5 and set(detections[1]).issubset(set(number)))][0]
    descriptive.remove(detections[3])
    detections[9] = [ number for number in descriptive if (len(number) == 6 and set(detections[4]).issubset(set(number)))][0]
    descriptive.remove(detections[9])
    detections[0] = [ number for number in descriptive if (len(number) == 6 and set(detections[7]).issubset(set(number)))][0]
    descriptive.remove(detections[0])
    detections[6] = [ number for number in descriptive if len(number) == 6][0]
    descriptive.remove(detections[6])
    detections[5] = [ number for number in descriptive if (len(number) == 5 and set(detections[6]).issuperset(set(number)))][0]
    descriptive.remove(detections[5])
    detections[2] = descriptive[0]

    result_local = 0

    definitions = dict((str(sorted(value)), key) for key, value in detections.items())

    for number in line.split("|")[1].split():
        result_local *= 10
        result_local += definitions[str(sorted(number))]

    result += result_local

print(result)