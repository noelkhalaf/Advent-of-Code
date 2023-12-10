with open("D:\Projects\Python Testing\Advent of Code\day 10\input.txt", "r") as f:
    lines = ["." + line.rstrip() + "." for line in f]
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))

directions_dict = {
    "north" : "|LJS",
    "south" : "|7FS",
    "east" : "-LFS",
    "west" : "-J7S",
}

def getStartingPosition():
    for row_idx, line in enumerate(lines):
        col_idx = line.lower().find('s')
        if col_idx != -1:
            break
    return [row_idx, col_idx]

def isLegalPath(curr_pos, dir):
    match dir:
        case "north":
            next_row = curr_pos[0] - 1
            next_col = curr_pos[1]
            print(f"[{next_row}, {next_col}]: {lines[next_row][next_col]}")
            if directions_dict["south"].find(lines[next_row][next_col]) != -1:
                print(f"Correct path")
                return [next_row, next_col]
        case "south":
            next_row = curr_pos[0] + 1
            next_col = curr_pos[1]
            print(f"[{next_row}, {next_col}]: {lines[next_row][next_col]}")
            if directions_dict["north"].find(lines[next_row][next_col]) != -1:
                print(f"Correct path")
                return [next_row, next_col]
        case "east":
            next_row = curr_pos[0]
            next_col = curr_pos[1] + 1
            print(f"[{next_row}, {next_col}]: {lines[next_row][next_col]}")
            if directions_dict["west"].find(lines[next_row][next_col]) != -1:
                print(f"Correct path")
                return [next_row, next_col]
        case "west":
            next_row = curr_pos[0]
            next_col = curr_pos[1] - 1
            print(f"[{next_row}, {next_col}]: {lines[next_row][next_col]}")
            if directions_dict["east"].find(lines[next_row][next_col]) != -1:
                print(f"Correct path")
                return [next_row, next_col]
    return False

def flipDirection(dir):
    match dir:
        case "north":
            return "south"
        case "south":
            return "north"
        case "east":
            return "west"
        case "west":
            return "east"

def isLegalExit(curr_pos, dir):
    return directions_dict[dir].find(lines[curr_pos[0]][curr_pos[1]]) != -1

def getNextPosition(curr_pos, prev_dir):
    for dir in directions_dict.keys():
        if (flipDirection(dir) != prev_dir) and isLegalExit(curr_pos, dir):
            next_pos = isLegalPath(curr_pos, dir)
            if next_pos:
                return next_pos, dir
    return False, ""

def printPipes():
    for line in lines:
        print(line)

def firstHalf():
    sum = 0
    starting_position = getStartingPosition()
    starting_directions = []
    current_position = starting_position
    previous_direction = ""
    done_searching = False
    printPipes()
    print("Starting position:", starting_position)
    print("Starting directions:", starting_directions)
    while (current_position != starting_position) or (previous_direction == ""):
        current_position, previous_direction = getNextPosition(current_position, previous_direction)
        sum += 1
        if not current_position:
            sum = 0
            current_position = starting_position
            if "north" not in starting_directions:
                starting_directions.append("north")
            elif "south" not in starting_directions:
                starting_directions.append("south")
            elif "east" not in starting_directions:
                starting_directions.append("east")
            elif "west" not in starting_directions:
                starting_directions.append("west")
            print("Starting directions:", starting_directions)
    print("sum:", sum//2)

def secondHalf():
    sum = 0
    print("sum:", sum)

firstHalf()
#secondHalf()