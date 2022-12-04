def sum_top_three_calories():
    # list of calorie counts
    calorie_counts = []

    with open("day1/input.txt", 'r') as input:
        # initialize list for calorie totals to add
        calories_to_add = []
        for line in input:
            new_value = line.strip()
            calories_to_add.append(new_value)
            if new_value == '':
                # if the most recently read value was not a number, add the previous ones together then reset
                calories_to_add.pop()
                calories_to_add = [int(calories) for calories in calories_to_add]
                calorie_total = sum(calories_to_add)
                calorie_counts.append(calorie_total)
                calories_to_add = []

    calorie_counts.sort(reverse=True)
    top_three_counts = calorie_counts[0:3]
    print(top_three_counts)
    print(sum(top_three_counts))
    return(sum(top_three_counts))

if __name__ == "__main__":
    sum_top_three_calories()
