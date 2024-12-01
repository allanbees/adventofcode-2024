from collections import Counter

def process_input(filename):
    left = []
    right = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            line_split = line.split()
            left.append(int(line_split[0]))
            right.append(int(line_split[1]))
    left.sort(), right.sort()
    return left, right
        
            

def get_distance(left, right):
    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    return distance

def get_similarity_score(left, right):
    score = 0
    counter_right = Counter(right)
    for num in left:
        freq = counter_right.get(num, 0)
        score += num * freq
    return score

def solve_day(filename):
    left, right = process_input(filename)
    # Part 1:
    print("Part 1 answer is: ", get_distance(left, right))
    # Part 2
    print("Part 2 answer is: ", get_similarity_score(left, right))


solve_day('input.txt')