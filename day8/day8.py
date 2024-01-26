from platform import node


PATH = '/Users/aratiu/Documents/Workspace/advent_of_code_2023/'


def read_input(puzzle):
    with open(f'{PATH}{puzzle}', 'r') as f:
        data = f.read().splitlines()
    return [line for line in data if line]


data = read_input('day8/input.txt')
instructions = [instruction.strip() for instruction in data.pop(0)]
input_nodes = {}
for node_info in data:
    content = node_info.split('=')[0].strip()
    neighbours = node_info.split(
        '=')[1].strip().replace('(', '').replace(')', '')
    input_nodes[content] = tuple(map(str, neighbours.split(', ')))

current = 'AAA'
count = 0
instruction_index = 0
instructions = instructions*len(list(input_nodes.keys()))
while current != 'ZZZ':
    count += 1
    instruction = instructions[instruction_index]
    if instruction == 'L':
        current = input_nodes[current][0]
    else:
        current = input_nodes[current][1]
    instruction_index += 1
print(count)