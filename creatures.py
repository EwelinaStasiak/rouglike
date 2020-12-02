import random
import display_information


"""
************************************
            CREATURES
************************************
"""


def creatures():
    worm = {'name': "Worm", 'kind': "Enemy", 'health': 2, "min_damage": 1, "max_damage": 1, "num_to_place": 5, 'pic': "W"} #128027}
    car = {'name': "Car", 'kind': "Enemy", 'health': 20, "min_damage": 5, "max_damage": 10, "num_to_place": 15, 'pic': "C"} #128663}
    lorry = {'name': "Lorry", 'kind': "Enemy", 'health': 20, "min_damage": 20, "max_damage": 50, "num_to_place": 5, 'pic': "L"} #128666}
    dog = {'name': "Dog", 'kind': "Enemy", 'health': 20, "min_damage": 1, "max_damage": 5, "num_to_place": 5, 'pic': "D"} #128021}
    hen = {'name': "Hen", 'kind': "Firend", 'health': 5, "num_to_place": 1, 'pic': "H"} #128020}

    return worm, car, lorry, dog, hen


def creatures_on_the_board_dicts(creature):
    list_of_creatures = []

    for num in range(creature["num_to_place"]):
        monster = {}
        for key, value in creature.items():
            monster[key] = value
        list_of_creatures.append(monster)

    return list_of_creatures


def random_creatures_locations(board, board_indexes, list_of_creatures):
    floor = " "

    for creature in list_of_creatures:
        value = False
        while value is False:
            row_index, col_index = random.choice(board_indexes)
            if board[row_index][col_index] == floor:
                board[row_index][col_index] = creature["pic"]
                creature["location"] = (row_index, col_index)
                value = True

    return board, list_of_creatures


def non_road_coordinates(board_indices, road_rows):
    row = 0
    for indices in board_indices:
        if indices[row] in road_rows:
            board_indices.remove(indices)

    return board_indices


def car_placement(board, board_indices, list_of_vehiculs):
    vehiculs_to_place = len(list_of_vehiculs)
    road_rows = [15, 16, 17, 19, 20, 21]
    non_road_indices = non_road_coordinates(board_indices, road_rows)
    min_col = 1
    max_col = 78

    while vehiculs_to_place > 0:
        row_index = random.choice(road_rows)
        col_index = random.randint(min_col, max_col)

        if board[row_index][col_index] == " " and board[row_index][col_index + 2] == " ":
            vehicul = list_of_vehiculs[vehiculs_to_place - 1]
            if vehicul["name"] == "Lorry":
                board[row_index][col_index: col_index + 2] = [vehicul["pic"]] * 2
                vehicul["location"] = (row_index, col_index)
            elif vehicul["name"] == "Car":
                board[row_index][col_index] = vehicul["pic"]
                vehicul["location"] = (row_index, col_index)
            else:
                random_creatures_locations(board, non_road_indices, [vehicul])
            vehiculs_to_place -= 1

    return board, list_of_vehiculs


def enemy_pics():
    creatures_list = creatures()
    enemy_pics = []

    for el in creatures_list:
        if el["kind"] == "Enemy":
            enemy_pics.append(el["pic"])

    return enemy_pics


"""
************************************
            BOSS
************************************
"""


def create_boss():
    global boss
    boss = {'name': "Wyga", 'species': "fox", 'health': 20, "max_health": 20, "min_damage": 2, "max_damage": 7, "picture": "F"}

    return boss


def put_boss_on_board(boss, board):
    boss_size = 5
    how_many_rows = len(board)
    how_many_cols = len(board[0])
    first_row = how_many_rows - 6
    first_col = int(how_many_cols / 2) - 3
    for row in range(boss_size):
        for col in range(boss_size):
            board[first_row + row][first_col + col] = boss.get("picture")

    return board


"""
************************************
            PLAYER
************************************
"""


def create_player():
    global hero
    'Tworzy bohatera wg wyboru użytkownika'
    display_information.choose_hero()
    invalid = True
    while invalid:
        user_choice = input()
        if user_choice == "1":
            hero = {'name': "Mikolaj", 'species': "hedgehog", 'health': 10, 'max_load': 15, "max_health": 25, "min_damage" : 2, "max_damage" : 5,  "picture": "@"}
            invalid = False
        elif user_choice == "2":
            hero = {'name': "Mikolaj", 'species': "Magic hedgehog", 'health': 15, 'max_load': 10, 'skill': "magic", "max_health": 25, "min_damage" : 0, "max_damage" : 7, "picture": "@"}
            invalid = False
        elif user_choice == "3":
            hero = {'name': "Mikolaj", 'species': "Invisible hedgehog", 'health': 5, 'max_load': 5, 'skill': "invisible", "max_health": 25, "min_damage" : 10, "max_damage" : 25, "picture": "@"}    
            invalid = False
        else:
            print("Choose 1, 2 or 3")
    return hero


