import random
import player


def create_boss():
    boss = {'name': "Wyga", 'species': "fox", 'health': 20, "max_health": 20, "picture": "FFF"}

    return boss

def put_boss_on_board():
    pass


def fight_boss(weapon, boss):
    if weapon.get("name") == "Hen":
        boss["health"] = 0
            
    elif weapon.get("name") == "Cone":
        hit_fox = did_it_hit()
        if hit_fox:
            boss["health"] -= 1
        else:
            stone = stone_throw()
            hit_hero = did_it_hit()
            if stone and hit_hero:
                player.hero["health"] -= 3
            elif hit_hero:
                player.hero["health"] -= 1

    win = win_the_game()
    if win == True:
        exit()

    return boss


def stone_throw():
    number = random.randint(1, 5)
    return (number % 3 == 0)


def did_it_hit():
    hit = [True, False]
    return random.choice(hit)


def win_the_game(boss_health):
    if boss_health == 0 and player.hero.get("health") > 0:
        print("""
        .|||||||||.     
        ||||||||||||| 
        |||||||||||' .\\  
        `||||||||||_,__o                     |\_/|,,_____,~~`
                                    You win! (.".)~~     )`~
                                              \o/\ /---~\\ ~
                                                _//    _// ~}""")
        return True
    else:
        return False

