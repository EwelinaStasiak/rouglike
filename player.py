


def create_player(user_choice):
    global hero
    'Tworzy bohatera wg wyboru użytkownika'
    if user_choice == "1":
        hero = {'name': "Mikolaj", 'species': "hedgehog", 'health': 10, 'max_load': 15, "max_health": 25, "picture": "@"}
    elif user_choice == "2":
        hero = {'name': "Mikolaj", 'species': " Magic hedgehog", 'health': 15, 'max_load': 10, 'skill': "magic", "max_health": 25, "picture": "@"}
    elif user_choice == "3":
        hero = {'name': "Mikolaj", 'species': "Invisible hedgehog", 'health': 5, 'max_load': 5, 'skill': "invisible", "max_health": 25, "picture": "@"}    
    return hero


def put_player_on_board(board):
    
    player_icon = hero.get("picture")
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "#" and board[row + 1][col] == "#" and board[row][col + 1] == "#":
                player_start_row = row + 1
                player_start_col = col + 2
                board[player_start_row][player_start_col] = player_icon
                
                return board


def is_it_alive(): #Tutaj brakowało parabetru heros?
    if hero["health"] <= 0:
        return False
    return True


def print_player_info():
    print(f"Player's name : {hero['name']}     Health level : {hero['health']}")


def print_end_game():
    print('''
        xxxxxxxxx   xxx      xxx   xxxxx 
        xxxxxxxxx   xxxx     xxx   xxx xxx
        xxx         xxxxx    xxx   xxx  xxx
        xxx         xxxxxx   xxx   xxx   xxx
        xxxxxxxxx   xxx xxx  xxx   xxx    xxx
        xxxxxxxxx   xxx  xxx xxx   xxx    xxx
        xxx         xxx   xxxxxx   xxx   xxx
        xxx         xxx    xxxxx   xxx  xxx
        xxxxxxxxx   xxx     xxxx   xxx xxx
        xxxxxxxxx   xxx      xxx   xxxxxx
    
    Unfortunately, your hero lost his life

    ''')