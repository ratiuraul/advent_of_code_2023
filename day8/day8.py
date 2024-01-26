PATH = '/Users/Raul/Documents/Workspace/advent_of_code/'


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

class Node:
    def __init__(self, content, left, right):
        self.content = content
        self.left = left
        self.right = right


root = None
while input_nodes:
    if not root:
        node_content = input_nodes.keys[0]
        left, right = input_nodes[node_content]
        root = Node(content=node_content, left=left, right=right)
        del input_nodes[node_content]
# for node_content in input_nodes:
#     left, right = input_nodes[node_content]
#     if not root:
#         root = Node(content=node_content, left=left, right=right)
#     elif node_content == root.left :


distance = 0
instructions = instructions * len(tree)
print('hre')
# for node, instruction in zip (tree, instructions):
