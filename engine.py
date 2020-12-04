import random
import termcolor


def create_board(hight=41, width=81, space=" ", vert_boarder=" ", horis_boarder=" "):

    board = []
    first_last_row = [0, hight - 1]

    for num in range(hight):
        if num in first_last_row:
            board.append([horis_boarder] * width)
        else:
            board.append([vert_boarder] + [space] * (width - 2) + [vert_boarder])

    return board


"""
–––––––––––––––––––––––––––––––––––––
Board_1
–––––––––––––––––––––––––––––––––––––
"""


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

    board, yellow1_green1_portals, available_coordinates = placing_1st_chember(board, chember_1, row_1, available_coordinates, hight_and_width[1])
    board, blue1_yellow_2_portals, available_coordinates = placing_2nd_chember(board, chember_2, col_1, available_coordinates, hight_and_width[2])
    board, green2_blue_2_portals, available_coordinates = placing_3rd_chember(board, chember_3, row_2, col_2, available_coordinates, hight_and_width[3])

    portals_dict = gen_portals_dict(yellow1_green1_portals + blue1_yellow_2_portals + green2_blue_2_portals)

    return board, available_coordinates, portals_dict


def gen_portals_dict(portals):

    portals_dict = {}

    for n in range(len(portals)//2):
        portals_dict[portals[n]] = portals[n+3]
        portals_dict[portals[n+3]] = portals[n]

    return portals_dict


def placing_1st_chember(board, chember_1, row_1, available_coordinates, dimensions):

    row_for_portal = row_1

    for row_num in range(len(chember_1)):
        n = 0
        for el in chember_1[row_num]:
            board[row_1][n] = el
            available_coordinates.append((row_1, n))
            n += 1
        row_1 += 1

    board, portal_indices = chember_1_portals(board, dimensions, row_for_portal)

    return board, portal_indices, available_coordinates


def placing_2nd_chember(board, chember_2, col_1, available_coordinates, dimensions):

    col_for_portal = col_1

    for row_num in range(len(chember_2)):
        n = 0
        r_col = col_1
        for col in chember_2[row_num]:
            board[row_num][r_col] = col
            available_coordinates.append((row_num, r_col))
            r_col += 1
            n += 1

    board, portal_indices = chember_2_portals(board, dimensions, col_for_portal)

    return board, portal_indices, available_coordinates


def placing_3rd_chember(board, chember_3, row_2, col_2, available_coordinates, dimensions):

    row_for_portal = row_2
    col_for_portal = col_2

    for row_num in range(len(chember_3)):
        col = col_2
        for el in chember_3[row_num]:
            board[row_2][col] = el
            available_coordinates.append((row_2, col))
            col += 1
        row_2 += 1

    board, portal_indices = chember_3_portals(board, dimensions, row_for_portal, col_for_portal)

    return board, portal_indices, available_coordinates


"""
–––––––––––––––––––––––––––––––––––––
Board_2
–––––––––––––––––––––––––––––––––––––
"""


def sec_board(board):

    road_banch = [14, 22]
    road_strips = [" ", "–"]

    for index in road_banch:
        board[index][1: 80] = ["–"] * 79

    midle_road_index = 1

    while midle_road_index < 77:
        for el in road_strips:
            board[18][midle_road_index: midle_road_index + 2] = [el] * 2
            midle_road_index += 2

    return board, board_all_indices(board)


def car_placement(board):

    car = 20

    while car > 0:
        road_indices = [15, 16, 17, 19, 20, 21]
        row_index = random.choice(road_indices)
        col_index = random.randint(1, 78)
        if board[row_index][col_index] == " " and board[row_index][col_index + 2] == " ":
            board[row_index][col_index: col_index + 2] = ["C"] * 2
            car -= 1

    return board


def board_all_indices(board):

    board_indices = []

    for row_num in range(len(board)):
        for col_num in range(len(board[row_num])):
            board_indices.append((row_num, col_num))

    return board_indices


"""
–––––––––––––––––––––––––––––––––––––
PRINT
–––––––––––––––––––––––––––––––––––––
"""


def display_board(board):

    for row in board:
        for el in row:
            if el == "K":
                print(termcolor.colored(el, "yellow"), end="")
            elif el == "@":
                print(termcolor.colored(el, "cyan"), end="")
            elif el == "H":
                print(termcolor.colored(el, "green"), end="")
            
            else:
                print(el, end="")
        print()


"""
–––––––––––––––––––––––––––––––––––––
PORTALS
–––––––––––––––––––––––––––––––––––––
"""


def mark_portals(board, portals, first_row, last_row, first_col, last_col,):

    portal_indices = []

    for portal in portals:
        rows_and_cols = {1: first_row, 2: last_row, 3: first_col, 4: last_col}
        key = random.randint(1, 4)

        if key < 3:
            rand_col = random.randint(first_col + 1, last_col - 2)
            board[rows_and_cols[key]][rand_col] = portal
            portal_indices.append((rows_and_cols[key], rand_col))
        else:
            rand_row = random.randint(first_row + 1, last_row - 2)
            board[rand_row][rows_and_cols[key]] = portal
            portal_indices.append((rand_row, rows_and_cols[key]))

    return board, portal_indices


def chember_1_portals(board, dimensions, rand_row):

    portals = [termcolor.colored("O", "yellow"), termcolor.colored("O", "green")]
    hight, width = dimensions
    first_row = rand_row
    last_row = rand_row + hight - 1
    first_col = 0
    last_col = width - 1

    return mark_portals(board, portals, first_row, last_row, first_col, last_col)


def chember_2_portals(board, dimensions, rand_col):

    portals = [termcolor.colored("O", "blue"), termcolor.colored("O", "yellow")]
    hight, width = dimensions
    first_row = 0
    last_row = hight - 1
    first_col = rand_col
    last_col = rand_col + width - 1

    return mark_portals(board, portals, first_row, last_row, first_col, last_col)


def chember_3_portals(board, dimensions, rand_row, rand_col):

    portals = [termcolor.colored("O", "green"), termcolor.colored("O", "blue")]
    hight, width = dimensions
    first_row = rand_row
    last_row = rand_row + hight - 1
    first_col = rand_col
    last_col = rand_col + width - 1

    return mark_portals(board, portals, first_row, last_row, first_col, last_col)


def main():
    
    board, available_coordinates = placing_chembers()
    display_board(board)
    print(len(available_coordinates))


if __name__ == "__main__":
    main()
