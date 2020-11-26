import util
import engine
import ui
import movement
import creatures
import gen_boards


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


def create_player(user_choice):
    'Tworzy bohatera wg wyboru użytkownika'
    if user_choice == "1":
        hero = {'name' : "Mikolaj", 'species' : "hedgehog", 'health' : 10, 'max_load' : 15}
    elif user_choice == "2":
        hero = {'name' : "Mikolaj", 'species' : " Magic hedgehog", 'health' : 15, 'max_load' : 10, 'skill' : "magic"}
    elif user_choice == "3":
        hero = {'name' : "Mikolaj", 'species' : "Invisible hedgehog", 'health' : 5, 'max_load' : 5, 'skill' : "invisible"}
    return hero

def create_items():
    apple = {'name' : "Apple", 'kind' : "Food", 'value_health' : 2, 'worm': False, 'collecting' : True, 'duration' : 60, 'picture' : 127822} # collecting - czy przedmiot podnosi się autoamtycznie, czy użytkownik musi wyrazić zgodę
    wormy_apple = {'name' : "Wormy Apple", 'kind' : "Food", 'value_healt' : 2, 'worm': True, 'collecting' : True, 'duration' :60, 'picture' : 127822}
    egg = {'name' : "Egg", 'kind' : "Food", 'value_healt' : 5, 'collecting' : True, 'druration' : 5, 'picture' : "E"}
    cone = {'name' : "Cone", 'kind' : "Weapon", 'weight' : 1, 'power' : 1, 'collecting' : False, 'picture' : "C"}
    stick = {'name' :"stick", 'kind' : "Tool", 'weight' : 2, 'collecting' : False, 'picture' : "S"}
    key = {'name' : "Key", 'kind' :"Tool", 'weight' : 1, 'pictures' : "K"}
    # worm = {'name' : "Worm", 'kind' : "Enemy", 'health' : 2, 'picture' : "W"} # przeniosłem do creatures.py zeby byly w jednum miejscu wszyscy wrogowie i stwory
    # hen = {'name' : "Hen", 'kind' : "Firend", 'health' : 5, 'picture' : "H"} # j.w.
    return apple,wormy_apple,egg,cone,stick,key #,worm,hen

def main(board):
    hero = create_player("1")
    apple,wormy_apple,egg,cone,stick,key = create_items() #,worm,hen
    worm, car, lorry, dog, hen = creatures.creatures()
    enemy_icons = creatures.enemy_pics()
    board_indices = gen_boards.board_indexes(board)
    
    board, creatures_location = creatures.random_creatures_locations(board, board_indices, worm["picture"], worm["num_to_place"])

    #board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    print(board)

    util.clear_screen()
    #print(board)
    ui.display_board(board) #W ten sposób będzie ju drukowało planszę tak jak ją będzie widać
    is_running = True
    while is_running:
        #engine.put_player_on_board(board, player)
        #ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            board = movement.player_move(board, PLAYER_ICON, key)
            board, creatures_location = movement.creature_movement(board, creatures_location)
            ui.display_board(board)
            #print(board)

        util.clear_screen()
        ui.display_board(board)
        #print(board)


if __name__ == '__main__':
    main(board)
