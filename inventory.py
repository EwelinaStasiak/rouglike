import items
import boss


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
            items.eat_food(list_of_items[index_name])
            
    elif first_letter.lower() == "e":
        if "Egg" in inventory_hero:
            index_name = items_name.index("Egg")
            remove_from_inventory("Egg")
            items.eat_food(list_of_items[index_name])
    elif first_letter.lower() == "c":
        if "Cone" in inventory_hero:
            index_name = items_name.index("Cone")
            remove_from_inventory("Cone")
            if fight_with_boss:
                boss = boss.fight_boss()
    elif first_letter.lower() == "s":
        pass
    elif first_letter.lower() == "k":
        pass