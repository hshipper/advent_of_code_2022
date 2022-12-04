def play_rps():

    # initialize total score
    total_score = 0

    with open("day2/input.txt", "r") as input:
        for line in input:
            # use ord(str) - 64 and ord(str) - 87 to make comparisons
            # ord('A') == 65    
            plays = [ord(play) for play in line.split()]
            # equalize our play with opponent, then subtract
            result = plays[1] - plays[0] - 23
            # add our guess to total score
            # if result == 0, draw & 3 points
            # if result is 1 or -2, win & 6 points
            multipliers = [1, 2, 0]
            total_score += (plays[1] - 87) + (multipliers[result] * 3)

    print(total_score)
    return(total_score)

if __name__ == '__main__':
    play_rps()


