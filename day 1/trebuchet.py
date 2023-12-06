with open("D:\Projects\Python Testing\Advent of Code\day 1\input.txt", "r") as f:
    lines = f.readlines()

def firstHalf():
    sum = 0
    for line in lines:
        for i in range(len(line)):
            if line[i].isdigit():
                calibration_value = line[i]
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                calibration_value = calibration_value + line[i]
                break
        print("calibration:", calibration_value)
        sum += int(calibration_value)
    print("sum:", sum)

def secondHalf():
    sum = 0
    for line in lines:
        for i in range(len(line)):
            if line[i].isdigit():
                calibration_value = line[i]
                break
            try:
                if line[i:i+3] == "one":
                    calibration_value = "1"
                    break
                elif line[i:i+3] == "two":
                    calibration_value = "2"
                    break
                elif line[i:i+5] == "three":
                    calibration_value = "3"
                    break
                elif line[i:i+4] == "four":
                    calibration_value = "4"
                    break
                elif line[i:i+4] == "five":
                    calibration_value = "5"
                    break
                elif line[i:i+3] == "six":
                    calibration_value = "6"
                    break
                elif line[i:i+5] == "seven":
                    calibration_value = "7"
                    break
                elif line[i:i+5] == "eight":
                    calibration_value = "8"
                    break
                elif line[i:i+4] == "nine":
                    calibration_value = "9"
                    break
            except IndexError:
                pass
        for i in range(len(line), -1, -1):
            if line[i-1].isdigit():
                calibration_value = calibration_value + line[i-1]
                break
            try:
                if line[i-3:i] == "one":
                    calibration_value = calibration_value + "1"
                    break
                elif line[i-3:i] == "two":
                    calibration_value = calibration_value + "2"
                    break
                elif line[i-5:i] == "three":
                    calibration_value = calibration_value + "3"
                    break
                elif line[i-4:i] == "four":
                    calibration_value = calibration_value + "4"
                    break
                elif line[i-4:i] == "five":
                    calibration_value = calibration_value + "5"
                    break
                elif line[i-3:i] == "six":
                    calibration_value = calibration_value + "6"
                    break
                elif line[i-5:i] == "seven":
                    calibration_value = calibration_value + "7"
                    break
                elif line[i-5:i] == "eight":
                    calibration_value = calibration_value + "8"
                    break
                elif line[i-4:i] == "nine":
                    calibration_value = calibration_value + "9"
                    break
            except IndexError:
                pass
        print("calibration:", calibration_value)
        sum += int(calibration_value)
    print("sum:", sum)

# firstHalf()
# secondHalf()