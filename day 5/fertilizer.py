with open("D:\Projects\Python Testing\Advent of Code\day 5\input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

def mapSeed(seed, mappings):
    for mapping in mappings:
        if mapping[1] <= seed < (mapping[1] + mapping[2]):
            diff = mapping[1] - mapping[0]
            return seed - diff
    return seed

def firstHalf():
    seeds = [int(seed) for seed in lines[0].replace("seeds:", "").split()]
    new_seeds = seeds
    lines.pop(0)
    mappings = []
    print(new_seeds)
    for line_idx, line in enumerate(lines):
        if (not line and mappings) or (line_idx == (len(lines) - 1)):
            for i, seed in enumerate(seeds):
                new_seeds[i] = mapSeed(new_seeds[i], mappings)
            print(new_seeds)
        if line and line[0].isdigit():
            mappings.append([int(num) for num in line.split()])
        else:
            print(line)
            mappings = []
    print("min:", min(new_seeds))

def secondHalf():
    sum = 0
    print("sum:", sum)

firstHalf()
#secondHalf()