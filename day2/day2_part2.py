import re
import math
PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'


games = []
sum = 0

with open(PATH + 'day2/input_part1.txt') as f:
    for line in f.readlines():

        game_dict = {
            'game_number': 0,
            'sets_of_cubes': []
        }

        game_info = line.split(':')[0]
        all_sets = line.split(':')[1]
        game_number = int(re.search(r'\d+', game_info).group())
        sets_of_cubes = []
        for set in all_sets.split(';'):

            set_of_cubes = {
                'green': 0,
                'blue': 0,
                'red': 0
            }

            for key in set_of_cubes.keys():
                set_regex = r'(\d+) ({})'.format(key)
                set_regex_obj = re.search(set_regex, set)
                if set_regex_obj:
                    cube_color = set_regex_obj.groups()[1]
                    number_of_cubes = set_regex_obj.groups()[0]
                    set_of_cubes[cube_color] = int(number_of_cubes)
                    sets_of_cubes.append(set_of_cubes)
        game_dict['game_number'] = game_number
        game_dict['sets_of_cubes'] = sets_of_cubes
        games.append(game_dict)


for game in games:
    set_power = 1
    min_set = {
        'red':0,
        'green':0,
        'blue':0
    }
    for set in game['sets_of_cubes']:
        for key in set.keys():
            if set[key] > min_set[key]:
                min_set[key] = set[key]
        set_power = math.prod(list(min_set.values()))
    sum += set_power
print(sum)