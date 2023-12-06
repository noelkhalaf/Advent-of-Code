with open("D:\Projects\Python Testing\Advent of Code\day 3\input.txt", "r") as f:
    lines = [line.rstrip() for line in f]
char_covered = [[False for char in line if char != "\n"] for line in lines]

def getLeftNumber(line_idx, char_idx):
    number = ""
    while (char_idx > -1):
        char = lines[line_idx][char_idx]
        if char.isdigit():
            number = char + number
            char_covered[line_idx][char_idx] = True
        else:
            break
        char_idx -= 1
    return "0" if number == "" else number

def getRightNumber(line_idx, char_idx):
    number = ""
    while (char_idx < len(lines[line_idx])):
        char = lines[line_idx][char_idx]
        if char.isdigit():
            number = number + char
            char_covered[line_idx][char_idx] = True
        else:
            break
        char_idx += 1
    return "0" if number == "" else number

def getMiddleNumber(line_idx, char_idx):
    number = getLeftNumber(line_idx, char_idx)
    if char_idx != len(lines[line_idx])-1 and lines[line_idx][char_idx + 1].isdigit():
        number = number + getRightNumber(line_idx, char_idx + 1)
    return number

def addAroundSymbol(line_idx, char_idx):
    partial_sum = 0
    has_up = has_down = has_left = has_right = False
    up_is_digit = down_is_digit = False
    if line_idx != 0:
        has_up = True
        up_is_digit = lines[line_idx-1][char_idx].isdigit()
        if up_is_digit and not char_covered[line_idx-1][char_idx]:
            partial_sum += int(getMiddleNumber(line_idx-1, char_idx))
    if line_idx != len(lines)-1:
        has_down = True
        down_is_digit = lines[line_idx+1][char_idx].isdigit()
        if down_is_digit and not char_covered[line_idx+1][char_idx]:
            partial_sum += int(getMiddleNumber(line_idx+1, char_idx))
    if char_idx != 0:
        has_left = True
        if lines[line_idx][char_idx-1].isdigit() and not char_covered[line_idx][char_idx-1]:
            partial_sum += int(getLeftNumber(line_idx, char_idx-1))
    if char_idx != len(lines[line_idx])-1:
        has_right = True
        if lines[line_idx][char_idx+1].isdigit() and not char_covered[line_idx][char_idx+1]:
            partial_sum += int(getRightNumber(line_idx, char_idx+1))
    # Check Diagonals
    if has_up and not up_is_digit:
        if has_left and lines[line_idx-1][char_idx-1].isdigit() and not char_covered[line_idx-1][char_idx-1]:
            partial_sum += int(getLeftNumber(line_idx-1, char_idx-1))
        if has_right and lines[line_idx-1][char_idx+1].isdigit() and not char_covered[line_idx-1][char_idx+1]:
            partial_sum += int(getRightNumber(line_idx-1, char_idx+1))
    if has_down and not down_is_digit:
        if has_left and lines[line_idx+1][char_idx-1].isdigit() and not char_covered[line_idx+1][char_idx-1]:
            partial_sum += int(getLeftNumber(line_idx+1, char_idx-1))
        if has_right and lines[line_idx+1][char_idx+1].isdigit() and not char_covered[line_idx+1][char_idx+1]:
            partial_sum += int(getRightNumber(line_idx+1, char_idx+1))
    return partial_sum

def firstHalf():
    sum = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit() or char == ".":
                pass
            else:
                sum += addAroundSymbol(i, j)
    print("sum:", sum)

def addTwoAroundSymbol(line_idx, char_idx):
    partial_mult = 1
    has_up = has_down = has_left = has_right = False
    up_is_digit = down_is_digit = False
    num_part_numbers = 0
    if line_idx != 0:
        has_up = True
        up_is_digit = lines[line_idx-1][char_idx].isdigit()
        if up_is_digit and not char_covered[line_idx-1][char_idx]:
            partial_mult *= int(getMiddleNumber(line_idx-1, char_idx))
            num_part_numbers += 1
    if line_idx != len(lines)-1:
        has_down = True
        down_is_digit = lines[line_idx+1][char_idx].isdigit()
        if down_is_digit and not char_covered[line_idx+1][char_idx]:
            partial_mult *= int(getMiddleNumber(line_idx+1, char_idx))
            num_part_numbers += 1
    if char_idx != 0:
        has_left = True
        if lines[line_idx][char_idx-1].isdigit() and not char_covered[line_idx][char_idx-1]:
            partial_mult *= int(getLeftNumber(line_idx, char_idx-1))
            num_part_numbers += 1
    if char_idx != len(lines[line_idx])-1:
        has_right = True
        if lines[line_idx][char_idx+1].isdigit() and not char_covered[line_idx][char_idx+1]:
            partial_mult *= int(getRightNumber(line_idx, char_idx+1))
            num_part_numbers += 1
    # Check Diagonals
    if has_up and not up_is_digit:
        if has_left and lines[line_idx-1][char_idx-1].isdigit() and not char_covered[line_idx-1][char_idx-1]:
            partial_mult *= int(getLeftNumber(line_idx-1, char_idx-1))
            num_part_numbers += 1
        if has_right and lines[line_idx-1][char_idx+1].isdigit() and not char_covered[line_idx-1][char_idx+1]:
            partial_mult *= int(getRightNumber(line_idx-1, char_idx+1))
            num_part_numbers += 1
    if has_down and not down_is_digit:
        if has_left and lines[line_idx+1][char_idx-1].isdigit() and not char_covered[line_idx+1][char_idx-1]:
            partial_mult *= int(getLeftNumber(line_idx+1, char_idx-1))
            num_part_numbers += 1
        if has_right and lines[line_idx+1][char_idx+1].isdigit() and not char_covered[line_idx+1][char_idx+1]:
            partial_mult *= int(getRightNumber(line_idx+1, char_idx+1))
            num_part_numbers += 1
    if num_part_numbers == 2:
        return partial_mult
    return 0

def secondHalf():
    sum = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit() or char == ".":
                pass
            else:
                sum += addTwoAroundSymbol(i, j)
    print("sum:", sum)

#firstHalf()
secondHalf()