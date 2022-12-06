import re

def find_signal():
    
    with open("day6/input.txt", "r") as input:
        message = input.read().strip()
        print(len(message))

    i = 0

    while i < (len(message) - 4):

        print(i)
        unique_characters = len(set(message[i:i+4]))
        
        if unique_characters == 4:
            print(message[i:i + 4])
            return i + 4
        
        else:
            i += 1 # there has to be a way to skip characters efficiently

if __name__ == '__main__':
    print(find_signal())