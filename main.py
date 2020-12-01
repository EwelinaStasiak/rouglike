import util
import ui
import movement
import creatures
import player
import first_board
import items
import inventory


def main():
    # global HERO
    # global inventory_hero

    # HERO = player.create_player("1")
    # inventory_hero = inventory.create_inventory()
    player.hero = player.create_player("1")
    inventory.inventory_hero = inventory.create_inventory()

    board_1, board_index, portals_dict = first_board.placing_chembers()
    board_1 = player.put_player_on_board(board_1)
    #board_index = gen_boards.board_indexes(board_1)
    worm, car, lory, dog, hen = creatures.creatures()
    
    
    list_of_creatures = creatures.creatures_on_the_board_dicts(worm)
    list_of_items = items.create_items()
    items_on_board = items.items_on_board(list_of_items)
    board_1, list_of_creatures = creatures.random_creatures_locations(board_1, board_index, list_of_creatures)
    board_1 = items.random_items_locations(board_1,board_index,items_on_board)
    icons = creatures.enemy_pics()
    
    util.clear_screen()
    ui.display_board(board_1)
     
    is_running = True

    while is_running:
        move_key = ["w", "s", "a", "d"]
        player.print_player_info()
        key = util.key_pressed()
        if not player.is_it_alive():
            is_running = False
            player.print_end_game()
        if key.lower() == 'q':
            is_running = False
            print("You exit the game!")
            exit()
        elif key.lower() in move_key:
            board_1, list_of_creatures = movement.player_move(board_1, key, list_of_creatures, inventory, list_of_items, portals_dict, board_index)
            board_1, list_of_creatures = movement.creature_movement(board_1, list_of_creatures)
            util.clear_screen()
            ui.display_board(board_1)
             
        elif key.lower() == "i":
            inventory.print_inventory()
            player_input = input("If you want to use an item from your inventory - press U ")
            if player_input.lower() == "u":
                name_item = input("Enter the name of the item you want to use")
                if name_item.lower() == "apple":
                    pass
                elif name_item.lower() == "egg":
                    pass
                elif name_item.lower() == "cone":
                    pass
                elif name_item.lower() == "stick":
                    pass
                elif name_item.lower() == "key":
                    pass

                
            #czy zatrzymać na kilka sekund ?
            # board_1, list_of_creatures = movement.player_move(board_1, key, list_of_creatures, inventory, list_of_items, portals_dict, board_index)
            # board_1, list_of_creatures = movement.creature_movement(board_1, list_of_creatures, icons)
            # util.clear_screen() 
            # ui.display_board(board_1)
        else:
            util.clear_screen()
            ui.display_board(board_1)


if __name__ == '__main__':
    main()
    