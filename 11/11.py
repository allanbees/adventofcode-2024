from collections import Counter

def process_input(input):
    rocks = []
    with open(input, 'r') as file:
        rocks = [rock for line in file for rock in line.split()]
    return rocks


def blink(rock):
    if rock == '0':
        return ['1']
    elif len(rock) % 2 == 0:
        length = len(rock)
        rock1 = rock[:length//2]
        rock2 = rock[length//2:]
        return [str(int(rock1)), str(int(rock2))]
    else:
        return [str(int(rock) * 2024)]

def part1(rocks):
    ans = rocks
    for _ in range(25):
        new = []
        for rock in ans:
            new.extend(blink(rock))
        ans = new
    return len(ans)
    
def part2(rocks):
    ans = Counter(rocks)
    for _ in range(75):
        new = Counter()
        for rock, occurences in ans.items():
            for r in blink(rock):
                if r in new:
                    new[r] += 1 * occurences
                else:
                    new[r] = 1 * occurences
        ans = new
    return sum(ans.values())

def solve_day(input):
    rocks = process_input(input)
    print('Day 1 answer is: ', part1(rocks))
    print('Day 2 answer is: ', part2(rocks))

solve_day('input.txt')
