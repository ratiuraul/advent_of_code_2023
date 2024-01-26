PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'
with open(PATH + 'day4/input.txt') as f:
    lines = f.readlines()
    cards_appearances = {card_id:1 for card_id in range(1, len(lines) + 1)}
    for card_id, line in enumerate(lines, 1):
        all_numbers = line.split(':')[1]
        numbers_you_have = all_numbers.split('|')[0].strip().split(' ')
        winning_numbers = all_numbers.split('|')[1].strip().split(' ')
        your_winning_numbers = list(filter(('').__ne__,
            set(numbers_you_have) & set(winning_numbers)))
        if your_winning_numbers:
            for number_of_cards in range(0, cards_appearances[card_id]):
                copy_of_card_id = card_id
                for card in range(0, len(your_winning_numbers)):
                    copy_of_card_id += 1
                    cards_appearances[copy_of_card_id] += 1
    print(sum(cards_appearances.values()))

