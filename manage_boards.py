import first_board
import creatures
import player
import moving_cars
import ui
import util
import movement

board_1_dict = {
    "board" : [],
    "available_indices" : [],
    "portals_dict" : {},
    "list_of_creatures" : [],
    "list_of_items" : []
}

board_2_dict = {
    "board" : [],
    "available_indices" : [],
    "portals_dict" : {},
    "list_of_creatures" : [],
    "list_of_items" : []
}

board_3_dict = {
    "board" : [],
    "available_indices" : [],
    "portals_dict" : {},
    "list_of_creatures" : [],
    "list_of_items" : []
} 

def boards_generator():
    global board_1_dict, board_2_dict, board_3_dict

    board_1_dict["board"], board_1_dict["available_indices"], board_1_dict["portals_dict"] = first_board.placing_chembers()
    board_2_dict["board"], board_2_dict["available_indices"] = first_board.sec_board(first_board.create_board(41, 81, " ", "#", "#"))
    board_3_dict["board"] = first_board.create_board(41, 81, " ", "#", "#")
    board_3_dict["available_indices"] = first_board.board_all_indices(board_3_dict["board"])

def creatures_to_put_dict():
    animals = creatures.creatures()
    creatures_to_put = []

    for creature in animals:
        creatures_to_put += [(creatures.creatures_on_the_board_dicts(creature))]
    
    return creatures_to_put

def creatures_board_division():
    global board_1_dict, board_2_dict, board_3_dict
    creatures_to_put = creatures_to_put_dict()

    for creature in creatures_to_put:
        creature_1 = creature[0]
        if creature_1["name"] == "Worm" or creature_1["name"] == "Dog":
            board_1_dict["list_of_creatures"] += creature
        elif creature_1["name"] == "Car" or creature_1["name"] == "Lorry" or creature_1["name"] == "Hen":
            board_2_dict["list_of_creatures"] += creature
        else:
            board_3_dict["list_of_creatures"] += creature

def fill_the_bard():
    global board_1_dict, board_2_dict, board_3_dict
    list_of_boards = [board_1_dict, board_2_dict, board_3_dict]

    for board in list_of_boards:
        new_board = player.put_player_on_board(board["board"])
        if board != board_2_dict:
            new_board, new_list_of_creatures = creatures.random_creatures_locations(new_board, board["available_indices"], board["list_of_creatures"])
        else:
            new_board, new_list_of_creatures = creatures.car_placement(new_board, board["available_indices"], board["list_of_creatures"])
        #Wstawianie itemów do zbierania
        board["board"] = new_board
        board["list_of_creatures"] = new_list_of_creatures

def screen_display(board):
    util.clear_screen()
    ui.display_board(board)
    player.print_player_info()

def inventory_management():
    pass

# def creatures_life(list_of_creatures):
#     n = 1
#     for creature in list_of_creatures:
#         print(f"{creature['name']} no {n}. hp: {creature['health']}")

def tour(board_dict, key, inventory = [], list_of_items = []):
    #creatures_life(board_dict["list_of_creatures"])
    board, list_of_creatures = movement.player_move(board_dict["board"], key, board_dict["list_of_creatures"], inventory, list_of_items, board_dict["portals_dict"], board_dict["available_indices"])
    board, list_of_creatures = movement.creature_movement(board_dict["board"], board_dict["list_of_creatures"])

    return board, list_of_creatures

def key_management(board_dict, move_keys = ["w", "s", "a", "d"]):
    key = util.key_pressed()

    if key.lower() == 'q':
        print("You exit the game!")
        exit()
    elif key.lower() == "i":
        inventory_management()
    elif key.lower() in move_keys:
        board_dict["board"], board_dict["list_of_creatures"] = tour(board_dict, key) #inventory, list_of_items

    return board_dict

def levels_menagement(is_running = True):
    global board_1_dict, board_2_dict, board_3_dict
    #list_of_boards = [board_2_dict, board_3_dict]
    list_of_boards = [board_1_dict, board_2_dict, board_3_dict]

    for board_dict in list_of_boards:
        while player.is_it_alive(): #Tutaj mona dać jeszcze warunek przez and
            screen_display(board_dict["board"])
            board_dict = key_management(board_dict)

        if not player.is_it_alive():
            player.print_end_game()
            exit()

def main():
    boards_generator()
    player.hero = player.create_player("1")
    creatures_board_division()
    fill_the_bard()

    levels_menagement()


if __name__ == "__main__":
    main()

#print(first_board.print_a_board(board_1_dict["board"]))
#print(first_board.print_a_board(board_2_dict["board"]))
#print(first_board.print_a_board(board_3_dict["board"]))
#moving_cars.cars_in_the_move(board_2_dict["board"], board_2_dict["list_of_creatures"])