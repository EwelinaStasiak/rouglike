import random

def who_is_the_oponent(list_of_creatures, location):
    for creature in list_of_creatures:
        if creature["location"] == location: return list_of_creatures.index(creature)

def carry_damage(attacker, opponent):
    damage = random.randint(attacker["min_damage"], attacker["max_damage"])
    opponent["health"] -= damage

    if opponent["health"] > 0:
        return opponent
    else:
        return False

def did_it_hit():
    hit = [True, False]
    return random.choice(hit)

# def random_damage(min_damage, max_damage):
#     return random.randint(min_damage, max_damage)

def fight(board, attacker, list_of_creatures, location):
    row, col = location
    #opponent = list_of_creatures[0]
    creature_index = who_is_the_oponent(list_of_creatures, location)
    opponent = list_of_creatures[creature_index]
    #print(carry_damage(opponent, 2))
    hit = did_it_hit()
    if hit:
        opponent = carry_damage(attacker, opponent)
        if opponent:
            list_of_creatures[creature_index] = opponent
        else:
            list_of_creatures.remove(list_of_creatures[creature_index])
            board[row][col] = " "
    else:
        print("You missed, sucker!")

    return board, list_of_creatures

#list_of_creatures = [{'name': 'Worm', 'health': 15, 'min_damage': 1, 'max_damage': 20, 'num_to_place': 5, 'pic': 'W', 'location': (2, 7)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 2)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (5, 5)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 5)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 3)}]
#location =(2, 7)

