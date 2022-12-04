def play_rps():

    # initialize total score
    total_score = 0
    i = 0

    with open("day2/input.txt", "r") as input:
        for line in input:
            # use ord(str) - 64 and ord(str) - 87 to make comparisons
            # ord('A') == 65    
            plays = [ord(play) for play in line.split()]
            opponent_shape = plays[0] - 64
            # lose, draw, win
            desired_result = plays[1] - 88
            # term to add
            addends = [2, 0, 1]
            # Z first, since 3 mod 3 = 0
            shapes = [3, 1, 2]
            # opponent_shape + added mod 3 gets us the value to add to total score
            total_score += desired_result * 3 + shapes[(opponent_shape + addends[desired_result]) % 3]
    
    
    print(total_score)
    return(total_score)
            



if __name__ == '__main__':
    play_rps()


