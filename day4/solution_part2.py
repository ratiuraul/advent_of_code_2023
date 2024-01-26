PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'
TOTAL_CARD_POINTS = 0
with open(PATH + 'day4/input.txt') as f:
    for line in f.readlines():
        all_numbers = line.split(':')[1]
        numbers_you_have = all_numbers.split('|')[0].strip().split(' ')
        winning_numbers = all_numbers.split('|')[1].strip().split(' ')
        your_winning_numbers = list(filter(('').__ne__,
            set(numbers_you_have) & set(winning_numbers)))
        if your_winning_numbers:
            card_points = 2**(len(your_winning_numbers) - 1)
            TOTAL_CARD_POINTS += card_points

print(TOTAL_CARD_POINTS)