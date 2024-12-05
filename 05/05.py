from collections import defaultdict

def process_input(rules_file, pages_file):
    rules = []
    pages = []
    with open(rules_file, 'r') as file:
        # Read each line in the file
        for rule in file:
            parsed_rule = rule.split('|')
            parsed_rule[-1] = parsed_rule[-1].strip()
            parsed_rule = [int(n) for n in parsed_rule]
            rules.append(parsed_rule)
    with open(pages_file, 'r') as file:
        # Read each line in the file
        for page in file:
            parsed_page = page.split(',')
            parsed_page[-1] = parsed_page[-1].strip()
            parsed_page = [int(n) for n in parsed_page]
            pages.append(parsed_page)
    return rules, pages

def part1(pages_rules, pages):
    valid_pages = []
    ans = 0
    for page in pages:
        safe = True
        for i in range(len(page)):
            curr = page[i]
            left = page[:i]
            right = page[i+1:]
            if not is_safe(pages_rules, curr, left, right):
                safe = False
                break
        if safe:
            valid_pages.append(page)
    for page in valid_pages:
        mid = len(page) // 2
        ans += page[mid]
    return ans




def part2(pages_rules, pages):
    invalid_pages = []
    ans = 0
    for page in pages:
        unsafe = False 
        for i in range(len(page)):
            left, right = page[:i], page[i+1:]
            if not is_safe(pages_rules, page[i], left, right):
                unsafe = True
                break
        if unsafe:
            invalid_pages.append(page)
    safe_pages = []
    for page in invalid_pages:
        variations = generate_variations(page)
        for var in variations:
            for i in range(len(var)):
                left, right = var[:i], var[i+1:]
                if is_safe(pages_rules, var[i], left, right):
                    safe_pages.append(var)
                    break
    print(safe_pages)
    for page in safe_pages:
        mid = len(page) // 2
        ans += page[mid]
    return ans

def is_safe(rules, value, left, right):
    safe = True
    for n in left:
        if n in rules[value]['R']:
            safe = False
    for n in right:
        if n in rules[value]['L']:
            safe = False
    return safe

def generate_variations(arr):
    # Base case: if the list has only one element, return it as a single variation
    if len(arr) == 1:
        return [arr]
    
    variations = []
    for i in range(len(arr)):
        # Pick the current element
        current = arr[i]
        # Get the remaining elements
        remaining = arr[:i] + arr[i+1:]
        # Generate permutations of the remaining elements
        for perm in generate_variations(remaining):
            variations.append([current] + perm)
    
    return variations

def add_pages_rules(rules):
    pages_rules = defaultdict(lambda: {'L': set(), 'R': set()})
    for rule in rules:
        left, right = rule[0], rule[1]
        pages_rules[left]['R'].add(right)
        pages_rules[right]['L'].add(left)
    return pages_rules

def solve_day(rules_file, pages_file):
    rules, pages = process_input(rules_file, pages_file)
    pages_rules = add_pages_rules(rules)
    # Part 1:
    print("Part 1 answer is: ", part1(pages_rules, pages))
    # Part 2
    print("Part 2 answer is: ", part2(pages_rules, pages))


solve_day('input_rules.txt', 'input_pages.txt')