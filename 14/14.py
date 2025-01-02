def process_input(input):
    robots = {}
    with open(input, 'r') as file:
        id_robot = 1
        for line in file:
            new = line.split()
            pos = new[0].split('=')
            pos = pos[1].split(',')
            pos = (int(pos[1]), int(pos[0]))
            velocities = new[1].split('=')
            velocities = velocities[1].split(',')
            velocities = (int(velocities[1]), int(velocities[0]))
            robots[id_robot] = [pos, velocities]
            id_robot += 1
    return robots

def create_grid(ROWS, COLS):
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def init_restroom(robots, restroom):
    ROWS, COLS = len(restroom), len(restroom[0])
    restroom_copy = restroom
    for id in robots:
        r, c = robots[id][0]
        if inquad(r,c,ROWS,COLS):
            restroom_copy[r][c] += 1
    return restroom_copy

def part1(restroom, robots): 
    ans = 1
    ROWS, COLS = len(restroom), len(restroom[0])
    for _ in range(100):
        for id in robots:
            prev_r, prev_c = robots[id][0]
            restroom[prev_r][prev_c] -= 1
            offset_r, offset_c = robots[id][1]

            new_r = (prev_r+offset_r) % ROWS
            new_c = (prev_c+offset_c) % COLS 
            restroom[new_r][new_c] += 1
            robots[id][0] = (new_r, new_c)
    quadrants = {}
    for r in range(ROWS):
        for c in range(COLS):
            if inquad(r,c,ROWS,COLS): 
                quad_r = 0 if r < ROWS//2 else 1
                quad_c = 0 if c < COLS//2 else 1
                quadrants[(quad_r, quad_c)] = restroom[r][c] + quadrants.get((quad_r, quad_c), 0)
    for quad in quadrants:
        ans *= quadrants[quad] if quadrants[quad] else 1  
    return ans

def inquad(r,c, rows, cols):
    return (r < rows//2 and c < cols//2) or (r < rows//2 and c > cols//2) or (r > rows//2 and c < cols//2)or (r > rows//2 and c > cols//2)

def part2(robots): 
    ans = 1
    COLS, ROWS = 101, 103
    minn = float('inf')
    for it in range(8400):
        a = b = c = d = 0
        for id in robots:
            prev_r, prev_c = robots[id][0]
            offset_r, offset_c = robots[id][1]

            new_r = (prev_r+offset_r) % ROWS
            new_c = (prev_c+offset_c) % COLS
            
            a += new_r > ROWS//2 and new_c > COLS//2
            b += new_r > ROWS//2 and new_c < COLS//2
            c += new_r < ROWS//2 and new_c > COLS//2
            d += new_r < ROWS//2 and new_c < COLS//2
            robots[id][0] = (new_r, new_c)
        curr = a*b*c*d
        if curr < minn:
            minn = curr
            ans = it
    return ans

def solve_day(input):
    robots = process_input(input)
    empty_restroom = create_grid(103, 101)
    restroom = init_restroom(robots, empty_restroom)
    print('Day 1 answer is: ', part1(restroom, robots))
    robots2 = process_input(input)
    print('Day 2 answer is: ', part2(robots2))

solve_day('input.txt')
