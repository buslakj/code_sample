# Advent of code: https://adventofcode.com/2024/day/1
# Helper function that reads a two-column text file and returns two lists.

def converts_columns_to_lists_helper(file_path):

    with open(file_path, 'r') as file:
        column1 = []
        column2 = []
        for line in file:
            values = line.strip().split() 
            if len(values) == 2:  
                column1.append(int(values[0]))
                column2.append(int(values[1]))

    return column1, column2

# Advent of Code Day 1: part 1

def compare_lists(list_1, list_2):
    list_1.sort()
    list_2.sort()
 
    if len(list_1) != len(list_1):
        return "Lists cannot be compared"
        
    result = 0
    for i in range(len(list_1)):
        result += abs(list_1[i] - list_2[i])
    return result

# Advent of Code Day 1: part 2

def gen_similarity_score(list_1, list_2):
    result = 0
    for id in list_1:
        result += id * list_2.count(id)
    return result

file = 'sample_2/data.txt'
l1, l2 = converts_columns_to_lists_helper(file)

compare_lists(l1, l2)
gen_similarity_score(l1,l2)