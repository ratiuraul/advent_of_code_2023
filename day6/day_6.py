PATH = '/Users/aratiu/Documents/Workspace/advent_of_code_2023/'
import math



def read_input(puzzle):
    with open(f'{PATH}{puzzle}', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_input('day6/input.txt')
time = [int(num) for num in data[0].split(':')[1].split(' ') if num != '']
distance = [int(num) for num in data[1].split(':')[1].split(' ') if num != '']
ways_to_beat_record = []


def get_number_of_ways(time, record):
    possible_values = []
    for i in range(0, time + 1):
        distance = (time - i) * i
        if distance > record:
            possible_values.append(distance)
    return len(possible_values)


for distance_poisition, time_values in enumerate(time):
    number_of_ways = get_number_of_ways(
        time_values, distance[distance_poisition])
    ways_to_beat_record.append(number_of_ways)

print(math.prod(ways_to_beat_record))
