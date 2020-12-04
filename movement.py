import random
import termcolor #wyświetliło że nieużywane
import hen_talk
import creatures
import inventory


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
        return (row - 1, col)
    elif key.upper() == "S":
        return (row + 1, col)
    elif key.upper() == "A":
        return (row, col - 1)
    elif key.upper() == "D":
        return (row, col + 1)
    else:
        return (row, col)


def identify_obstacle(obstacle, obstacles_dict):

    for key, value in obstacles_dict.items():
        if obstacle == value or obstacle in value:
            return key

    return False


def move_to_empty_space(board, current_row, current_col, next_row, next_col, obstacles_dict, player_icon):

    board[current_row][current_col] = obstacles_dict["empty_space"]
    board[next_row][next_col] = player_icon
    creatures.hero["location"] = (next_row, next_col)

    return board


def bumps_on_vehicul(board, obstacle, obstacles_dict, list_of_creatures, current_position, next_position):

    current_row, current_col = current_position
    vehicul_index = creatures.who_is_the_oponent(list_of_creatures, next_position)
    board, list_of_creatures = creatures.fight(board, list_of_creatures[vehicul_index], list_of_creatures, (current_row, current_col))
    board = creatures.car_crash(board, obstacle, current_position, obstacles_dict)

    return board


def obstacle_move(board, key, obstacle, obstacles_dict, current_position, next_position, list_of_creatures, player_icon):

    current_row, current_col = current_position
    next_row, next_col = next_position
    new_row, new_col = direction_of_movement(key, (next_row, next_col))
    new_obstacle = identify_obstacle(board[new_row][new_col], obstacles_dict)

    if obstacle == "enemies":
        board, list_of_creatures = creatures.fight(board, creatures.hero, list_of_creatures, (next_row, next_col))
    elif new_obstacle == "vehiculs":
        board = bumps_on_vehicul(board, new_obstacle, obstacles_dict, list_of_creatures, current_position, (new_row, new_col))
    elif obstacle == "empty_space" or obstacle == "player_icon":
        move_to_empty_space(board, current_row, current_col, next_row, next_col, obstacles_dict, player_icon)
    elif obstacle == "road":
        if new_obstacle == "empty_space":
            move_to_empty_space(board, current_row, current_col, new_row, new_col, obstacles_dict, player_icon)
        else:
            board = bumps_on_vehicul(board, new_obstacle, obstacles_dict, list_of_creatures, current_position, (new_row, new_col))
    elif obstacle == "friends":
        choice = hen_talk.talking_to_hen(board)
    elif obstacle == "vehiculs":
        bumps_on_vehicul(board, obstacle, obstacles_dict, list_of_creatures, current_position, next_position)
    elif obstacle == "boss":
        creatures.fight_boss()

    return board, list_of_creatures


def moveing_through_portals(board, current_position, obstacles_dict, next_position, possible_coordinates, portals_dict, player_icon):

    current_row, current_col = current_position
    board[current_row][current_col] = obstacles_dict["empty_space"]
    portal_indices = portals_dict[next_position]
    next_row, next_col = getting_off_the_portal(board, portal_indices, possible_coordinates)
    board[next_row][next_col] = player_icon
    creatures.hero["location"] = (next_row, next_col)

    return board


def player_move(board, key, list_of_creatures, inventory_hero, list_of_items, portals_dict, possible_coordinates):

    obstacles_dict = {"empty_space" : " ", "wall" : "#", "friends" : "H", "enemies" : ["W", "D"], "vehiculs" : ["C", "L"], "road" : "–", "portals" : portals_dict, "player_icon" : "@", "boss": "F"}
    player_icon = obstacles_dict["player_icon"]
    current_position = character_position(player_icon, board)
    next_position = direction_of_movement(key, current_position)
    next_row, next_col = next_position
    obstacle = identify_obstacle(board[next_row][next_col], obstacles_dict)

    if obstacle == "wall":
        board[current_position[0]][current_position[1]] = player_icon
    elif obstacle:
        board, list_of_creatures = obstacle_move(board,key, obstacle, obstacles_dict, current_position, next_position, list_of_creatures, player_icon)
    elif next_position in portals_dict:
        board = moveing_through_portals(board, current_position, obstacles_dict, next_position, possible_coordinates, portals_dict, player_icon)
    else:
        for item in list_of_items:
            if item.get("picture") == board[next_row][next_col]:
                board = inventory.player_interaction(board, item, next_position, current_position)
                break

    return board, list_of_creatures

