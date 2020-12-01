import random
import player

def who_is_the_oponent(list_of_creatures, location):
    for creature in list_of_creatures:
        if location == creature["location"]:
            return list_of_creatures.index(creature)
        elif location == player.hero.get("location"):
            return False

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

def hit_the_opponent(attacker, opponent):
    if did_it_hit():
        opponent = carry_damage(attacker, opponent)
        if opponent:
            return opponent
        else:
            return None
    else:
        print("You missed, sucker!")
        return False

# def random_damage(min_damage, max_damage):
#     return random.randint(min_damage, max_damage)

def fight(board, attacker, list_of_creatures, location):
    row, col = location
    creature_index = who_is_the_oponent(list_of_creatures, location)

    if creature_index:
        opponent = list_of_creatures[creature_index]
        opponent = hit_the_opponent(attacker, opponent)
        if opponent:
            list_of_creatures[creature_index] = opponent
        elif opponent is None:
            list_of_creatures.remove(list_of_creatures[creature_index])
            board[row][col] = " "
    else:
        opponent = player.hero
        opponent = hit_the_opponent(attacker, opponent)
        if opponent:
            player.hero = opponent
    
    return board, list_of_creatures

#list_of_creatures = [{'name': 'Worm', 'health': 15, 'min_damage': 1, 'max_damage': 20, 'num_to_place': 5, 'pic': 'W', 'location': (2, 7)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 2)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (5, 5)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 5)}, {'name': 'Worm', 'health': 2, 'min_damage': 1, 'max_damage': 1, 'num_to_place': 5, 'pic': 'W', 'location': (3, 3)}]
#location =(2, 7)

