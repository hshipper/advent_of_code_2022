import re

def import_crate_rows():

    box_rows = []
    in_box_declaration = True

    with open("day5/input.txt", "r") as input:
        while in_box_declaration:
            for line in input:
                if line.strip() == '':
                    return box_rows
                box_rows.append(line.rstrip())

def transpose_crates_to_stacks(box_rows):

    # number of stacks is defined in the last row
    n_stacks = int(box_rows[-1][-1])

    # initialize n_stack lists
    stacks = [list() for i in range(n_stacks)]

    # put crates in appropriate stacks
    # start by limiting to just rows with stacks, then reversing order 
    for row in box_rows[:-1][::-1]:
        
        char_number = 0

        for char in row:
            # crates are in columns (0-indexed) 1, 5, 9, etc.
            # if char number + 3 is divisible by 4 and there is a letter in the column, put it in the appropriate stack
            if ((char_number + 3) % 4 == 0) & (re.match(r'[A-Z]', char) is not None):
                # 1 -> 0, 5 -> 1, 9 -> 2, etc.
                stacks[int((char_number + 3) / 4) - 1].append(char)
            char_number += 1

    return stacks

def read_instructions():

    instructions = []

    with open("day5/input.txt", "r") as input:
        for line in input:
            if re.match(r'm', line):
                split_line = line.split()
                instructions.append([int(value) for value in split_line if re.match(r'[0-9]+', value)])
    
    return instructions

def execute_instructions(stacks: list, instructions: list):

    for instruction in instructions:

        # rename instructions for readability
        n_crates = instruction[0]
        source = instruction[1] - 1
        destination = instruction[2] - 1

        # copy crates to new stack then delete
        stacks[destination].extend(stacks[source][-n_crates:])
        del stacks[source][-n_crates:]

    return stacks

def get_top_letters(stacks:list):

    top_letters = list(map(lambda x: x[-1], stacks))
    result_string = ('').join(top_letters)
    return(result_string)

if __name__ == '__main__':
    stacks = transpose_crates_to_stacks(box_rows=import_crate_rows())
    instructions = read_instructions()
    organized_stacks = execute_instructions(stacks = stacks, instructions = instructions)
    print(get_top_letters(organized_stacks))