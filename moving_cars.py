import first_board
import random
import creatures
import gen_boards
import time
import os

def car_movement(board, list_of_vehiculs):
    floor = " "
    min_col = 1
    max_col = 79

    for vehicul in list_of_vehiculs:
        row, col = vehicul["location"]
        kind = vehicul["name"]

        if kind == "Car":
            board[row][col] = floor
            if col == min_col:
                new_col = max_col
            else:
                new_col = col - 1
            board[row][new_col] = vehicul["pic"]
        elif kind == "Lorry":
            board[row][col : col + 2] = [floor] * 2
            if col == min_col:
                new_col = max_col - 1
            else:
                new_col = col - 1
            board[row][new_col : new_col+2] = [vehicul["pic"]] * 2

        vehicul["location"] = (row, new_col)

    return board, list_of_vehiculs         

def cars_in_the_move(board, list_of_vehiculs):
    while True:
        board, list_of_vehiculs =  car_movement(board, list_of_vehiculs)
        os.system("cls | clear")
        first_board.print_a_board(board)
        time.sleep(0.1)

def main():
    vehiculs = [1, 2]
    vehiculs_list = []
    on_board_vehiculs = []
    

    for vehicul in vehiculs:
        car_or_lorry = creatures.creatures()[vehicul]
        vehiculs_list.append(car_or_lorry)
        on_board_vehiculs += creatures.creatures_on_the_board_dicts(car_or_lorry)

    board = first_board.create_board(41, 81, " ", "#", "#")
    board = first_board.sec_board(board)
    board_index = gen_boards.board_indexes(board)
    board, list_of_vehiculs = creatures.car_placement(board, board_index, on_board_vehiculs)
    cars_in_the_move(board, list_of_vehiculs)

    #second_board.print_a_board(board)

if __name__ == "__main__":
    main()