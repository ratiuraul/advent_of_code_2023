import sys
PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'

totalPoints = 0
with open(PATH + 'day4/input.txt') as file:
    # Read all the lines of the file into a list
    lines = file.readlines()
    cardCounts = [1] * len(lines)
    for cardId, line in enumerate(lines):
        goal = set(
            (tokens := line.split())[2: (barIndex := tokens.index('|'))])
        hand = set(tokens[barIndex + 1:])

        totalPoints += (points := 2 ** (matches - 1)
                        if (matches := len(goal & hand)) else 0)

        for copyCardId in range(cardId + 1, cardId + matches + 1):
            cardCounts[copyCardId] += cardCounts[cardId]

    print('Part 1 result:', totalPoints)
    print('Part 2 result:', sum(cardCounts))