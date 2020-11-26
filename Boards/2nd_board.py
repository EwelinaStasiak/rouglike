import random

def create_board(hight = 41, width = 81, space = " ", vert_boarder = " ", horis_boarder = " "):
    board = []
    first_last_row = [0, hight - 1]

    for num in range(hight):
        if num in first_last_row:
            board.append([horis_boarder] * width)
        else:
            board.append([vert_boarder] + [space] * (width - 2) + [vert_boarder])
    
    return board

def sec_board(board):
    road_banch = [14, 22]
    road_strips = [" ", "–"]

    for index in road_banch:
        board[index][1 : 80] = ["–"] * 79
    
    midle_road_index = 1
    while midle_road_index < 77:
        for el in road_strips:
            board[18][midle_road_index : midle_road_index + 2] = [el] * 2
            midle_road_index += 2
    
    return board

def car_placement(board):
    car = 20

    while car > 0:
        road_indices = [15, 16, 17, 19, 20, 21]
        row_index = random.choice(road_indices)
        col_index = random.randint(1, 78)
        
        if board[row_index][col_index] == " " and board[row_index][col_index + 2] == " ":
            board[row_index][col_index : col_index + 2] = ["C"] * 2
            car -= 1
    
    return board

def print_a_board(board):
    for row in board:
        for el in row:
            print(el, end = "")
        print()

def main():
    board = create_board(41, 81, " ", "#", "#")
    board = sec_board(board)
    board = car_placement(board)
    print_a_board(board)

main()