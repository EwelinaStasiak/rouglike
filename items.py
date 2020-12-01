import player
import random


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

