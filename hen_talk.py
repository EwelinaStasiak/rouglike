import util
import os
# import time  wyświetliło że nieużywane
# from termcolor import colored wyświetliło że nieużywane
import engine


sent_1 = "Greetings, mighty hedgehog!"
sent_2 = "You've been on a long and dangerous\njourney to make your dream come true."
sent_2_1 = "But beware!"
sent_3 = "There's still darkness lingering around your BELOVED APPLE. "
sent_4 = "You will have to choose between facing your deepest fears\nor abandoning your desires... and (probably) your life."
sent_5 = "Make your choice wisely!"
sent_6 = "1. I will continue! Only the PERFECT APPLE can save my soule. "
sent_7 = "2. You're right! I will not take that much of the rist. "
sent_8 = "\t   I still have family to take care of. "
arrow = "–>  "

make_your_choice = [sent_5, sent_6, sent_7, sent_8]
greetings = [sent_1, sent_2, sent_2_1, sent_3, sent_4]


def hen_starts_talking(board, greetings):

    for sent in greetings:
        talking_window = engine.create_board(8, 81, " ", "#", "#")
        os.system("cls | clear")
        dialog_window(talking_window, sent)
        engine.display_board(board)
        engine.display_board(talking_window)
        input()


def hen_gives_a_choice(board, make_your_choice, arrow):

    sent_5, sent_6, sent_7, sent_8 = make_your_choice
    up_down_keys = ["w", "s"]
    user_input = ""
    num_of_moves = 0

    choice_1 = sent_5 + "\n" + arrow + sent_6 + "\n" + "\t" + sent_7 + "\n" + sent_8
    choice_2 = sent_5 + "\n" + "\t" + sent_6 + "\n" + arrow + sent_7 + "\n" + sent_8
    
    user_choice = choice_1
    choice = "Continue"

    while user_input != '\r':
        os.system("cls | clear")
        engine.display_board(board)
        talking_window = engine.create_board(8, 81, " ", "#", "#")
        if user_input.lower() in up_down_keys:
            if num_of_moves == 0:
                #talking_window = dialog_window(talking_window, choice_2)
                user_choice = choice_2
                choice = "Abandon"
                num_of_moves += 1
            else:
                #talking_window = dialog_window(talking_window, choice_1)
                user_choice = choice_1
                choice = "Continue"
                num_of_moves = 0
            #engine.display_board(talking_window)
        # else:
        #     engine.display_board(dialog_window(talking_window, choice_1))
        talking_window = dialog_window(talking_window, user_choice)
        engine.display_board(dialog_window(talking_window, user_choice))
        user_input = util.key_pressed()

    return choice


def dialog_window(talking_window, text):

    row = 2
    col = 3

    for el in text:
        if el == "\n":
            row += 1
            col = 3
        elif el == "\t":
            col += 4
        else:
            talking_window[row][col] = el
            col += 1

    return talking_window


def talking_to_hen(board):

    global greetings, make_your_choice, arrow

    hen_starts_talking(board, greetings)

    return hen_gives_a_choice(board, make_your_choice, arrow)


def main():
    
    global greetings, make_your_choice, arrow
    board = engine.create_board(41, 81, " ", "#", "#")

    hen_starts_talking(board, greetings)
    choice = hen_gives_a_choice(board, make_your_choice, arrow)


if __name__ == "__main__":
    main()