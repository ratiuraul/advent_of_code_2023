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
with open('input.txt') as f:
    for line in f.readlines():
        line_numbers = []
        word = ''
        for char in line:
            word += char
            if char.isdigit():
                line_numbers.append(char)
                word = ''
            else:
                for key in integers.keys():
                    if key in word:
                        line_numbers.append(integers[key])
                        word = ''
        if len(line_numbers):
            number = int(line_numbers[0]+line_numbers[-1])
            s += number

print(s)