def put_player_on_board(board):
    global hero
    player_icon = hero.get("picture")
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "#" and board[row + 1][col] == "#" and board[row][col + 1] == "#":
                player_start_row = row + 1
                player_start_col = col + 2
                board[player_start_row][player_start_col] = player_icon

                return board


def is_it_alive():
    if hero["health"] <= 0:
        display_information.print_end_game()
        return False
    return True


def print_player_info():
    print(f"Player's name : {hero['name']}     Health level : {hero['health']}")


"""
************************************
            FIGHT
************************************
"""


def who_is_the_oponent(list_of_creatures, location):
    for creature in list_of_creatures:
        if location == creature["location"]:
            return list_of_creatures.index(creature)
        elif location == hero.get("location"):
            return False


def carry_damage(attacker, opponent):
    damage = random.randint(attacker["min_damage"], attacker["max_damage"])
    opponent["health"] -= damage

    if opponent["health"] > 0:
        return opponent
    else:
        return False


def did_it_hit():
    hit = [True, False]
    return random.choice(hit)


def hit_the_opponent(attacker, opponent):
    if did_it_hit():
        opponent = carry_damage(attacker, opponent)
        if opponent:
            return opponent
        else:
            return None
    else:
        print("You missed, sucker!")
        return False


def fight(board, attacker, list_of_creatures, location):
    global hero
    row, col = location
    creature_index = who_is_the_oponent(list_of_creatures, location)

    if creature_index:
        opponent = list_of_creatures[creature_index]
        opponent = hit_the_opponent(attacker, opponent)
        if opponent:
            list_of_creatures[creature_index] = opponent
        elif opponent is None:
            list_of_creatures.remove(list_of_creatures[creature_index])
            board[row][col] = " "
    else:
        opponent = hero
        opponent = hit_the_opponent(attacker, opponent)
        if opponent:
            hero = opponent
    
    return board, list_of_creatures


def fight_boss(weapon):
    global hero
    global boss
    if weapon.get("name") == "Hen":
        boss["health"] = 0

    elif weapon.get("name") == "Cone":
        hit_fox = did_it_hit()
        if hit_fox:
            boss = carry_damage(hero, boss)
        else:
            stone = stone_throw()
            hit_hero = did_it_hit()
            if stone and hit_hero:
                hero["health"] -= boss["max_damage"]
            elif hit_hero:
                hero = carry_damage(boss, hero)
    elif weapon == "close":
        hero["health"] = 0

    win = win_the_game()
    if win:
        exit()

    return boss


def stone_throw():
    number = random.randint(1, 5)
    return (number % 3 == 0)


def win_the_game(boss_health):
    if boss_health == 0 and hero.get("health") > 0:
        display_information.win_screen()
        return True
    else:
        return False

#list_of_creatures = [{'name': 'Worm', 'health': 15, 'min_damage': 1, 'max_damage': 20, 'num_to_place': 5, 'pic': 'W', 'location': (2, 7)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 2)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (5, 5)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 5)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 3)}]
#location =(2, 7)

# def main():
#     board_list = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", "@", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
    
#     #worm_1, worm_2, worm_3, worm_4, worm_5 = list_of_creatures
    
#     board_index = gen_boards.board_indexes(board_list)
#     worm, car, lory, dog, hen = creatures()
#     list_of_creatures = creatures_on_the_board_dicts(worm)
#     board, list_of_creatures = random_creatures_locations(board_list, board_index, list_of_creatures)
#     ui.display_board(board_list)





# def random_creatures_locations(board, board_indexes, list_of_creatures):
#     floor = " "
#     creatures_locations = []
    
#     while creatures_number > 0:
#         row_index, col_index = random.choice(board_indexes)
#         if board[row_index][col_index] == floor:
#             board[row_index][col_index] = creature_icon
#             creatures_locations.append((row_index, col_index))
#             creatures_number -= 1

#     return board, creatures_locations

# def random_damage(min_damage, max_damage):
#     return random.randint(min_damage, max_damage)


# if __name__ == "__main__":
    
#     main()
