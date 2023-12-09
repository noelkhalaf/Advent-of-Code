with open("D:\Projects\Python Testing\Advent of Code\day 9\input.txt", "r") as f:
    lines = [line.rstrip().split() for line in f]

def buildLevelTree(levels, direction):
    last_level_reached = False
    while not last_level_reached: # Adds new levels until current is all 0s
        temp_level = []

        if direction == "right":
            for level_idx, num in enumerate(levels[-1]): # Loops through current level and calculates next level
                if levels[-1][level_idx + 1] == "P":
                    break
                else:
                    temp_level.append(levels[-1][level_idx + 1] - num)
            last_level_reached = all(number == 0 for number in temp_level)
            if last_level_reached:
                temp_level.append(0)
            else:
                temp_level.append("P")
            levels.append(temp_level)

        elif direction == "left":
            for level_idx in range(len(levels[-1]) - 1, 0, -1): # Loops through current level and calculates next level
                if levels[-1][level_idx - 1] == "P":
                    break
                else:
                    temp_level.insert(0, levels[-1][level_idx] - levels[-1][level_idx - 1])
            last_level_reached = all(number == 0 for number in temp_level)
            if last_level_reached:
                temp_level.insert(0, 0)
            else:
                temp_level.insert(0, "P")
            levels.append(temp_level)
    return levels

def replaceTreePlaceholders(levels, direction):
    for i in range(len(levels) - 2, -1, -1):
        if direction == "right":
            levels[i][-1] = levels[i][-2] + levels[i + 1][-1]
        elif direction == "left":
            levels[i][0] = levels[i][1] - levels[i + 1][0]
    return levels

def firstHalf():
    sum = 0
    for line in lines:
        levels = [[int(num) for num in line] + ["P"]] # Fills first line
        levels = buildLevelTree(levels, "right") # Completes levels tree
        levels = replaceTreePlaceholders(levels, "right") # Calculates/replaces placeholders
        sum += levels[0][-1]
    print("sum:", sum)

def secondHalf():
    sum = 0
    for line in lines:
        levels = [["P"] + [int(num) for num in line]] # Fills first line
        levels = buildLevelTree(levels, "left") # Completes levels tree
        levels = replaceTreePlaceholders(levels, "left") # Calculates/replaces placeholders
        sum += levels[0][0]
    print("sum:", sum)

#firstHalf()
secondHalf()