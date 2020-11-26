import random

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

def creature_movement(board, creatures_location):
    keybord_keys = ["W", "S", "A", "D"]
    floor = " "
    new_locations = []

    for index in creatures_location:
        random_key = random.choice(keybord_keys)
        row, col = index

        new_row, new_col = direction_of_movement(random_key, index)

        if board[new_row][new_col] == floor:
            board[new_row][new_col] = board[row][col]
            board[row][col] = floor
            new_locations.append((new_row, new_col))
        else:
            new_locations.append((row, col))
    
    return board, new_locations

def fight(character_1, character_2_health, min_damage = 1, max_damage = 2):
    if not did_I_miss():
        damage = random.randint(min_damage, max_damage)
        character_2_health -= damage

def did_I_miss():
    values = [True, False]

    return random.choice(values)

def did_it_die():
    pass


