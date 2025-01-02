DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

def process_input(input):
    map = []
    with open(input, 'r') as file:
        for line in file:
            line = [int(n) for n in list(line.strip())]
            map.append(line)
    return map

def part1(map):
    ans = 0
    reached = set()
    def dfs(val, r, c):
        nonlocal ans
        if not validPos(r,c, map) or map[r][c] - val != 1 or (r,c) in reached:
            return
        if map[r][c] == 9 and map[r][c] - val == 1:
            ans += 1
            reached.add((r,c))
            return
        for dr, dc in DIRS:
            dfs(map[r][c], r+dr, c+dc)
            
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 0:
                for dr, dc in DIRS:
                    dfs(0, r+dr, c+dc)
                reached.clear()
    return ans

def part2(map):
    ans = 0
    def dfs(val, r, c):
        nonlocal ans
        if not validPos(r,c, map) or map[r][c] - val != 1:
            return
        if map[r][c] == 9 and map[r][c] - val == 1:
            ans += 1
            return
        for dr, dc in DIRS:
            dfs(map[r][c], r+dr, c+dc)
            
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 0:
                for dr, dc in DIRS:
                    dfs(0, r+dr, c+dc)
    return ans



def validPos(r, c, map):
    return 0 <= r < len(map) and 0 <= c < len(map[0])

def solve_day(input):
    map = process_input(input)
    print('Day 1 answer is: ', part1(map))
    print('Day 2 answer is: ', part2(map))

solve_day('input.txt')
