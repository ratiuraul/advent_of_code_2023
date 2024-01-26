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

current_nodes = [n for n in input_nodes if n.endswith('A')]
copy_of_current_nodes = list(current_nodes)
all_nodes_were_moved = len(current_nodes)
nodes_moved = 0
count = 0
instruction_index = 0
instructions = instructions*(len(list(input_nodes.keys()))+ 1)


while not all([True if node_value.endswith('Z') else False for node_value in current_nodes]):
    instruction = instructions[instruction_index]
    for node in copy_of_current_nodes:
        if instruction == 'L':
            next_node = input_nodes[node][0]
        else:
            next_node = input_nodes[node][1]
        current_nodes.append(next_node)
        current_nodes.remove(node)
        nodes_moved += 1
        if nodes_moved == all_nodes_were_moved:
            count += 1
            nodes_moved = 0
            instruction_index += 1
            copy_of_current_nodes = list(current_nodes)
    print('out_of_for')
print(count)