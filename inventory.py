def create_inventory():
    inventory = {"start":0}
    return inventory

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

