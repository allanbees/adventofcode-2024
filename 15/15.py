import re

dirs = {'<': (0,-1), '>': (0,1), 'v': (1,0), '^': (-1,0)}

def valid_pos(r,c, wh):
    return 0 <= r < len(wh) and 0 <= c < len(wh[0]) and wh[r][c] != '#'
             
def part1(warehouse, moves):
    R, C = len(warehouse), len(warehouse[0])
    robot = [coordinate for pair in [ [x,y] for x in range(R) for y in range(C) if warehouse[x][y] == '@'] for coordinate in pair] # Get the position of the robot. This is not that readable but makes it a one liner. First get the position [x,y] and the flattens the result
    for move in moves:
        dr, dc = dirs[move]
        r, c = robot
        if not valid_pos(r+dr,c+dc, warehouse): continue
        if warehouse[r+dr][c+dc] == '.':
            warehouse[r][c], warehouse[r+dr][c+dc], robot = '.', '@', [r+dr, c+dc]
            continue
        stk, to = [], None
        
        while valid_pos(r+dr, c+dc, warehouse):
            if warehouse[r+dr][c+dc] == '.':
                to = [r+dr, c+dc]
                break
            stk.append([r+dr, c+dc])
            r, c = r+dr, c+dc
        while stk and to:
            to_r, to_c = to
            from_r, from_c = stk.pop()
            warehouse[to_r][to_c], warehouse[from_r][from_c] = warehouse[from_r][from_c], warehouse[to_r][to_c]
            to = [from_r, from_c]
        if to:
            r, c = robot
            robot = [r+dr, c+dc]
            warehouse[r][c] = '.'
            warehouse[r+dr][c+dc] = '@'
    part1 = 0
    boxes = []
    for r in range(R):
        for c in range(C):
            if warehouse[r][c] == 'O':
                boxes.append([r,c])
    for box in boxes:
        top, left = box
        part1 += 100 * top + left
        
    return part1

#################################################################################################

def part2(grid, moves):
    def get_edges(r, c, dr):
        nonlocal stk
        if not valid_pos(r, c, warehouse) or warehouse[r][c] == '.':
            stk.append([r,c])
            print(stk)
            return
        if warehouse[r][c] == warehouse[r+dr][c]:
            get_edges(r+dr, c, dr)
        elif warehouse[r][c] == '[' and warehouse[r+dr][c] == ']':
            get_edges(r+dr, c-1, dr)
        elif warehouse[r][c] == ']' and warehouse[r+dr][c] == '[':
            get_edges(r+dr, c+1, dr)
            
    R, C = len(grid), len(grid[0])
    robot = [coordinate for pair in [ [x,y*2] for x in range(R) for y in range(C) if grid[x][y] == '@'] for coordinate in pair]
    warehouse = [['#' if (j == 0 or j == R - 1) or (i <= 1 or i >= C*2 - 2) else '.' for i in range(C*2)] for j in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                warehouse[r][c*2] = warehouse[r][c*2+1] = '#'
            if grid[r][c] == 'O':
                warehouse[r][c*2], warehouse[r][c*2+1] = '[', ']'
    R, C = len(warehouse), len(warehouse[0])
    warehouse[robot[0]][robot[1]] = '@'

    for move in moves:
        dr, dc = dirs[move]
        r, c = robot
        if not valid_pos(r+dr,c+dc, warehouse): continue
        
        if warehouse[r+dr][c+dc] == '.':
            warehouse[r][c] = '.'
            warehouse[r+dr][c+dc] = '@'
            robot = [r+dr, c+dc]
            continue
        stk, to = [], None
        if move in '<>':
            while valid_pos(r+dr, c+dc, warehouse):
                if warehouse[r+dr][c+dc] == '.':
                    to = [r+dr, c+dc]
                    break
                stk.append([r+dr, c+dc])
                c += dc
            while stk and to:
                to_r, to_c = to
                from_r, from_c = stk.pop()
                warehouse[to_r][to_c], warehouse[from_r][from_c] = warehouse[from_r][from_c], warehouse[to_r][to_c]
                to = [from_r, from_c]
            if to:
                r, c = robot
                robot = [r+dr, c+dc]
                warehouse[r][c] = '.'
                warehouse[r+dr][c+dc] = '@'
        else:
            if warehouse[r+dr][c] == '[':
                get_edges(r+dr, c, dr)
                get_edges(r+dr, c+1, dr)
            elif warehouse[r+dr][c] == ']':
                get_edges(r+dr, c, dr) 
                get_edges(r+dr, c-1, dr)
            print(stk)
            
    # for n in warehouse:
    #     print(''.join(n))

def process_input():
    grid = [re.findall(r'[.@#O]', l) for l in open('input.txt') if re.findall(r'[.@#O]', l)]
    moves = [re.findall(r'[<>v^]', l) for l in open('input.txt') if re.findall(r'[<>v^]', l)]
    return grid, [move for sublist in moves for move in sublist]

def solve_day():
    warehouse, moves = process_input()
    wh1 = [n[:] for n in warehouse]
    wh2 = [n[:] for n in warehouse]
    print('Day 1 answer is: ', part1(wh1, moves))
    print('Day 2 answer is: ', part2(wh2, moves))

solve_day()
