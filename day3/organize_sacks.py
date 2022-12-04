# convert letters to priorities
# a is priority 1, z 26
# A is priority 27, Z 52
def convert_letter_to_priority(letter:str):
    if letter.isupper():
        # ord('A') = 65
        return(ord(letter) - 38)
    else:
        # ord('a') = 97
        return(ord(letter) - 96)


def sum_matched_elements():
    # maintain set of elements in both halves of each sack
    total_matched_priorities = 0

    # split rucksacks in half
    with open("day3/input.txt", "r") as input:
        for line in input:
            line = line.strip()
            midpoint = int(len(line) / 2)
            compartment_1, compartment_2 = line[:midpoint], line[midpoint:]
            compartment_1_priorities = [convert_letter_to_priority(letter) for letter in compartment_1]
            compartment_2_priorities = [convert_letter_to_priority(letter) for letter in compartment_2]
            matches = set(compartment_1_priorities).intersection(compartment_2_priorities)
            total_matched_priorities += sum(matches)
            print(f'line matches: {matches} | overall matches: {total_matched_priorities}')

    print(total_matched_priorities)
    return(total_matched_priorities)
        
if __name__ == '__main__':
    sum_matched_elements()