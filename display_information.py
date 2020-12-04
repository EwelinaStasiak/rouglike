import util
from termcolor import colored


def press_enter():
    input(colored("Press Enter to continue...", "cyan"))


def choose_hero():
    print(colored("""
    Choose your hero:
    1. Hedgehog Mikolaj 
    2. Magic hedgehog Mikolaj 
    3. Invisible hedgehog Mikolaj \n
    """, "blue"))


def win_screen():
    print(colored("""
        .|||||||||.     
        ||||||||||||| 
        |||||||||||' .\\  
        `||||||||||_,__o                     |\_/|,,_____,~~`
                                    You win! (.".)~~     )`~
                                              \o/\ /---~\\ ~
                                                _//    _// ~}""", "blue"))


def print_end_game():
    print(colored('''
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

    ''', "blue"))


def name_game():
    print(colored("""

     _____ _           ______          __          _      ___              _      
    |_   _| |          | ___ \        / _|        | |    / _ \            | |     
      | | | |__   ___  | |_/ /__ _ __| |_ ___  ___| |_  / /_\ \_ __  _ __ | | ___ 
      | | | '_ \ / _ \ |  __/ _ \ '__|  _/ _ \/ __| __| |  _  | '_ \| '_ \| |/ _\\
      | | | | | |  __/ | | |  __/ |  | ||  __/ (__| |_  | | | | |_) | |_) | |  __/
      \_/ |_| |_|\___| \_|  \___|_|  |_| \___|\___|\__| \_| |_/ .__/| .__/|_|\___|
                                                          | |   | |           
                                                          |_|   |_|           
                                                          
                                                                                    
                                                    ___
                                                _/`.-'`.
                                        _      _/` .  _.'
                            ..:::::.(_)   /` _.'_./
                            .oooooooooo\ \o/.-'__.'o.
                            .ooooooooo`._\_|_.'`oooooob.
                        .ooooooooooooooooooooo&&oooooob.
                        .oooooooooooooooooooo&@@@@@@oooob.
                        .ooooooooooooooooooooooo&&@@@@@ooob.
                        doooooooooooooooooooooooooo&@@@@ooob
                        doooooooooooooooooooooooooo&@@@oooob
                        dooooooooooooooooooooooooo&@@@ooooob
                        dooooooooooooooooooooooooo&@@oooooob
                        `dooooooooooooooooooooooooo&@ooooob'
                        `doooooooooooooooooooooooooooooob'
                        `doooooooooooooooooooooooooooob'
                        `doooooooooooooooooooooooooob'
                         `doooooooooooooooooooooooob'
                          `doooooooooooooooooooooob'
                           `dooooooooobodoooooooob'
                            `doooooooob dooooooob'
                                `"""""""' `""""""'                                                      
                                                          """, "red"))

    press_enter()


def start_story():
    print(colored("""

    The hedgehog Mikolaj decided to go in search of the perfect apple...
    He didn't know this trip would be so dangerous.



                         .|||||||||.          
                        |||||||||||||      Oh.. I must have the Perfect Apple!  
                        |||||||||||' .\      
                        `||||||||||_,__o    
                   
                        """, "blue"))

    press_enter()


def rules_game():
    print(colored("""
    Rules game:
    1. Collect apples (A) and eggs (E) to heal yourself.
    2. Collect cones (V) - they will be useful for the final fight.
    3. Find the key (K) to go to the next level.
    4. To use an item from your inventory press I.
    5. Move keys: W, S, A, D.
     """, "blue"))

    press_enter()


def first_board_rules():
    print(colored("""
    Hints:
    1. Watch out for opponents - dogs(D) and worms(W).
    2. You can move between chambers using portals (O).
    3. Collect useful items - apple (A), egg(E), cone (V).
    4. Remember to find the key.
    """, "blue"))

    press_enter()   


def second_board_rules():
    print(colored("""
    Hints:
    1. Be careful when crossing the road there are cars (C) and lorries (L) on it.
    2. Find a friendly hen (H), maybe she can help.
    3. Collect useful items - apple (A), egg(E), cone (V).
    4. Remember to find the key.
    """, "blue"))
    press_enter()


def third_board_rules():
    print(colored("""
    Hints:
    1. Watch out for the fox(F).
    2. Collect useful items - apple (A), egg(E), cone (V).
    3. Use the cones to fight the fox.
    """, "blue"))

    press_enter()


def start_game():
    util.clear_screen()
    name_game()
    util.clear_screen()
    start_story()
    util.clear_screen()
    rules_game()
    util.clear_screen()
    