import random


def creatures():
    worm = {'name' : "Worm", 'kind' : "Enemy", 'health' : 2, "min_damage" : 1, "max_damage" : 1, "num_to_place" : 5, 'pic' : "W"} #128027}
    car = {'name' : "Car", 'kind' : "Enemy", 'health' : 20, "min_damage" : 5, "max_damage" : 10, "num_to_place" : 15, 'pic' : "C"} #128663}
    lorry = {'name' : "Lorry", 'kind' : "Enemy", 'health' : 20, "min_damage" : 20, "max_damage" : 50, "num_to_place" : 5, 'pic' : "L"} #128666}
    dog = {'name' : "Dog", 'kind' : "Enemy", 'health' : 20, "min_damage" : 1, "max_damage" : 5, "num_to_place" : 5, 'pic' : "D"} #128021}
    hen = {'name' : "Hen", 'kind' : "Firend", 'health' : 5, "num_to_place" : 1, 'pic' : "H"} #128020}

    return worm, car, lorry, dog, hen

    
def creatures_on_the_board_dicts(creature):
    list_of_creatures = []
    
    for num in range(creature["num_to_place"]):
        monster = {}
        for key, value in creature.items():
            monster[key] = value
        list_of_creatures.append(monster)
    
    return list_of_creatures


def random_creatures_locations(board, board_indexes, list_of_creatures):
    floor = " "

    for creature in list_of_creatures:
        value = False
        while value is False:
            row_index, col_index = random.choice(board_indexes)
            if board[row_index][col_index] == floor:
                board[row_index][col_index] = creature["pic"]
                creature["location"] = (row_index, col_index)
                value = True

    return board, list_of_creatures

def non_road_coordinates(board_indices, road_rows):
    row = 0
    for indices in board_indices:
        if indices[row] in road_rows:
            board_indices.remove(indices)
    
    return board_indices

def car_placement(board, board_indices, list_of_vehiculs):
    vehiculs_to_place = len(list_of_vehiculs)
    road_rows = [15, 16, 17, 19, 20, 21]
    non_road_indices = non_road_coordinates(board_indices, road_rows)
    min_col = 1
    max_col = 78

    while vehiculs_to_place > 0:
        row_index = random.choice(road_rows)
        col_index = random.randint(min_col, max_col)
        
        if board[row_index][col_index] == " " and board[row_index][col_index + 2] == " ":
            vehicul = list_of_vehiculs[vehiculs_to_place - 1]
            if vehicul["name"] == "Lorry":
                board[row_index][col_index : col_index + 2] = [vehicul["pic"]] * 2
                vehicul["location"] = (row_index, col_index)
            elif vehicul["name"] == "Car":
                board[row_index][col_index] = vehicul["pic"]
                vehicul["location"] = (row_index, col_index)
            else:
                random_creatures_locations(board, non_road_indices, [vehicul])
            vehiculs_to_place -= 1
    
    return board, list_of_vehiculs

# def random_creatures_locations(board, board_indexes, list_of_creatures):
#     floor = " "
#     creatures_locations = []
    
#     while creatures_number > 0:
#         row_index, col_index = random.choice(board_indexes)
#         if board[row_index][col_index] == floor:
#             board[row_index][col_index] = creature_icon
#             creatures_locations.append((row_index, col_index))
#             creatures_number -= 1

#     return board, creatures_locations


def enemy_pics():
    creatures_list = creatures()
    enemy_pics = []

    for el in creatures_list:
        if el["kind"] == "Enemy":
            enemy_pics.append(el["pic"])
    
    return enemy_pics

# def main():
#     board_list = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", "@", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
    
#     #worm_1, worm_2, worm_3, worm_4, worm_5 = list_of_creatures
    
#     board_index = gen_boards.board_indexes(board_list)
#     worm, car, lory, dog, hen = creatures()
#     list_of_creatures = creatures_on_the_board_dicts(worm)
#     board, list_of_creatures = random_creatures_locations(board_list, board_index, list_of_creatures)
#     ui.display_board(board_list)


if __name__ == "__main__":
    pass
    #main()



