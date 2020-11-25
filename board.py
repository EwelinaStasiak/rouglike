import random
from termcolor import colored

def load_board(path):
    board = []
    f = open(path + "board_2.txt", "r")
    
    init_board = f.readlines()
    
    for line in init_board:
        board.append(list(line))
    
    return board

# def create_regular_board(width = 60, hight = 20, space_sign = ".", vertic_sign = "|", horis_sign = "#"):
#     board = []

#     for num in range(hight):
#         if num == 0 or num == hight - 1:
#             board.append([horis_sign] * width)
#         else:
#             board.append([vertic_sign] + [space_sign] * (width - 2) + [vertic_sign])
    
#     return board



def print_a_board():
    board = load_board("/Users/kt/OneDrive/Codecool/Projekty/Rogue_like_game/")
    EXIT = ["E", "X", "I", "T"]

    for row in board:
        for el in row:
            if el in EXIT:
                print(colored(el, "green"), end = "")
            else:
                print(el, end = "")

def main():
    print_a_board()

if __name__ == "__main__":
    main()


