with open("D:\Projects\Python Testing\Advent of Code\day 6\input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

def firstHalf():
    mult = 1
    times = [int(time) for time in lines[0].split()[1:]]
    distances = [int(distance) for distance in lines[1].split()[1:]]
    for race_idx, time in enumerate(times):
        partial_sum = 0
        for milliseconds in range(time):
            calc_distance = (time - milliseconds) * milliseconds
            if calc_distance > distances[race_idx]:
                partial_sum += 1
        mult = mult * partial_sum
    print("mult:", mult)

def secondHalf():
    sum = 0
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    for milliseconds in range(time):
        calc_distance = (time - milliseconds) * milliseconds
        if calc_distance > distance:
            sum += 1
    print("sum:", sum)

#firstHalf()
secondHalf()