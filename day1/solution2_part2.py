s = 0
integers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


class Number:
    def __init__(self, first_index, last_index, value):
        self.first_index = first_index
        self.last_index= last_index
        self.value = value


with open('input.txt') as f:
    for line in f.readlines():
        line_numbers = []
        to_be_added = ''
        for key in integers.keys():
            if key in line:
                line_numbers.append(Number(line.find(key), line.rfind(key), integers[key]))
        for char in line:
            if char.isdigit():
                line_numbers.append(Number(line.find(char), line.rfind(char), char))

        good_numbers = [min(line_numbers, key=lambda number: number.first_index),
                        max(line_numbers, key=lambda number: number.last_index)]
        for number in good_numbers:
            to_be_added += str(number.value)
        s += int(to_be_added)
print(s)
