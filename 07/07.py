from collections import defaultdict

def part1(equations):
    ans = 0
    for target in equations:
      values = equations[target]
      if dfs(1, values[0], target, values):
        ans += target
    return ans

def dfs(i, res, target, values):
    if i == len(values):
      return res == target
    return dfs(i+1, res + values[i], target, values) or dfs(i+1, res * values[i], target, values)

def dfs2(i, res, target, values):
    if i == len(values):
      return str(res) == str(target)
    return dfs2(i+1, str(res) + str(values[i]), target, values) or dfs2(i+1, int(res) + int(values[i]), target, values) or dfs2(i+1, int(res) * int(values[i]), target, values)

def part2(equations):
    ans = 0
    for target in equations:
      values = equations[target]
      if dfs2(1, values[0], target, values):
        ans += target
    return ans

def process_input(input):
    equations = {}
    with open(input, 'r') as file:
        for line in file:
            line = line.split(':')
            target = int(line[0])
            numbers = [ int(n.strip()) for n in line[1].split()]
            equations[target] = numbers
    return equations
     
def solve_day(input):
    equations = process_input(input)
    print('Day 1 answer is: ', part1(equations))
    print('Day 2 answer is: ', part2(equations))
    
solve_day('input.txt')
