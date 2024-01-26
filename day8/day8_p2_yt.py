from collections import defaultdict
import re
import math

PATH = '/Users/aratiu/Documents/Workspace/advent_of_code_2023/'

with open(PATH +"day8/input.txt") as fin:
    lines = fin.read().strip().split("\n")

children = defaultdict(str)

steps = lines[0]
for line in lines[2:]:
    par, left, right = re.search("(...) = \((...), (...)\)", line).groups(0)
    children[par] = (left, right)


def n_steps(cur):
    count = 0
    while cur[2] != "Z":
        step = steps[count % len(steps)]
        if step == "L":
            cur = children[cur][0]
        else:
            cur = children[cur][1]

        count += 1

    return count


cur = [n for n in children if n[2] == "A"]
lens = [n_steps(node) for node in cur]

ans = math.lcm(*lens)
print(ans)