from collections import defaultdict
import copy

DIRECTIONS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
NEXT_DIR = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
def part1(grid):
    # First get the initial position of the guard
    r, c = get_guard_pos(grid)
    # Get visited positions
    visited = get_visited_places(grid)
    return len(visited)

def part2(grid):
    # Get guard pos
    r, c = get_guard_pos(grid)
    # Get visited positions
    visited = get_visited_places(grid)
    visited.remove((r,c))
    return find_cycles(visited, grid)

def get_guard_pos(grid):
  for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == '^':
          r, c = row, col
          return r, c
  
def get_visited_places(grid):
  r, c = get_guard_pos(grid)
  visited = set()
  visited.add((r,c))
  dir = '^'
  while valid_pos(r,c, grid):
      dr, dc = DIRECTIONS[dir]
      if grid[r][c] == '#':
        # Go back one pos and change the direction when an obstacle is found
        r -= dr
        c -= dc
        dir = NEXT_DIR[dir]
      else:
        visited.add((r,c))
        r += dr
        c += dc
  return visited

def find_cycles(visited, grid):
  cycles = 0
  hit_from = defaultdict(set)
  for vr, vc in visited:
    cpgrid = copy.deepcopy(grid)
    r, c = get_guard_pos(cpgrid)
    cpgrid[vr][vc] = '#'
    dir = '^'
    while valid_pos(r,c, cpgrid):
      dr, dc = DIRECTIONS[dir]
      if cpgrid[r][c] == '#':
        # Go back one pos and change the direction when an obstacle is found
        if dir in hit_from[(r,c)]:
          cycles += 1
          break
        hit_from[(r,c)].add(dir)
        r -= dr
        c -= dc
        dir = NEXT_DIR[dir]
      else:
        r += dr
        c += dc
    hit_from.clear()

  return cycles

def valid_pos(r, c, grid):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def process_input(input):
    grid = []
    with open(input, 'r') as file:
        for line in file:
            parsed = list(line.strip())
            grid.append(parsed)
    return grid
     
def solve_day(input):
    grid = process_input(input)
    print('Day 1 answer is: ', part1(grid))
    grid = process_input(input)
    print('Day 2 answer is: ', part2(grid))
    
solve_day('input.txt')
