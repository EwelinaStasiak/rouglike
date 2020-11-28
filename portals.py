import random
import termcolor

def mark_portals(board, portals, first_row, last_row, first_col, last_col,):
    portal_indices = []
    for portal in portals:
        rows_and_cols = {1 : first_row, 2 : last_row, 3 : first_col, 4 : last_col}
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
    #first_board.placing_chembers
    pass

if __name__ == "__main__":
    main()