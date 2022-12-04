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


def sum_badge_priorities():

    # initialize line index, reset after i = 2
    i = 0
    total_badge_priorities = 0
    current_matches = set()

    with open("day3/input.txt", "r") as input:
        for line in input:
            line = line.strip()
            line_priorities = [convert_letter_to_priority(letter) for letter in line]
            if i == 0:
                current_matches = set(line_priorities)
            else:
                current_matches = set(line_priorities).intersection(current_matches)
            if i == 2:
                total_badge_priorities += sum(current_matches)
            i = (i + 1) % 3
            print(f'current matches: {current_matches} | total badge priorities: {total_badge_priorities}')

    print(total_badge_priorities)
    return(total_badge_priorities)
        
if __name__ == '__main__':
    sum_badge_priorities()