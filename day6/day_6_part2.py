import math
PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'


def read_input(puzzle):
    with open(f'{PATH}{puzzle}', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_input('day6/input.txt')
time = int(data[0].split(':')[1].replace(' ', ''))
distance = int(data[1].split(':')[1].replace(' ', ''))
ways_to_beat_record = []


def get_number_of_ways(time, record):
    possible_values = 0
    for i in range(0, int((time / 2)) + 1):
        distance = (time - i) * i
        if distance > record:
            possible_values += 1
    return 2*possible_values


number_of_ways = get_number_of_ways(time, distance)
print(number_of_ways)
