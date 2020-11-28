import util
import engine
import ui
import movement
import creatures
import gen_boards
import player
import first_board


def main():
    PLAYER = player.create_player("1")
    board_1 = first_board.placing_chembers()
    board_1 = player.put_player_on_board(PLAYER, board_1)
    PLAYER_ICON = PLAYER.get("picture")
    board_index = gen_boards.board_indexes(board_1)
    worm, car, lory, dog, hen = creatures.creatures()
    ui.display_board(board_1)
    list_of_creatures = creatures.creatures_on_the_board_dicts(worm)
    board_1, list_of_creatures = creatures.random_creatures_locations(board_1, board_index, list_of_creatures)
    icons = creatures.enemy_pics()
    util.clear_screen()
    ui.display_board(board_1)
    util.clear_screen()

    is_running = True

    while is_running:
        ui.display_board(board_1)
        key = util.key_pressed()
        util.clear_screen()
        if key == 'q':
            is_running = False
        else:
            board_1, list_of_creatures = movement.player_move(board_1, PLAYER_ICON, key, list_of_creatures)
            board_1, list_of_creatures = movement.creature_movement(board_1, list_of_creatures, icons)
            ui.display_board(board_1)
            util.clear_screen()

if __name__ == '__main__':
    main()
