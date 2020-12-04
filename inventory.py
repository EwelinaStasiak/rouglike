import random
import creatures
from termcolor import colored


"""
*******************************
            INVENTORY
*******************************
"""


def create_inventory():

    global inventory_hero
    inventory_hero = {"Key": 0}

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

    global inventory_hero
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

    return inventory_hero


def print_inventory():  # if user press "I"
    #do porawy inteligentne formatowanie zależne od długości najdłuższego key w inventory
    print(20*"-")
    print("{:>12} | {:<5}".format("item", "count"))
    print(20*"-")

    for key, value in inventory_hero.items():
        print("{:>12} | {:<5}".format(key, value))
    print(20*"-")


def choose_item_to_use():

    first_letter = input(colored("Enter the first letter of the item you want to use \n", "blue"))
    item = ""

    if first_letter.lower() == "a":
        item = "Apple"
    elif first_letter.lower() == "e":
        item = "Egg"
    elif first_letter.lower() == "c":
        item = "Cone"
    elif first_letter.lower() == "s":
        item = "Stick"
    elif first_letter.lower() == "k":
        item = "Key"
    elif first_letter.lower() == "h":
        item = "Hen"
    else:
        item = None

    return item


def use_item_from_inventory(list_of_items, item, fight_with_boss=False):

    items_names = []
    if item != "Hen":
        for items in list_of_items:
            items_names.append(items.get("name"))
        item_index = items_names.index(item)

    if item == "Apple" or item == "Egg":
        eat_food(list_of_items[item_index])
    elif item == "Cone" and fight_with_boss:
        creatures.fight_boss(list_of_items[item_index])
    elif item == "Hen" and fight_with_boss:
        creatures.fight_boss(item)


"""
*******************************
            ITEMS
*******************************
"""


def create_items():

    apple = {'name': "Apple", 'kind': "Food", 'value_health': 2, 'num_to_place': 5, 'collecting': True, 'duration': 60, 'picture': "A"} 
    egg = {'name': "Egg", 'kind': "Food", 'value_health': 5, 'collecting': True, 'num_to_place': 2, 'picture': "E"}
    cone = {'name' : "Cone", 'kind' : "Weapon", 'weight' : 1, 'num_to_place': 5, 'collecting': False, 'picture': "V"}
    key = {'name': "Key", 'kind':"Tool", 'weight': 1, 'num_to_place': 1,'picture': "K"}

    list_of_items = [apple, egg, cone, key]

    return list_of_items


def items_on_board(list_of_items):

    items_on_board = []

    for item in list_of_items:
        for i in range(item["num_to_place"]):
            items_on_board.append(item)

    return items_on_board


def eat_food(food):

    if creatures.hero["health"] + food.get("value_health", 0) > creatures.hero["max_health"] and creatures.hero["health"] < creatures.hero["max_health"]:
        creatures.hero["health"] = creatures.hero["max_health"]
    elif creatures.hero["health"] == creatures.hero["max_health"]:
        print(colored("You have the maximum amount of health. Food will be added to your inventory", "blue"))
        add_to_inventory([food.get("name")])
    else:
        creatures.hero["health"] += food.get("value_health", 0)


def random_items_locations(new_board, board_indexes, items_on_board, num_board):

    floor = " "
    road_rows = [14, 15, 16, 17, 18, 19, 20, 21]
    boss_rows = [35, 36, 37, 38, 39]
    road_width = 6
    boss_high = 5

    if num_board == 3:
        for item in items_on_board:
            if item.get("name") == "Key":
                items_on_board.remove(item)

    for item in items_on_board:
        value = False
        while value is False:
            row_index, col_index = random.choice(board_indexes)
            
            if num_board == 2:
                if row_index in road_rows:
                    row_index = row_index + road_width
            elif num_board == 3:
                if row_index in boss_rows:
                    row_index = row_index - boss_high

            if new_board[row_index][col_index] == floor:
                new_board[row_index][col_index] = item.get("picture")
                value = True

    return new_board


"""
*******************************
        INTERACTION
*******************************
"""


def player_interaction(board, item, position_item, position_player):

    kind = item.get("kind")
    choose_player = choose_interaction(kind, item.get("name"))

    if choose_player.upper() == "E":
        eat_food(item)
        board[position_player[0]][position_player[1]] = " "
        board[position_item[0]][position_item[1]] = creatures.hero.get("picture")  
    elif choose_player.upper() == "I":
        add_to_inventory([item.get("name")])
        board[position_player[0]][position_player[1]] = " "
        board[position_item[0]][position_item[1]] = creatures.hero.get("picture")
    elif choose_player.upper() == "N":
        pass

    return board


def choose_interaction(kind, item_name):

    correct_answer = ["E", "I", "N"]
    is_invalid = True

    while is_invalid:
        if kind == "Food":
            choose_player = input(colored(f"""
                            You found {item_name}. What do you want to do with it?
                                    Press E to eat {item_name}
                                    Press I to add to inventory {item_name}
                                    Press N if you don't want to eat or collect {item_name} \n""", "blue"))

        elif kind == "Weapon" or kind == "Tool" or kind == "Friend":
            choose_player = input(colored(f"""
                            You found {item_name}. What do you want to do with it?
                                    Press I to add to inventory {item_name}
                                    Press N if you don't want to eat or collect {item_name} \n""", "blue"))

        if choose_player.upper() in correct_answer:
            is_invalid = False
        else:
            print(colored("Invalid input! Please enter the correct answer", "red"))

    return choose_player


# def main():
#     global inventory_hero
#     inventory_hero = create_inventory()
#     print_inventory()
#     list_of_items = create_items()
#     inventory_hero = use_item_from_inventory(list_of_items, fight_with_boss=True)
#     print_inventory()

# if __name__ == "__main__":
#     main()
