import util
import engine
import ui
import movement


PLAYER_ICON = '@'
# PLAYER_START_X = 3
# PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


# tablica do testów
board = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "@", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():
    #player = create_player()
    #board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    print(board)

    util.clear_screen()
    print(board)
    is_running = True
    while is_running:
        #engine.put_player_on_board(board, player)
        #ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            movement.player_move(key, board, PLAYER_ICON)
            print(board)

        util.clear_screen()
        print(board)


if __name__ == '__main__':
    main()
