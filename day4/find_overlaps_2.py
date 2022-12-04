# import re to enable splitting on multiple delimiters at once
import re

def check_overlap(endpoints):
    
    # add one to terminal end of range to make it inclusive
    range_1, range_2 = range(endpoints[0], endpoints[1] + 1), range(endpoints[2], endpoints[3] + 1)

    n_intersecting_values = len(set(list(range_1)).intersection(list(range_2)))

    # if the intersection is the same size as one of the ranges, it is fully overlapped
    if  n_intersecting_values > 0:
        return True
    else:
        return False
    

def count_overlapping_assignments():

    total_overlapping_assignments = 0

    with open("day4/input.txt", "r") as input:
        for line in input:
            endpoint_strings = re.split(r'\D', line.strip())
            endpoints = [int(endpoint) for endpoint in endpoint_strings]
            total_overlapping_assignments += check_overlap(endpoints)

    print(total_overlapping_assignments)
    return(total_overlapping_assignments)

if __name__ == "__main__":
    count_overlapping_assignments()