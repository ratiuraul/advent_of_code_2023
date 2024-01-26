import re
PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'
SUM = 0


def flatten(xss):
    return [x for xs in xss for x in xs]


def is_symbol(char):
    return True if not char.isnumeric() and char != '.' else False


def get_neighbour_matrix_for_position(input_matrix, line_number, column_number_start, column_number_end):

    if line_number == 0:
        line_number_start = 0
        line_number_end = 2
    elif line_number == len(input_matrix)-1:
        line_number_start = line_number -1
        line_number_end = line_number + 1
    else:
        line_number_start = line_number - 1
        line_number_end = line_number + 2

    column_number_start = 1 if column_number_start == 0 else column_number_start

    if column_number_end == len(input_matrix[line_number]):
        column_number_end = column_number_end - 1

    return [
        [
            input_matrix[line_number][column_number_start -
                                      1:column_number_end+1],
        ]
        for line_number in range(line_number_start, line_number_end)
    ]


with open(PATH + 'day3/input_part1.txt') as f:
    input_matrix = [[char for char in line]for line in f.read().splitlines()]
    for line_number, line_content_list in enumerate(input_matrix):
        line_content = ''.join(line_content_list)
        numbers_in_current_line = re.findall('\d+', line_content)
        for number in numbers_in_current_line:
            number_start_index = line_content.find(number)
            number_end_index = number_start_index + len(number)
            neighbour_matrix = get_neighbour_matrix_for_position(
                input_matrix=input_matrix, line_number=line_number,
                column_number_start=number_start_index, column_number_end=number_end_index
            )
            for line in neighbour_matrix:
                if any([is_symbol(char) for char in flatten(line)]):
                    print(f'Adding number: {number}')
                    SUM = SUM + int(number)
                    break

print(SUM)
