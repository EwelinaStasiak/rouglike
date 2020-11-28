def create_items():
    apple = {'name' : "Apple", 'kind' : "Food", 'value_health' : 2, 'worm': False, 'collecting' : True, 'duration' : 60, 'picture' : "A"} # collecting - czy przedmiot podnosi się autoamtycznie, czy użytkownik musi wyrazić zgodę
    wormy_apple = {'name' : "Wormy Apple", 'kind' : "Food", 'value_healt' : 2, 'worm': True, 'collecting' : True, 'duration' :60, 'picture' : "A"}
    egg = {'name' : "Egg", 'kind' : "Food", 'value_healt' : 5, 'collecting' : True, 'druration' : 5, 'picture' : "E"}
    cone = {'name' : "Cone", 'kind' : "Weapon", 'weight' : 1, 'power' : 1, 'collecting' : False, 'picture' : "C"} #nie znalazłem kodu
    stick = {'name' :"stick", 'kind' : "Tool", 'weight' : 2, 'collecting' : False, 'picture' : "S"} #hokejowy;)
    key = {'name' : "Key", 'kind' :"Tool", 'weight' : 1, 'pictures' : "K"}
    
    return apple,wormy_apple,egg,cone,stick,key 

def eat_food(hero, food): #Tutaj brakowało parabetru hero?
    #pobieramy parametr food,bo nie tylko jabłko będzie dodawało 'życie'
    if hero["health"] + food.get("value_health",0) > hero["max_health"]:
        pass
    else :
        hero["health"] += food.get("value_health",0)