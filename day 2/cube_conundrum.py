import re

with open("D:\Projects\Python Testing\Advent of Code\day 2\input.txt", "r") as f:
    lines = f.readlines()

def firstHalf(red_dice, green_dice, blue_dice):
    sum = 0
    for i, line in enumerate(lines):
        dice = re.findall(r"(\d+)\s(blue|red|green)", line)
        red_max = 0
        green_max = 0
        blue_max = 0
        for (count, color) in dice:
            count_int = int(count)
            match color:
                case "red":
                    if count_int > red_max:
                        red_max = count_int
                case "green":
                    if count_int > green_max:
                        green_max = count_int
                case "blue":
                    if count_int > blue_max:
                        blue_max = count_int
        if (red_max <= red_dice) and (green_max <= green_dice) and (blue_max <= blue_dice):
            sum += i + 1
    print("sum:", sum)

def secondHalf():
    sum = 0
    for i, line in enumerate(lines):
        dice = re.findall(r"(\d+)\s(blue|red|green)", line)
        red_max = 0
        green_max = 0
        blue_max = 0
        for (count, color) in dice:
            count_int = int(count)
            match color:
                case "red":
                    if count_int > red_max:
                        red_max = count_int
                case "green":
                    if count_int > green_max:
                        green_max = count_int
                case "blue":
                    if count_int > blue_max:
                        blue_max = count_int
        min_power = red_max * green_max * blue_max
        print(f"Game {i+1} power of minimum:", min_power)
        sum += min_power
    print("sum:", sum)

# firstHalf(12, 13, 14)
secondHalf()