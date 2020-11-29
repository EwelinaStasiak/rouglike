import items
import inventory
import player


def player_interaction(board, item, position_item, position_player):
    kind = item.get("kind")
    choose_player = choose_interaction(kind, item.get("name"))
    if choose_player == "E":
        items.eat_food(item)
        board[position_player[0]][position_player[1]] = " "
        board[position_item[0]][position_item[1]] = player.hero.get("picture")
            
    elif choose_player == "I":
        inventory.add_to_inventory(item.get("name"))
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
