def process_input(filename):
    input = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            parsed_line = list(line)
            if parsed_line[-1] == '\n':
                parsed_line.pop()
            input.append(parsed_line)
    return input

def part1(input):
    xmas = 0
    directions = [(1,0), (-1,0), (0,1),(0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == 'X':
                for dr, dc in directions:
                    i = 0
                    curr = ''
                    x, y = r, c
                    while isInbound(x, y, input) and i < 4:
                        curr += input[x][y]
                        x, y = x+dr, y+dc
                        i += 1
                    if curr == 'XMAS':
                        xmas+=1
    return xmas

def part2(input):
    mas = 0
    diag1 = [(1,1), (-1,-1)]
    diag2 = [(-1,1), (1,-1)]
    for r in range(len(input)):
        for c in range(len(input[0])):
            curr1 = ''
            curr2 = ''
            if input[r][c] == 'A':
                x, y = r, c
                curr1 += 'A'
                curr2 += 'A'
                for dx, dy in diag1:
                    if isInbound(x+dx, y+dy, input):
                        curr1 += input[x+dx][y+dy]
                for dx, dy in diag2:
                    if isInbound(x+dx, y+dy, input):
                        curr2 += input[x+dx][y+dy]
                curr1 = ''.join(sorted(curr1))
                curr2 = ''.join(sorted(curr2))
                if curr1 == curr2 == 'AMS':
                    mas += 1
    return mas

def isInbound(r,c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def solve_day(filename):
    input = process_input(filename)
    # Part 1:
    print("Part 1 answer is: ", part1(input))
    # Part 2
    print("Part 2 answer is: ", part2(input))


solve_day('input.txt')