# def player_move(board, key, list_of_creatures, inventory, list_of_items, portals_dict, possible_coordinates): #Parametr z lokacją wrogów
#     enemy_icon = ["W", "D"] #"C", "L"
#     vehiculs_icons = ["C", "L"]
#     player_icon = creatures.hero.get("picture")
#     road_line = "–"
#     elements_without_interaction = [" ", "#", road_line]
#     hen_icon = "H"
#     portals = [termcolor.colored("O", "green"), termcolor.colored("O", "blue"), termcolor.colored("O", "yellow")]
#     row, col = character_position(player_icon, board)

#     next_row, next_col = direction_of_movement(key, (row, col))
#     next_row_2, next_col_2 = direction_of_movement(key, (next_row, next_col))
#     #next_player_coordinate = direction_of_movement(key, player_coordinate)
#     #next_row = next_player_coordinate[0] # Moze to tak skrócić, by było bardziej czytelne?
#     #next_col = next_player_coordinate[1]
#     next_position = board[next_row][next_col]

#     if next_position in enemy_icon:   # pętla na wypadek natrafienia na wroga
#         board, list_of_creatures = creatures.fight(board, creatures.hero, list_of_creatures, (next_row, next_col))

#     elif board[next_row_2][next_col_2] in vehiculs_icons:
#         vehicul_index = creatures.who_is_the_oponent(list_of_creatures, (next_row_2, next_col_2))
#         board, list_of_creatures = creatures.fight(board, list_of_creatures[vehicul_index], list_of_creatures, (row, col))
#         board = creatures.car_accident(board, board[next_row_2][next_col_2], (row, col), vehiculs_icons)

#     elif next_position == " " or next_position == player_icon:    # next_position == player_icon zabezpieczenie jak wciśnie się coś innego niż W, S, A, D. Player zostaje w tym samym miejscu 
#         board[row][col] = " "
#         board[next_row][next_col] = player_icon
#         creatures.hero["location"] = (next_row, next_col)
    
#     elif (next_row, next_col) in portals_dict:
#         board[row][col] = " "
#         portal_indices = portals_dict[(next_row, next_col)]
#         next_row, next_col = getting_off_the_portal(board, portal_indices, possible_coordinates)
#         board[next_row][next_col] = player_icon
#         creatures.hero["location"] = (next_row, next_col)

#     elif next_position == hen_icon:
#         choice = hen_talk.talking_to_hen(board)

#     elif next_position not in elements_without_interaction and next_position not in enemy_icon:
#         for item in list_of_items:
#             if item.get("picture") == next_position:
#                 board = inventory.player_interaction(board, item, [next_row, next_col], [row, col])
#                 break
#     elif next_position == road_line:
#         board[row][col] = " "
#         next_row, next_col = direction_of_movement(key, (next_row, next_col))
#         if board[next_row][next_col] not in vehiculs_icons:
#             board[next_row][next_col] = player_icon
#             creatures.hero["location"] = (next_row, next_col)
#         else:
#             vehicul_index = creatures.who_is_the_oponent(list_of_creatures, (next_row_2, next_col_2))
#             board, list_of_creatures = creatures.fight(board, list_of_creatures[vehicul_index], list_of_creatures, (row, col))
#             board = creatures.car_accident(board, board[next_row_2][next_col_2], (row, col), vehiculs_icons)
#     return board, list_of_creatures


