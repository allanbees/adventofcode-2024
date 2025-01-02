from collections import defaultdict
from itertools import product

DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

def process_input(input):
    garden = []
    with open(input, 'r') as file:
        garden = [[plot for plot in line.strip()] for line in file]
    return garden

def part1(garden):
    perims, regions = get_perimeters(garden)
    ans = 0
    for region in regions:
        ans += len(regions[region]) * perims[region]
    return ans
    
    
    
def part2(garden):
    sides, regions = get_sides(garden)
    ans = 0
    for region in regions:
        ans += len(regions[region]) * sides[region]
    return ans

def get_regions(garden):
    regions = defaultdict(list)
    visited = set()
    regionId = 1
    
    def dfs(r,c, type):
        nonlocal regionId
        if not valid_pos(r, c, garden) or garden[r][c] != type or (r,c) in visited:
            return
        visited.add((r,c))
        regions[regionId].append((r,c))
        for dr, dc in DIRS:
            dfs(r+dr, c+dc, type)
        
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if (r,c) not in visited:
                dfs(r, c, garden[r][c])
                regionId += 1
    return regions

def get_perimeters(garden):
    regions = get_regions(garden)
    perimeters = {}
    for region in regions:
        currPerim = 0
        for plot in regions[region]:
            r, c = plot
            type = garden[r][c]
            for dr, dc in DIRS:
                if not valid_pos(r+dr, c+dc, garden) or garden[r+dr][c+dc] != type:
                    currPerim += 1
        perimeters[region] = currPerim + perimeters.get(region, 0)
    return perimeters, regions

def get_sides(garden):
    regions = get_regions(garden)
    sides = {}
    for region in regions:
        currSides = 0
        for plot in regions[region]:
            r, c = plot
            for dr, dc in product([1,-1], repeat=2):
                row_nei = (r+dr, c)
                col_nei = (r, c+dc)
                diag_nei = (r+dr, c+dc)
                
                if row_nei not in regions[region] and col_nei not in regions[region]:
                    currSides += 1
                if row_nei in regions[region] and col_nei in regions[region] and diag_nei not in regions[region]:
                    currSides += 1
        sides[region] = currSides + sides.get(region, 0)
    return sides, regions
    
    
def valid_pos(r, c, garden):
    return 0 <= r < len(garden) and 0 <= c < len(garden[0])

def solve_day(input):
    garden = process_input(input)
    print('Day 1 answer is: ', part1(garden))
    print('Day 2 answer is: ', part2(garden))

solve_day('input.txt')
