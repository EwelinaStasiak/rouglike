import random
import gen_boards
import ui

def creatures():
     worm = {'name' : "Worm", 'kind' : "Enemy", 'health' : 2, "min_damage" : 1, "max_damage" : 1, "num_to_place" : 5, 'pic' : "W"} #128027}
     car = {'name' : "Car", 'kind' : "Enemy", 'health' : 20, "min_damage" : 5, "max_damage" : 10, "num_to_place" : 15, 'pic' : "C"} #128663}
     lorry = {'name' : "Car", 'kind' : "Enemy", 'health' : 20, "min_damage" : 20, "max_damage" : 50, "num_to_place" : 5, 'pic' : "L"} #128666}
     dog = {'name' : "Car", 'kind' : "Enemy", 'health' : 20, "min_damage" : 1, "max_damage" : 5, "num_to_place" : 5, 'pic' : "D"} #128021}
     hen = {'name' : "Hen", 'kind' : "Firend", 'health' : 5, 'picture' : "H"} #128020}

     return worm, car, lorry, dog, hen
    
def random_creatures_locations(board, board_indexes, creature_icon, creatures_number = 10):
    floor = " "
    creatures_locations = []
    
    while creatures_number > 0:
        row_index, col_index = random.choice(board_indexes)
        if board[row_index][col_index] == floor:
            board[row_index][col_index] = creature_icon
            creatures_locations.append((row_index, col_index))
            creatures_number -= 1

    return board, creatures_locations

def enemy_pics():
    creatures_list = creatures()
    enemy_pics = []

    for el in creatures_list:
        if el["kind"] == "Enemy":
            enemy_pics.append(el["pic"])
    
    return enemy_pics

def main():
    board_list = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "@", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
    
    worm, car, lory, dog, hen = creatures()
    creature_icon = "W"
    board_index = gen_boards.board_indexes(board_list)
    board_list = random_creatures_locations(board_list, board_index, creature_icon, 5)
    ui.display_board(board_list)


if __name__ == "__main__":
    main()



