PATH = '/Users/aratiu/Documents/Workspace/advent_of_code_2023/'


def read_input(puzzle):
    with open(f'{PATH}{puzzle}', 'r') as f:
        data = f.read().splitlines()
    return [line for line in data if line]


data = [num.split(' ') for num in read_input('day9/input.txt')]

history_values = []


def generate_sequences(input_sequence):
    input_sequence = [int(i) for i in input_sequence]
    list_of_sequences = [input_sequence]
    new_sequence = input_sequence
    while True:
        new_sequence = [new_sequence[i+1] - new_sequence[i]
                        for i in range(len(new_sequence)-1)]
        list_of_sequences.append(new_sequence)
        if all([True if number == 0 else False for number in new_sequence]):
            break
    return list_of_sequences


def calculate_history_of_sequences(input_sequence):
    local_history = []
    list_of_sequences = list(reversed(generate_sequences(input_sequence)))
    for index, sequence in enumerate(list_of_sequences):
        if index < len(list_of_sequences) - 1:
            history_value = sequence[-1] + list_of_sequences[index + 1][-1]
            local_history.append(history_value)
            list_of_sequences[index + 1].append(history_value)
    history_values.append(local_history[-1])


for history_data in data:
    calculate_history_of_sequences(history_data)


print(sum(history_values))
print('here')
