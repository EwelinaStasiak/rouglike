import util


def player_position(player_icon, board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == player_icon:
                player_coordinate = [row, col]
    return player_coordinate


def player_move(key, board, player_icon):

    player_coordinate = player_position(player_icon, board)
    player_row = player_coordinate[0]
    player_col = player_coordinate[1]

    if key.upper() == "W":
        if board[player_row - 1][player_col] != "#":
            board[player_row][player_col] = " "
            board[player_row - 1][player_col] = "@"
    elif key.upper() == "S":
        if board[player_row + 1][player_col] != "#":
            board[player_row][player_col] = " "
            board[player_row + 1][player_col] = "@"
    elif key.upper() == "A":
        if board[player_row][player_col - 1] != "#":
            board[player_row][player_col] = " "
            board[player_row][player_col - 1] = "@"
    elif key.upper() == "D":
        if board[player_row][player_col + 1] != "#":
            board[player_row][player_col] = " "
            board[player_row][player_col + 1] = "@"

    return board
