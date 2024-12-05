def process_input(filename):
    reports = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            reports.append([int(c) for c in line.split()])
    return reports        

def get_safe_reports(reports):
    safe_count = 0
    for report in reports:
        safe = True
        # Check if is increasing
        isIncreasing = False
        isDecreasing = False
        for i in range(1, len(report)):
            if report[i] > report[i-1]:
                isIncreasing =  True
                break
            if report[i] < report[i-1]:
                isDecreasing =  True
                break
        if isIncreasing:
            for i in range(1, len(report)):
                diff = abs(report[i] - report[i-1])
                if report[i] < report[i-1] or diff == 0 or diff > 3:
                    safe = False
        # Check if is decreasing
        if isDecreasing:
            for i in range(1, len(report)):
                diff = abs(report[i] - report[i-1])
                if report[i] > report[i-1] or diff == 0 or diff > 3:
                    safe = False
        if safe:
            safe_count += 1
    return safe_count

def part2(reports):
    def is_safe(report):
        diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
        return all(diff in [1, 2, 3] for diff in diffs) or all(diff in [-1, -2, -3] for diff in diffs)

    def generate_variations(report):
        # Generate all reports with one level removed
        return [report[:i] + report[i + 1:] for i in range(len(report))]

    safe_count = 0

    for report in reports:
        # Check if the original report or any of its variations is safe
        if is_safe(report) or any(is_safe(variation) for variation in generate_variations(report)):
            safe_count += 1

    return safe_count

def solve_day(filename):
    reports = process_input(filename)
    # Part 1:
    print("Part 1 answer is: ", get_safe_reports(reports))
    # Part 2:
    print("Part 2 answer is: ", part2(reports))


solve_day('input.txt')