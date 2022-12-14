file1 = open('input', 'r')
Lines = file1.readlines()

total_full_overlap = 0
total_general_overlap = 0

for string in Lines:
    parts = string.strip('\n').split(',')

    left = parts[0]
    right = parts[1]

    def get_range(chores):
        numbers = chores.split('-')
        numbers = [int(n) for n in numbers]

        numbers_range = range(numbers[0], numbers[1]+1)
        return set(numbers_range)

    
    left_range = get_range(left)
    right_range = get_range(right)
    
    #part1
    if left_range >= right_range or right_range >= left_range:
        total_full_overlap += 1
    #part2
    if left_range & right_range:
        total_general_overlap += 1

print(f"The total tasks containing others is: {total_full_overlap}\nTotal tasks mixed is: {total_general_overlap} ")


