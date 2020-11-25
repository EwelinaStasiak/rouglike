def character_position(character_icon, board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == character_icon:
                character_coordinate = [row, col]
    return character_coordinate


def direction_of_movement(key, character_coordinate):
    row = character_coordinate[0]
    col = character_coordinate[1]
    
    if key.upper() == "W":
        return [row - 1, col]
    elif key.upper() == "S":
        return [row + 1, col]
    elif key.upper() == "A":
        return [row, col - 1]
    elif key.upper() == "D":
        return [row, col + 1]
    else:
        return [row, col]


def player_move(board, player_icon, key):

    player_coordinate = character_position(player_icon, board)
    next_player_coordinate = direction_of_movement(key, player_coordinate)

    if board[next_player_coordinate[0]][next_player_coordinate[1]] == " " or board[next_player_coordinate[0]][next_player_coordinate[1]] == player_icon:
        board[player_coordinate[0]][player_coordinate[1]] = " "
        board[next_player_coordinate[0]][next_player_coordinate[1]] = player_icon
    return board
