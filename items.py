import player


def create_items():
    apple = {'name' : "Apple", 'kind' : "Food", 'value_health' : 2, 'worm': False, 'collecting' : True, 'duration' : 60, 'picture' : "A"} # collecting - czy przedmiot podnosi się autoamtycznie, czy użytkownik musi wyrazić zgodę
    wormy_apple = {'name' : "Wormy Apple", 'kind' : "Food", 'value_healt' : 2, 'worm': True, 'collecting' : True, 'duration' :60, 'picture' : "Y"}
    egg = {'name' : "Egg", 'kind' : "Food", 'value_healt' : 5, 'collecting' : True, 'druration' : 5, 'picture' : "E"}
    cone = {'name' : "Cone", 'kind' : "Weapon", 'weight' : 1, 'power' : 1, 'collecting' : False, 'picture' : "C"} #nie znalazłem kodu
    stick = {'name' :"stick", 'kind' : "Tool", 'weight' : 2, 'collecting' : False, 'picture' : "S"} #hokejowy;)
    key = {'name' : "Key", 'kind' :"Tool", 'weight' : 1, 'pictures' : "K"}
    
    return apple,wormy_apple,egg,cone,stick,key 


def eat_food(food): #Tutaj brakowało parabetru hero?
    #pobieramy parametr food,bo nie tylko jabłko będzie dodawało 'życie'
    if player.hero["health"] + food.get("value_health",0) >= player.hero["max_health"]:
        player.hero["health"] = player.hero["max_health"]
    else:
        player.hero["health"] += food.get("value_health",0)
    

def random_items_locations(board, board_indexes, list_of_creatures):
    floor = " "

    for i in range(5):
        value = False
        while value is False:
            row_index, col_index = random.choice(board_indexes)
            if board[row_index][col_index] == floor:
                board[row_index][col_index] = creature["pic"]
                creature["location"] = (row_index, col_index)
                value = True

    return board, list_of_creatures