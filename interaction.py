import items
import inventory


def player_interaction(player, player_inventory, board, item, position_item, position_player):
    if item.get("kind") == "Food":
        choose_player = choose_interaction("Food", item.get("name"))
        if choose_player == "E":
            items.eat_food(player, item)
        elif choose_player == "I":
            inventory.add_to_inventory(player_inventory)
    elif item.get("kind") == "Weapon":
        pass
    elif item.get("kind") == "Tool":
        pass

def choose_interaction(kind, item_name):
    correct_answer = ["E", "I", "N"]
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
        return choose_player
    else:
        print("Invalid input! Please enter the correct answer")
    
