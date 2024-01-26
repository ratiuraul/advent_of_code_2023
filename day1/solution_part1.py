s = 0
with open('input.txt') as f:
    for line in f.readlines():
        numbers = [char for char in line if char.isdigit()]
        if len(numbers):
            number = int(numbers[0]+numbers[-1])
            #print(number)
            s += number
print(s)