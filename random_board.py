import random

def create_board(space = " ", vert_boarder = " ", horis_boarder = " ", hight = 21, width = 81):
    board = []
    first_last_row = [0, hight - 1]

    for num in range(hight):
        if num in first_last_row:
            board.append([horis_boarder] * width)
        else:
            board.append([vert_boarder] + [space] * (width - 2) + [vert_boarder])
    
    return board

def implement_chember(main_board, chember, hight, width, chemb_hight, chemb_width):
    n = 0

    for row in range(hight, hight + chemb_hight):
        main_board[row][width : width + chemb_width] = chember[n]
        n += 1

    return main_board

def implement_corridor(main_board, central_hight, central_width):
    corr_width = 3
    corr_hight = random.randint(3, 8)
    space = "."
    vert_borader = "|"
    horis_boarder =" "

    corridor = create_board(space, vert_borader, horis_boarder, corr_hight, corr_width)



def implement_middle_chember(main_board, hight = 21, width = 81):
    mid_chemb_hight = 6
    mid_chemb_width = 11
    space = "."
    vert_boarder = "|"
    horis_boarder = "#"
    middle_chember = create_board(space, vert_boarder, horis_boarder, mid_chemb_hight, mid_chemb_width)
    middle_chember = implement_gate(middle_chember, mid_chemb_hight, mid_chemb_width)

    central_hight = hight//2 - mid_chemb_hight//2
    central_width = width//2 - mid_chemb_width//2
    
    return implement_chember(main_board, middle_chember, central_hight, central_width, mid_chemb_hight, mid_chemb_width)

def implement_gate(chember, chemb_hight, chemb_width):
    rows = [0, 5]
    space = "."

    for el in rows:
        col_index = random.randint(1, chemb_width - 2)
        chember[el][col_index] = space

    return chember

def gen_main_board():
    main_board = create_board()
    
    return implement_middle_chember(main_board)

def print_a_board():
    board = gen_main_board()

    for row in board:
        for el in row:
            print(el, end = "")
        print()

print_a_board()
