import first_board
import creatures
import player
import moving_cars

board_1_dict = {
    "board" : None,
    "available_indices" : None,
    "portals_dict" : None,
    "list_of_creatures" : [],
    "list_of_items" : []
}

board_2_dict = {
    "board" : None,
    "available_indices" : None,
    "portals_dict" : None,
    "list_of_creatures" : [],
    "list_of_items" : []
}

board_3_dict = {
    "board" : None,
    "available_indices" : None,
    "portals_dict" : None,
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

def main():
    boards_generator()
    creatures_board_division()
    fill_the_bard()


if __name__ == "__main__":
    main()

print(first_board.print_a_board(board_1_dict["board"]))
#print(first_board.print_a_board(board_2_dict["board"]))
#print(first_board.print_a_board(board_3_dict["board"]))
#moving_cars.cars_in_the_move(board_2_dict["board"], board_2_dict["list_of_creatures"])