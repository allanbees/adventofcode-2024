from collections import defaultdict

def process_input(input):
    claws = defaultdict(list)
    with open(input, 'r') as file:
        key = 1
        for line in file:
            new = line.split()
            if not new:
                key += 1
                continue
            claws[key].append(new)
    for key in claws:
        X_tuple = (int(claws[key][0][2].split('+')[1].split(',')[0]), int(claws[key][1][2].split('+')[1].split(',')[0]))
        Y_tuple = (int(claws[key][0][3].split('+')[1]), int(claws[key][1][3].split('+')[1]))
        prize_tuple = (int(claws[key][2][1].split('=')[1].split(',')[0]), int(claws[key][2][2].split('=')[1]))
        claws[key] = [X_tuple, Y_tuple, prize_tuple]
    return claws

def process_input2(input):
    claws = defaultdict(list)
    with open(input, 'r') as file:
        key = 1
        for line in file:
            new = line.split()
            if not new:
                key += 1
                continue
            claws[key].append(new)
    for key in claws:
        X_tuple = (int(claws[key][0][2].split('+')[1].split(',')[0]), int(claws[key][1][2].split('+')[1].split(',')[0]))
        Y_tuple = (int(claws[key][0][3].split('+')[1]), int(claws[key][1][3].split('+')[1]))
        prize_tuple = (10000000000000+int(claws[key][2][1].split('=')[1].split(',')[0]), 10000000000000+int(claws[key][2][2].split('=')[1]))
        claws[key] = [X_tuple, Y_tuple, prize_tuple]
    return claws

def part1(claws): 
    ans = 0
    for key in claws:
        A1, B1 = claws[key][0]
        A2, B2 = claws[key][1]
        prize1, prize2 = claws[key][2]
        a, b = find_intersection(A1, A2, B1, B2, prize1, prize2)
        if a.is_integer() and b.is_integer():
            ans += a*3 + b
    return ans

def find_intersection(
    a_x: int, a_y: int, b_x: int, b_y: int, x_prize: int, y_prize: int
) -> tuple[float, float]:
    # step 1
    a_x_with_b_y = a_x * b_y
    x_prize_with_b_y = x_prize * b_y
    # step 1.5
    a_y_with_b_x = a_y * b_x
    y_prize_with_b_x = y_prize * b_x
    a = (x_prize_with_b_y - y_prize_with_b_x) / (a_x_with_b_y - a_y_with_b_x)
    b = (y_prize - a_y * a) / b_y

    return a, b
    
def part2(claws):
    ans = 0
    for key in claws:
        A1, B1 = claws[key][0]
        A2, B2 = claws[key][1]
        prize1, prize2 = claws[key][2]
        a, b = find_intersection(A1, A2, B1, B2, prize1, prize2)
        if a.is_integer() and b.is_integer():
            ans += a*3 + b
    return ans

def solve_day(input):
    claws = process_input(input)
    print('Day 1 answer is: ', part1(claws))
    claws = process_input2(input)
    print('Day 2 answer is: ', part2(claws))

solve_day('input.txt')
