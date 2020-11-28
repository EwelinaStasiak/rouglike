import random
import fight

def character_position(character_icon, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
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


def player_move(board, player_icon, key, list_of_creatures): #Parametr z lokacją wrogów
    enemy_icon = ["W"]
    player_coordinate = character_position(player_icon, board)
    next_player_coordinate = direction_of_movement(key, player_coordinate)

    if board[next_player_coordinate[0]][next_player_coordinate[1]] == " ":
        board[player_coordinate[0]][player_coordinate[1]] = " "
        board[next_player_coordinate[0]][next_player_coordinate[1]] = player_icon
    elif board[next_player_coordinate[0]][next_player_coordinate[1]] in enemy_icon: # pętla na wypadek natrafienia na wroga
        board, list_of_creatures = fight.fight(board, list_of_creatures, (next_player_coordinate[0], next_player_coordinate[1]))
    return board, list_of_creatures

def creature_movement(board, list_of_creatures, enemy_icon):
    keybord_keys = ["W", "S", "A", "D"]
    floor = " "
    #new_locations = []

    for creature in list_of_creatures:
        random_key = random.choice(keybord_keys)
        row, col = creature["location"]

        new_row, new_col = direction_of_movement(random_key, creature["location"])

        if board[new_row][new_col] == floor:
            board[new_row][new_col] = board[row][col]
            board[row][col] = floor
            creature["location"] = (new_row, new_col)
        elif board[new_row][new_col] in enemy_icon:
            creature["location"] = (new_row, new_col)
            board, list_of_creatures = fight.fight(board, list_of_creatures, (new_row, new_col))
        else:
           creature["location"] = (row, col)
    
    return board, list_of_creatures

# def fight(character_1, character_2_health, min_damage = 1, max_damage = 2):
#     did_I_miss = random.choice([True, False])
#     if not did_I_miss():
#         damage = random.randint(min_damage, max_damage)
#         character_2_health -= damage
    
#     return character_2_health

# def did_it_die(character_health):
#     if character_health <= 0:
#         return True
#     else:
#         return False


