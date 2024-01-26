from functools import cmp_to_key
from collections import defaultdict
PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'


def read_input(puzzle):
    with open(f'{PATH}{puzzle}', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_input('day7/input.txt')


labels = "AKQJT98765432"


def get_type(hand):
    counts = defaultdict(int)
    for x in hand:
        counts[x] += 1

    amounts = sorted(counts.values())
    if amounts == [5]:
        return 5
    if amounts == [1, 4]:
        return 4
    if amounts == [2, 3]:
        return 3.5
    if amounts == [1, 1, 3]:
        return 3
    if amounts == [1, 2, 2]:
        return 2.5
    if amounts == [1, 1, 1, 2]:
        return 2
    return 1


def compare(a, b):
    rank_a = get_type(a)
    rank_b = get_type(b)

    if rank_a == rank_b:
        if a == b:
            return 0
        for i, j in zip(a, b):
            if labels.index(i) > labels.index(j):
                return -1
            if labels.index(i) < labels.index(j):
                return 1
        return -1
    elif rank_a > rank_b:
        return 1
    return -1


lines = []
for line in data:
    line = line.split()
    lines.append((line[0], int(line[1])))
lines = sorted(lines, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
ans = 0
for i, line in enumerate(lines):
    ans += (i + 1) * line[1]

print(ans)