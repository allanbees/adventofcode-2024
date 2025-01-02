def process_input(input):
    blocks = []
    with open(input, 'r') as file:
        for line in file:
            line = list(line.strip())
            blocks = list(line)
    processed_blocks = []
    curr = 0
    for i in range(len(blocks)):
        if i % 2 == 0:
            for _ in range(int(blocks[i])):
                processed_blocks.append(str(curr))
            curr += 1
            continue
        for _ in range(int(blocks[i])):
            processed_blocks.append('.')
    return processed_blocks

def part2(blocks):
    ans = 0
    idx = len(blocks)-1
    block = blocks
    while idx >= 0:
        num_idx = idx
        curr = block[idx]
        num_block = []
        empty_block = []
        if curr != '.':
            while block[num_idx] == curr:
                num_block.append(num_idx)
                num_idx -= 1
            idx = num_idx
            dot_idx = 0
            while dot_idx < idx:
                if block[dot_idx] == '.':
                    start_dot = dot_idx
                    while block[start_dot] == '.' and len(empty_block) < len(num_block):
                        empty_block.append(start_dot)
                        start_dot += 1
                    dot_idx = start_dot
                    if len(empty_block) == len(num_block):
                        while num_block:
                            pos_num, pos_dot = num_block.pop(), empty_block.pop()
                            block[pos_num], block[pos_dot] = '.', curr
                        break
                else:
                    empty_block = []
                    dot_idx += 1
            continue
        idx -= 1
    for idx, mult in enumerate(block):
        if mult != '.':
            ans += idx * int(mult)
    return ans

def solve_day(input):
    blocks = process_input(input)
    print('Day 2 answer is: ', part2(blocks))

solve_day('input.txt')
