import string

def part1(map):
    # For every antenna we find, check on the possible directions that differ by 2 if there are other antennas and make pair
    antenna_pairs = {}
    for r in range(len(map)):
      for c in range(len(map[0])):
        if is_antenna(map[r][c]):
          pairs = find_pairs(r, c, map)
          if pairs:
            antenna_pairs[(r,c)] = pairs
    # Now we got the antennas with their pairs, we can add the antinodes in the map
    ans = 0
    checked = set()
    for ant in antenna_pairs:
      for r, c in antenna_pairs[ant]:
        ant_r, ant_c = ant 
        new_r, new_c = r+(r-ant_r), c+(c-ant_c)
        if valid_pos(new_r, new_c, map) and (new_r, new_c) not in checked:
          if map[new_r][new_c] == '.':
            map[new_r][new_c] = '#'
          ans += 1
          checked.add((new_r, new_c))
    return ans

def part2(map):
  # For every antenna we find, check on the possible directions that differ by 2 if there are other antennas and make pair
    antenna_pairs = {}
    for r in range(len(map)):
      for c in range(len(map[0])):
        if is_antenna(map[r][c]):
          pairs = find_pairs(r, c, map)
          if pairs:
            antenna_pairs[(r,c)] = pairs
    # Now we got the antennas with their pairs, we can add the antinodes in the map
    ans = 0
    checked = set()
    for ant in antenna_pairs:
      for r, c in antenna_pairs[ant]:
        ant_r, ant_c = ant 
        dr, dc = (r-ant_r), (c-ant_c)
        new_r, new_c = r+dr, c+dc
        while valid_pos(new_r, new_c, map):
          if map[new_r][new_c] == '.':
            map[new_r][new_c] = '#'
            if (new_r, new_c) not in checked:
              ans += 1
          checked.add((new_r, new_c))
          new_r, new_c = new_r+dr, new_c+dc
    for ant in antenna_pairs:
      appearances = 0
      for ant2 in antenna_pairs:
        if ant != ant2 and ant in antenna_pairs[ant2]:
          appearances += 1
      if appearances == len(antenna_pairs[ant]):
        ans += 1
    return ans

def find_pairs(row, col, map):
  pairs = []
  for r in range(len(map)):
    for c in range(len(map[0])):
      if is_antenna(map[r][c]) and (r,c) != (row, col) and map[row][col] == map[r][c]:
        pairs.append((r, c))
  return pairs

def valid_pos(r,c,map):
  return 0 <= r < len(map) and 0 <= c < len(map[0])

def is_antenna(char):
  return char in string.digits or char in string.ascii_letters

def process_input(input):
    antennas_map = []
    with open(input, 'r') as file:
        for line in file:
            line = list(line.strip())
            antennas_map.append(line)
    return antennas_map

def solve_day(input):
    map = process_input(input)
    print('Day 1 answer is: ', part1(map))
    map = process_input(input)
    print('Day 2 answer is: ', part2(map))

solve_day('input.txt')
