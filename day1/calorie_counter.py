
def most_calories():
    # initialize most calories
    most_calories = 0

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
                if calorie_total > most_calories:
                    most_calories = calorie_total
                calories_to_add = []

    print(most_calories)
    return most_calories

if __name__ == "__main__":
    most_calories()
