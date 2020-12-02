import random
import creatures


"""
*******************************
            INVENTORY
*******************************
"""


def create_inventory():
    global inventory_hero
    inventory_hero = {"start": 0}
    return inventory_hero


def add_to_inventory(added_items):
    for elements in added_items:
        for key in inventory_hero:
            if key == elements:
                inventory_hero[key] += 1
    for elements in added_items:
        if elements not in inventory_hero:
            inventory_hero[elements] = 1


def remove_from_inventory(removed_items):
    check_if_null = []
    for elements in removed_items:
        for key in inventory_hero:
            if key == elements:
                inventory_hero[key] -= 1
    for key, value in inventory_hero.items():
        if value <= 0:
            check_if_null.append(key)
    for elements in check_if_null:
        inventory_hero.pop(elements)


def print_inventory():  # if user press "I"
    #do porawy inteligentne formatowanie zależne od długości najdłuższego key w inventory
    print(20*"-")
    print("{:>12} | {:<5}".format("item", "count"))
    print(20*"-")
    for key, value in inventory_hero.items():
        print("{:>12} | {:<5}".format(key, value))
    print(20*"-")


def use_item_from_inventory(list_of_items, fight_with_boss=False):
    items_name = []
    for item in list_of_items:
        items_name.append(item.get("name"))

    first_letter = input("Enter the first letter of the item you want to use")
    if first_letter.lower() == "a":
        if "Apple" in inventory_hero:
            index_name = items_name.index("Apple")
            remove_from_inventory("Apple")
            eat_food(list_of_items[index_name])
            
    elif first_letter.lower() == "e":
        if "Egg" in inventory_hero:
            index_name = items_name.index("Egg")
            remove_from_inventory("Egg")
            eat_food(list_of_items[index_name])
    elif first_letter.lower() == "c":
        if "Cone" in inventory_hero:
            index_name = items_name.index("Cone")
            remove_from_inventory("Cone")
            if fight_with_boss:
                creatures.fight_boss(list_of_items[index_name])
    elif first_letter.lower() == "s":
        pass
    elif first_letter.lower() == "k":
        pass


"""
*******************************
            ITEMS
*******************************
"""


def create_items():
    apple = {'name' : "Apple", 'kind' : "Food", 'value_health' : 2, 'num_to_place': 10, 'collecting' : True, 'duration' : 60, 'picture' : "A"} # collecting - czy przedmiot podnosi się autoamtycznie, czy użytkownik musi wyrazić zgodę
    #wormy_apple = {'name' : "Wormy Apple", 'kind' : "Food", 'value_healt' : 2, 'worm': True, 'collecting' : True, 'duration' :60, 'picture' : "Y"}
    egg = {'name' : "Egg", 'kind' : "Food", 'value_healt' : 5, 'collecting' : True, 'num_to_place': 2, 'picture' : "E"}
    cone = {'name' : "Cone", 'kind' : "Weapon", 'weight' : 1, 'num_to_place': 10, 'collecting' : False, 'picture' : "C"} #nie znalazłem kodu
    stick = {'name' :"stick", 'kind' : "Tool", 'weight' : 2, 'collecting' : False, 'picture' : "S"} #hokejowy;)
    key = {'name' : "Key", 'kind' :"Tool", 'weight' : 1, 'num_to_place': 1,'picture' : "K"}
    list_of_items = [apple,egg,cone,key]
    return list_of_items

def items_on_board(list_of_items):
    items_on_board =[]
    for item in list_of_items:
        for i in range(item["num_to_place"]):
            items_on_board.append(item)
    return items_on_board


def eat_food(food): #Tutaj brakowało parabetru hero?
    #pobieramy parametr food,bo nie tylko jabłko będzie dodawało 'życie'
    if player.hero["health"] + food.get("value_health",0) > player.hero["max_health"]:
        pass
    else :
        player.hero["health"] += food.get("value_health",0)
    

def random_items_locations(board, board_indexes, items_on_board):
    floor = " "
    for item in items_on_board:
        value = False
        while value is False:
            row_index, col_index = random.choice(board_indexes)
            if board[row_index][col_index] == floor:
                board[row_index][col_index] = item.get("picture")
                value = True

    return board


"""
*******************************
        INTERACTION
*******************************
"""
def player_interaction(board, item, position_item, position_player):
    kind = item.get("kind")
    choose_player = choose_interaction(kind, item.get("name"))
    if choose_player == "E":
        items.eat_food(item)
        board[position_player[0]][position_player[1]] = " "
        board[position_item[0]][position_item[1]] = player.hero.get("picture")
            
    elif choose_player == "I":
        inventory.add_to_inventory(item)
        board[position_player[0]][position_player[1]] = " "
        board[position_item[0]][position_item[1]] = player.hero.get("picture")
    elif choose_player == "N":
        pass
    
    return board


def choose_interaction(kind, item_name):
    correct_answer = ["E", "I", "N"]
    is_invalid = True
    while is_invalid:
        if kind == "Food":
            choose_player = input(f"""
                            You found {item_name}. What do you want to do with it?
                                    Press E to eat {item_name}
                                    Press I to add to inventory {item_name}
                                    Press N if you don't want to eat or collect {item_name}""")
            
        elif kind == "Weapon" or kind == "Tool":
            choose_player = input(f"""
                            You found {item_name}. What do you want to do with it?
                                    Press I to add to inventory {item_name}
                                    Press N if you don't want to eat or collect {item_name}""")
        
        if choose_player in correct_answer:
            is_invalid = False
        else:
            print("Invalid input! Please enter the correct answer")
    return choose_player
