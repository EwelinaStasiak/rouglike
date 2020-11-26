def create_board(width, hight, space = " ", vert_boarder = " ", horis_boarder = " "):
    board = []
    first_last_row = [0, hight - 1]

    for num in range(hight):
        if num in first_last_row:
            board.append([horis_boarder] * width)
        else:
            board.append([vert_boarder] + [space] * (width - 2) + [vert_boarder])
    
    return board

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
