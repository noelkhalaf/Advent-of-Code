import re

with open("D:\Projects\Python Testing\Advent of Code\day 4\input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

count = 0

def firstHalf():
    sum = 0
    for line in lines:
        winning_numbers = re.findall(r":\s*([\d\s]+)\s*\|", line)[0].split()
        your_numbers = re.findall(r"\|\s*([\d\s]+)\s*", line)[0].split()
        partial_sum = 0
        for number in your_numbers:
            if number in winning_numbers:
                partial_sum = 1 if partial_sum == 0 else partial_sum * 2
        sum += partial_sum
    print("sum:", sum)

def recursiveAddition(line_idx):
    global count
    winning_numbers = re.findall(r":\s*([\d\s]+)\s*\|", lines[line_idx])[0].split()
    your_numbers = re.findall(r"\|\s*([\d\s]+)\s*", lines[line_idx])[0].split()
    num_matches = sum(1 for number in your_numbers if number in winning_numbers)
    for i in range(line_idx + 1, line_idx + num_matches + 1):
        count += 1
        recursiveAddition(i)

def secondHalf():
    global count
    for i in range(len(lines)):
        count += 1
        recursiveAddition(i)
    sum = count
    print("sum:", sum)

#firstHalf()
secondHalf()