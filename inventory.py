def create_inventory():
    global inventory_hero
    inventory_hero = {"start": 0}
    

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

