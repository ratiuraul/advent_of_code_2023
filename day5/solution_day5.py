import re
from collections import defaultdict

PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'
MAPS_REGEX = '({} map:)(([0-9]*\s?|\n)*)'


BIG_MAP = defaultdict(lambda: list(range(9999999999)))


def populate_maps(map, data):
    maps = {map: []}
    ranges = re.search(MAPS_REGEX.format(map), data)
    for map_range in ranges.groups()[1].strip().split('\n'):

        map_structure = {
            'destination_range_start': 0,
            'source_range_start': 0,
            'range_length': 0,
        }
        map_structure['destination_range_start'] = int(map_range.split(' ')[0])
        map_structure['source_range_start'] = int(map_range.split(' ')[1])
        map_structure['range_length'] = int(map_range.split(' ')[2])
        maps[map].append(map_structure)
    return maps


def add_maps_to_big_map(initial_maps):
    for map in initial_maps:
        map_value = list(map.keys())[0].split('-to-')[1]
        for map_ranges in map.values():
            for map_range in map_ranges:
                for i in range(map_range['destination_range_start'],
                               map_range['destination_range_start'] + map_range['range_length']):
                    BIG_MAP[map_value][map_range['source_range_start']] = i
                    map_range['source_range_start'] += 1


def get_lowest_location_for_seeds(seed_numbers):
    location_numbers = []
    for seed_number in seed_numbers:
        soil_number = BIG_MAP['soil'][int(seed_number)]
        fertilizer_number = BIG_MAP['fertilizer'][soil_number]
        water_number = BIG_MAP['water'][fertilizer_number]
        light_number = BIG_MAP['light'][water_number]
        temperature_number = BIG_MAP['temperature'][light_number]
        humidity_number = BIG_MAP['humidity'][temperature_number]
        location_number = BIG_MAP['location'][humidity_number]
        location_numbers.append(location_number)
    print(min(location_numbers))


with open(PATH + 'day5/input.txt', 'r') as file:
    data = file.read()
    maps_mappings = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
                     'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    initial_maps = []
    for map_name in maps_mappings:
        initial_maps.append(populate_maps(map_name, data))

    add_maps_to_big_map(initial_maps)
    seeds = re.search('(seeds:)(([0-9]*\s?|\n)*)', data).groups()[1].strip().split(' ')
    get_lowest_location_for_seeds(seeds)
