import re

def process_input(filename):
    input = ''
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            input += line
    return input

def part1(input):
    operations = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
    results = 0
    for op in operations:
        numbers = re.findall(r'\d{1,3}', op)
        x, y = int(numbers[0]), int(numbers[1])
        results += x*y
    
    return results

def part2(input):
    operations = re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', input)
    do = True
    results = 0
    for op in operations:
        if op == 'don\'t()':
            do = False
        elif op == 'do()':
            do = True
        else:
            if do:
                numbers = re.findall(r'\d{1,3}', op)
                x, y = int(numbers[0]), int(numbers[1])
                results += x*y
    return results


def solve_day(filename):
    input = process_input(filename)
    # Part 1:
    print("Part 1 answer is: ", part1(input))
    # Part 2
    print("Part 2 answer is: ", part2(input))


solve_day('input.txt')