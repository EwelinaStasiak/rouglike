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
        hero = {'name' : "Mikolaj", 'species' : "hedgehog", 'health' : 10, 'max_load' : 15,"max_health" : 25, "picture" : 129428}
    elif user_choice == "2":
        hero = {'name' : "Mikolaj", 'species' : " Magic hedgehog", 'health' : 15, 'max_load' : 10, 'skill' : "magic","max_health" : 25,"picture" : 129428}
    elif user_choice == "3":
        hero = {'name' : "Mikolaj", 'species' : "Invisible hedgehog", 'health' : 5, 'max_load' : 5, 'skill' : "invisible","max_health" : 25,"picture" : 129428}
    inventory = {}
    return hero, inventory

def create_items():
    apple = {'name' : "Apple", 'kind' : "Food", 'value_health' : 2, 'worm': False, 'collecting' : True, 'duration' : 60, 'picture' : 127822} # collecting - czy przedmiot podnosi się autoamtycznie, czy użytkownik musi wyrazić zgodę
    wormy_apple = {'name' : "Wormy Apple", 'kind' : "Food", 'value_healt' : 2, 'worm': True, 'collecting' : True, 'duration' :60, 'picture' : 127822}
    egg = {'name' : "Egg", 'kind' : "Food", 'value_healt' : 5, 'collecting' : True, 'druration' : 5, 'picture' : 129370}
    cone = {'name' : "Cone", 'kind' : "Weapon", 'weight' : 1, 'power' : 1, 'collecting' : False, 'picture' : "C"} #nie znalazłem kodu
    stick = {'name' :"stick", 'kind' : "Tool", 'weight' : 2, 'collecting' : False, 'picture' : 127954} #hokejowy;)
    key = {'name' : "Key", 'kind' :"Tool", 'weight' : 1, 'pictures' : 128273}
    # worm = {'name' : "Worm", 'kind' : "Enemy", 'health' : 2, 'picture' : 128027} # przeniosłem do creatures.py zeby byly w jednum miejscu wszyscy wrogowie i stwory
    # hen = {'name' : "Hen", 'kind' : "Firend", 'health' : 5, 'picture' : 128020} j.w.
    return apple,wormy_apple,egg,cone,stick,key #,worm,hen

def eat_food(hero, food): #Tutaj brakowało parabetru hero?
    #pobieramy parametr food,bo nie tylko jabłko będzie dodawało 'życie'
    if hero["health"] + food.get("value_health",0) > hero["max_health"]:
        pass
    else :
        hero["health"] += food.get("value_health",0)

def is_it_alive(heros): #Tutaj brakowało parabetru heros?
    if heros["health"] <= 0:
        return False
    return True

def add_to_inventory(inventory, added_items):
    for elements in added_items:
        for key in inventory:
            if key == elements:
                inventory[key] += 1
    for elements in added_items:
        if elements not in inventory:
            inventory[elements] = 1

def remove_from_inventory(inventory, removed_items):
    check_if_null = []
    for elements in removed_items:
        for key in inventory:
            if key == elements:
                inventory[key] -= 1
    for key, value in inventory.items():
        if value <= 0:
            check_if_null.append(key)
    for elements in check_if_null:
        inventory.pop(elements)

def print_inventory(inventory):# if user press "I"
    #do porawy inteligentne formatowanie zależne od długości najdłuższego key w inventory
    print(20*"-")
    print("{:>12} | {:<5}".format("item","count"))
    print(20*"-")
    for key,value in inventory.items():
        print("{:>12} | {:<5}".format(key,value))
    print(20*"-")

# def main(board):
#     hero = create_player("1")
#     apple,wormy_apple,egg,cone,stick,key = create_items() #,worm,hen
#     worm, car, lorry, dog, hen = creatures.creatures()

def main(board):
    hero, inventory = create_player("1")
    apple,wormy_apple,egg,cone,stick,key = create_items() #,worm,hen
    worm, car, lory, dog, hen = creatures.creatures()
    icons = creatures.enemy_pics() + [hero["picture"]]
    list_of_creatures = creatures.creatures_on_the_board_dicts(worm)
    board_indices = gen_boards.board_indexes(board)
    board, list_of_creatures = creatures.random_creatures_locations(board, board_indices, list_of_creatures)
    

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
            board, list_of_creatures = movement.player_move(board, PLAYER_ICON, key, list_of_creatures)
            board, list_of_creatures = movement.creature_movement(board, list_of_creatures, icons)
            ui.display_board(board)

            #print(board)

        util.clear_screen()
        ui.display_board(board)
        #print(board)
        for el in list_of_creatures:
            print(el["health"])
        # print(list_of_creatures[0]["health"])
        # print(list_of_creatures[1]["health"])
        # print(list_of_creatures[2]["health"])
        # print(list_of_creatures[3]["health"])
        # print(list_of_creatures[4]["health"])

if __name__ == '__main__':
    main(board)
