with open("D:\Projects\Python Testing\Advent of Code\day 8\input.txt", "r") as f:
    lines = [line.rstrip().split() for line in f]
instructions = lines[0][0]
lines = lines[2:]
node_mappings = {line[0]:(line[2][1:-1], line[3][:-1]) for line in lines}

def firstHalf():
    sum = 0
    curr_node = "AAA"
    while curr_node != "ZZZ":
        for instruction in instructions:
            if curr_node == "ZZZ":
                break
            elif instruction == "L":
                curr_node = node_mappings[curr_node][0]
                sum += 1
            elif instruction == "R":
                curr_node = node_mappings[curr_node][1]
                sum += 1
    print("sum:", sum)

def secondHalf():
    curr_nodes = [key for key in node_mappings.keys() if key.endswith("A")]
    done_searching = False
    sum = 0
    while not done_searching:
        for instruction in instructions:
            done_searching = all(node.endswith("Z") for node in curr_nodes)
            if done_searching:
                break
            elif instruction == "L":
                for i in range(len(curr_nodes)):
                    curr_nodes[i] = node_mappings[curr_nodes[i]][0]
                sum += 1
            elif instruction == "R":
                for i in range(len(curr_nodes)):
                    curr_nodes[i] = node_mappings[curr_nodes[i]][1]
                sum += 1
    print("sum:", sum)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(nums):
    result_lcm = nums[0]
    for num in nums[1:]:
        result_lcm = abs(result_lcm * num) // gcd(result_lcm, num)
    return result_lcm

def secondHalfLCM():
    curr_nodes = [key for key in node_mappings.keys() if key.endswith("A")]
    curr_count = [0 for node in curr_nodes]
    done_searching = False
    sum = 0
    while not done_searching:
        for instruction in instructions:
            done_searching = all(node.endswith("Z") for node in curr_nodes)
            if done_searching:
                break
            elif instruction == "L":
                for i in range(len(curr_nodes)):
                    if not curr_nodes[i].endswith("Z"):
                        curr_nodes[i] = node_mappings[curr_nodes[i]][0]
                        curr_count[i] += 1
            elif instruction == "R":
                for i in range(len(curr_nodes)):
                    if not curr_nodes[i].endswith("Z"):
                        curr_nodes[i] = node_mappings[curr_nodes[i]][1]
                        curr_count[i] += 1
    sum = lcm(curr_count)
    print("sum:", sum)


#firstHalf()
#secondHalf()
secondHalfLCM()