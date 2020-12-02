import creatures
import util
import movement
import engine
import inventory


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

    board_1_dict["board"], board_1_dict["available_indices"], board_1_dict["portals_dict"] = engine.placing_chembers()
    board_2_dict["board"], board_2_dict["available_indices"] = engine.sec_board(engine.create_board(41, 81, " ", "#", "#"))
    board_3_dict["board"] = engine.create_board(41, 81, " ", "#", "#")
    board_3_dict["available_indices"] = engine.board_all_indices(board_3_dict["board"])

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
        # elif creature_1["name"] == "Wyga":
        #     board_3_dict["list_of_creatures"] += creature

def fill_the_bard():
    global board_1_dict, board_2_dict, board_3_dict
    list_of_boards = [board_1_dict, board_2_dict, board_3_dict]
    list_of_items = inventory.create_items()
    items_on_board = inventory.items_on_board(list_of_items)

    for board in list_of_boards:
        new_board = creatures.put_player_on_board(board["board"])
        if board == board_1_dict:
            new_board, new_list_of_creatures = creatures.random_creatures_locations(new_board, board["available_indices"], board["list_of_creatures"])
            new_board = inventory.random_items_locations(new_board,board["available_indices"],items_on_board,num_board = 1)
        elif board == board_2_dict:
            new_board, new_list_of_creatures = creatures.car_placement(new_board, board["available_indices"], board["list_of_creatures"])            
            new_board = inventory.random_items_locations(new_board,board["available_indices"],items_on_board,num_board = 2)
        elif board == board_3_dict:
            #new_board = creatures.put_boss_on_board(board["list_of_creatures"], board["board"])
            boss = creatures.create_boss()
            new_board, new_list_of_creatures = creatures.put_boss_on_board(boss, board["board"])
            new_board = inventory.random_items_locations(new_board,board["available_indices"],items_on_board,num_board = 3)
        #new_board = inventory.random_items_locations(new_board,board["available_indices"],items_on_board,board)
        #Wstawianie itemów do zbierania
        board["board"] = new_board
        board["list_of_creatures"] = new_list_of_creatures


def screen_display(board):
    util.clear_screen()
    engine.display_board(board)
    creatures.print_player_info()


def inventory_management(board_dict):
    global board_3_dict
    list_of_items = inventory.create_items()
    inventory.inventory_hero = inventory.create_inventory()
    inventory.print_inventory()
    if board_dict == board_3_dict:
        inventory.use_item_from_inventory(list_of_items, fight_with_boss=True)
    else:
        inventory.use_item_from_inventory(list_of_items)

# def creatures_life(list_of_creatures):
#     n = 1
#     for creature in list_of_creatures:
#         print(f"{creature['name']} no {n}. hp: {creature['health']}")


def tour(board_dict, key, inventory=[], list_of_items=[]):
    #creatures_life(board_dict["list_of_creatures"])
    board, list_of_creatures = movement.player_move(board_dict["board"], key, board_dict["list_of_creatures"], inventory, list_of_items, board_dict["portals_dict"], board_dict["available_indices"])
    board, list_of_creatures = movement.creature_movement(board_dict["board"], board_dict["list_of_creatures"])

    return board, list_of_creatures


def key_management(board_dict, move_keys=["w", "s", "a", "d"]):
    key = util.key_pressed()

    if key.lower() == 'q':
        print("You exit the game!")
        exit()
    elif key.lower() == "i":
        inventory_management(board_dict)
    elif key.lower() in move_keys:
        board_dict["board"], board_dict["list_of_creatures"] = tour(board_dict, key) #inventory, list_of_items

    return board_dict


def levels_menagement(is_running=True):
    global board_1_dict, board_2_dict, board_3_dict
    list_of_boards = [board_2_dict, board_3_dict]
    #list_of_boards = [board_1_dict, board_2_dict, board_3_dict]

    for board_dict in list_of_boards:
        #move = 0
        while creatures.is_it_alive(): # and move < 5: #Tutaj mozna dać jeszcze warunek przez and
            screen_display(board_dict["board"])
            board_dict = key_management(board_dict)
            #move += 1

        if not creatures.is_it_alive():
            # display_information.print_end_game()
            exit()


def main():
    boards_generator()
    creatures.hero = creatures.create_player()
    creatures_board_division()
    fill_the_bard()

    levels_menagement()


if __name__ == "__main__":
    main()

#print(first_board.print_a_board(board_1_dict["board"]))
#print(first_board.print_a_board(board_2_dict["board"]))
#print(first_board.print_a_board(board_3_dict["board"]))
#moving_cars.cars_in_the_move(board_2_dict["board"], board_2_dict["list_of_creatures"])