def getting_off_the_portal(board, portal_indices, possible_coordinates):

    portals = [termcolor.colored("O", "green"), termcolor.colored("O", "blue"), termcolor.colored("O", "yellow")]
    next_indices = ()
    row, col = portal_indices

    if (row + 1, col) in possible_coordinates and board[row + 1][col] != "#" and board[row + 1][col] not in portals:
        return (row + 1, col)
    elif (row - 1, col) in possible_coordinates and board[row - 1][col] != "#" and board[row - 1][col] not in portals:
        return (row - 1, col)
    elif (row, col + 1) in possible_coordinates and board[row][col + 1] != "#" and board[row][col + 1] not in portals:
        return (row, col + 1)
    elif (row, col - 1) in possible_coordinates and board[row][col - 1] != "#" and board[row][col - 1] not in portals:
        return (row, col - 1)

def random_creature_move(board, list_of_creatures, floor = " "):

    keybord_keys = ["W", "S", "A", "D"]
    enemy_icons = ["W", "D"]
    player_icon = creatures.hero.get("picture")
    for creature in list_of_creatures:
        random_key = random.choice(keybord_keys)
        row, col = creature["location"]

        new_row, new_col = direction_of_movement(random_key, creature["location"])

        if board[new_row][new_col] == floor:
            board[new_row][new_col] = board[row][col]
            board[row][col] = floor
            creature["location"] = (new_row, new_col)

        elif board[new_row][new_col] == player_icon or board[new_row][new_col] in enemy_icons:
            board, list_of_creatures = creatures.fight(board, creature, list_of_creatures, (new_row, new_col))
            #creature["location"] = (new_row, new_col)

    return board, list_of_creatures


def car_movement(board, list_of_vehiculs):

    #player_icon = creatures.hero.get("picture")  #wyświetliło że nieużywane
    # above_road_row = 13  wyświetliło że nieużywane
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
                # if board[row][new_col] == player_icon:
                #     board[above_road_row][new_col]
            board[row][new_col] = vehicul["pic"]
        elif kind == "Lorry":
            board[row][col: col + 2] = [floor] * 2
            if col == min_col:
                new_col = max_col - 1
            else:
                new_col = col - 1
                # if board[row][new_col] == player_icon:
                #     board[above_road_row][new_col]
            board[row][new_col: new_col+2] = [vehicul["pic"]] * 2
            vehicul["location_2"] = (row, new_col + 1)

        vehicul["location"] = (row, new_col)

    return board, list_of_vehiculs


def creature_movement(board, list_of_creatures):

    first_creature = list_of_creatures[0]

    if first_creature["name"] == "Car" or first_creature["name"] == "Lorry":
        board, list_of_creatures = car_movement(board, list_of_creatures)
    elif first_creature["name"] == "Worm" or first_creature["name"] == "Dog":
        board, list_of_creatures = random_creature_move(board, list_of_creatures)
    elif first_creature["name"] == "Fox":
        board, list_of_creatures = boss_movement(board, list_of_creatures)

    return board, list_of_creatures


def boss_movement(board, list_of_creatures):

    global boss
    boss = creatures.boss
    boss_coordinate = character_position(boss.get("picture"), board)
    first_row = boss_coordinate[0]
    first_col = boss_coordinate[1]
    last_col = first_col + (boss.get("size") - 1)
    lenght_row_board = len(board[first_row])
    movement = 2

    if last_col + movement < lenght_row_board - 2:
        for row in range(boss.get("size")):
            for col in range(movement):
                board[first_row + row][first_col + col] = " "
                board[first_row + row][last_col + (col + 1)] = boss.get("picture")
    else:
        for row in range(boss.get("size")):
            for col in range(boss.get("size")):
                board[first_row + row][first_col + col] = " "
                # board[lenght_board - (boss.get("size") + 1) + row][start_col_boss + col]
        creatures.put_boss_on_board(boss, board)
        
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


