import random
import player

def create_board(hight = 41, width = 81, space = " ", vert_boarder = " ", horis_boarder = " "):
    board = []
    first_last_row = [0, hight - 1]

    for num in range(hight):
        if num in first_last_row:
            board.append([horis_boarder] * width)
        else:
            board.append([vert_boarder] + [space] * (width - 2) + [vert_boarder])
    
    return board

def generate_chembers():
    chembers = []
    hight_and_width = {}

    for num in range(1, 4):
        hight = random.randint(10, 15)
        width = random.randint(15, 30)
        chembers.append(create_board(hight, width, " ", "#", "#"))
        hight_and_width[num] = (hight, width)
    
    return chembers, hight_and_width

def random_chembers_indices(board_hight, board_width, first_row_col, hight_and_width):
    chemb_1_hight, chemb_1_width = hight_and_width[1]
    chemb_2_hight, chemb_2_width = hight_and_width[2]
    chemb_3_hight, chemb_3_width = hight_and_width[3]

    random_row_1 = random.randint(first_row_col, board_hight - chemb_1_hight)
    
    if random_row_1 > chemb_2_hight:
        random_col_1 = random.randint(first_row_col, board_width - chemb_2_width)
    else:
        random_col_1 = random.randint(chemb_1_width, board_width - chemb_2_width)
    
    random_row_2 = random.randint(chemb_2_hight, board_hight - chemb_3_hight)

    if random_row_1 + chemb_1_hight < random_row_2:
        random_col_2 = random.randint(first_row_col, board_width - chemb_3_width)
    else:
        random_col_2 = random.randint(chemb_1_width, board_width - chemb_3_width)

    return random_row_1, random_col_1, random_row_2, random_col_2

def placing_chembers():
    board_hight = 31
    board_width = 81
    first_row_col = 0

    board = create_board(board_hight, board_width)
    available_coordinates = []

    chembers, hight_and_width = generate_chembers()
    chember_1, chember_2, chember_3 = chembers
    row_1, col_1, row_2, col_2 = random_chembers_indices(board_hight, board_width, first_row_col, hight_and_width)

    board, available_coordinates = placing_1st_chember(board, chember_1, row_1, available_coordinates)
    board, available_coordinates = placing_2nd_chember(board, chember_2, col_1, available_coordinates)
    board, available_coordinates = placing_3rd_chember(board, chember_3, row_2, col_2, available_coordinates)

    return board, available_coordinates

def placing_1st_chember(board, chember_1, row_1, available_coordinates):
    for row_num in range(len(chember_1)):
        n = 0
        for el in chember_1[row_num]:
            board[row_1][n] = el
            available_coordinates.append((row_1, n))
            n += 1
        row_1 += 1
    
    return board, available_coordinates

def placing_2nd_chember(board, chember_2, col_1, available_coordinates):
    for row_num in range(len(chember_2)):
        n = 0
        r_col = col_1
        for col in chember_2[row_num]:
            board[row_num][r_col] = col
            available_coordinates.append((row_num, r_col))
            r_col += 1
            n += 1
    
    return board, available_coordinates

def placing_3rd_chember(board, chember_3, row_2, col_2, available_coordinates) :
    for row_num in range(len(chember_3)):
        n = 0
        col = col_2
        for el in chember_3[row_num]:
            board[row_2][col] = el
            available_coordinates.append((row_2, col))
            col += 1
        row_2 += 1

    return board, available_coordinates

# def placing_chembers():
#     board_hight = 31
#     board_width = 81
#     board = create_board(board_hight, board_width)
#     first_row_col = 0
#     last_row = board_hight - 1
#     last_col = board_width - 1

#     chembers, hight_and_width = generate_chembers()
#     chember_1, chember_2, chember_3 = chembers
#     chemb_1_hight, chemb_1_width = hight_and_width[1]
#     chemb_2_hight, chemb_2_width = hight_and_width[2]
#     chemb_3_hight, chemb_3_width = hight_and_width[3]

#     random_row_1 = random.randint(first_row_col, board_hight - chemb_1_hight)
    
#     if random_row_1 > chemb_2_hight:
#         random_col_1 = random.randint(first_row_col, board_width - chemb_2_width)
#     else:
#         random_col_1 = random.randint(chemb_1_width, board_width - chemb_2_width)
    
#     random_row_2 = random.randint(chemb_2_hight, board_hight - chemb_3_hight)

#     if random_row_1 + chemb_1_hight < random_row_2:
#         random_col_2 = random.randint(first_row_col, board_width - chemb_3_width)
#     else:
#         random_col_2 = random.randint(chemb_1_width, board_width - chemb_3_width)


#     for row_num in range(len(chember_1)):
#         board[random_row_1][first_row_col : chemb_1_width] = chember_1[row_num]
#         random_row_1 += 1
    
#     for row_num in range(len(chember_2)):
#         board[row_num][random_col_1 : random_col_1 + chemb_2_width - 1] = chember_2[row_num]
    
#     for row_num in range(len(chember_3)):
#         board[random_row_2][random_col_2 : random_col_2 + chemb_3_width - 1] = chember_3[row_num]
#         random_row_2 += 1

    

#     return board

def print_a_board(board):
    for row in board:
        for el in row:
            print(el, end = "")
        print()

def main():
    board, available_coordinates = placing_chembers()
    print_a_board(board)
    print(len(available_coordinates))

if __name__ == "__main__":
    main()