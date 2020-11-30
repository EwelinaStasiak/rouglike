import random
import fight
import interaction
import termcolor
import player
import manage_boards


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


def player_move(board, key, list_of_creatures, inventory, list_of_items, portals_dict, possible_coordinates): #Parametr z lokacją wrogów
    enemy_icon = ["W", "D"]
    player_icon = player.hero.get("picture")
    elements_without_interaction = [" ", "#"]
    portals = [termcolor.colored("O", "green"), termcolor.colored("O", "blue"), termcolor.colored("O", "yellow")]

    player_coordinate = character_position(player_icon, board)

    next_player_coordinate = direction_of_movement(key, player_coordinate)
    #next_row = next_player_coordinate[0] # Moze to tak skrócić, by było bardziej czytelne?
    #next_col = next_player_coordinate[1]
    next_position = board[next_player_coordinate[0]][next_player_coordinate[1]]
    
    if next_position == " " or next_position == player_icon:    # next_position == player_icon zabezpieczenie jak wciśnie się coś innego niż W, S, A, D. Player zostaje w tym samym miejscu 
        board[player_coordinate[0]][player_coordinate[1]] = " "
        board[next_player_coordinate[0]][next_player_coordinate[1]] = player_icon
    
    elif (next_player_coordinate[0], next_player_coordinate[1]) in portals_dict:
        board[player_coordinate[0]][player_coordinate[1]] = " "
        portal_indices = portals_dict[(next_player_coordinate[0], next_player_coordinate[1])]
        next_row, next_col = getting_off_the_portal(board, portal_indices, possible_coordinates)
        board[next_row][next_col] = player_icon

    elif next_position in enemy_icon:   # pętla na wypadek natrafienia na wroga
        board, list_of_creatures = fight.fight(board, player.hero, list_of_creatures, (player_coordinate[0], player_coordinate[1]))

    elif next_position not in elements_without_interaction and next_position not in enemy_icon:
        for item in list_of_items:
            if item.get("picture") == next_position:
                board = interaction.player_interaction(board, item, next_player_coordinate, player_coordinate)
                break
    return board, list_of_creatures


def getting_off_the_portal(board, portal_indices, possible_coordinates):
    next_indices = ()
    row, col = portal_indices
    
    if (row + 1, col) in possible_coordinates and board[row + 1][col] != "#":
        return (row + 1, col)
    elif (row - 1, col) in possible_coordinates and board[row - 1][col] != "#":
        return (row - 1, col)
    elif (row, col + 1) in possible_coordinates and board[row][col + 1] != "#":
        return (row, col + 1)
    elif (row, col - 1) in possible_coordinates and board[row][col - 1] != "#":
        return (row, col - 1)

def random_creature_move(board, list_of_creatures, floor = " "):
    keybord_keys = ["W", "S", "A", "D"]
    enemy_icons = ["W", "D", "C", "L"]
    player_icon = player.hero.get("picture")
    for creature in list_of_creatures:
        random_key = random.choice(keybord_keys)
        row, col = creature["location"]

        new_row, new_col = direction_of_movement(random_key, creature["location"])

        if board[new_row][new_col] == floor:
            board[new_row][new_col] = board[row][col]
            board[row][col] = floor
            creature["location"] = (new_row, new_col)
        elif board[new_row][new_col] in [player_icon] + [enemy_icons]:
            creature["location"] = (new_row, new_col)
            board, list_of_creatures = fight.fight(board, creature, list_of_creatures, (new_row, new_col))

        else:
            creature["location"] = (row, col)
    
    return board, list_of_creatures

def car_movement(board, list_of_vehiculs):
    floor = " "
    min_col = 1
    max_col = 79

    for vehicul in list_of_vehiculs:
        row, col = vehicul["location"]
        kind = vehicul["name"]

        if kind == "Car":
            board[row][col] = floor
            if col == min_col:
                new_col = max_col
            else:
                new_col = col - 1
            board[row][new_col] = vehicul["pic"]
        elif kind == "Lorry":
            board[row][col : col + 2] = [floor] * 2
            if col == min_col:
                new_col = max_col - 1
            else:
                new_col = col - 1
            board[row][new_col : new_col+2] = [vehicul["pic"]] * 2

        vehicul["location"] = (row, new_col)

    return board, list_of_vehiculs         

def creature_movement(board, list_of_creatures):
    first_creature = list_of_creatures[0]
    if first_creature["name"] == "Car" or first_creature["name"] == "Lorry":
        board, list_of_creatures = car_movement(board, list_of_creatures)
    elif first_creature["name"] == "Worm" or first_creature["name"] == "Dog":
        board, list_of_creatures = random_creature_move(board, list_of_creatures)
        
    
    return board, list_of_creatures
    #new_locations = []

    

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


