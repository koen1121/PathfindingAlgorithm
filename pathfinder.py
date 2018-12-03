from map import Map


map_array = [
    ['_', '_', '_', 'X', 'X', '_', 'X', '_'],
    ['_', 'X', '_', '_', 'X', '_', '_', '_'],
    ['S', 'X', 'X', '_', '_', '_', 'X', '_'],
    ['X', 'X', '_', 'X', 'X', '_', '_', '_'],
    ['_', 'X', '_', 'X', 'X', '_', 'X', '_'],
    ['_', 'X', '_', '_', 'X', '_', 'X', '_'],
    ['X', 'X', 'X', '_', '_', '_', 'X', '_'],
    ['X', '_', '_', 'F', 'X', '_', '_', '_']
]

map = Map(map_array, 30, 30)

main_queue = []
main_queue.append((map.get_finish(), 0))

for point in main_queue:
    temp_list = []
    for temp_point in map.get_adjacent_cells(point[0]):
        temp_list.append((temp_point, point[1] + 1))

    for temp in temp_list.copy():
        try:
            value = map.get_coords(temp[0])

            if value == 'X' or map.outofbounds(temp[0]):
                temp_list.remove(temp)

            for item in main_queue.copy():

                if item[0] == temp[0] and item[1] <= temp[1]:
                    temp_list.remove(temp)

        except IndexError:
            temp_list.remove(temp)

    for item in temp_list:
        main_queue.append(item)

    if map.get_coords(point[0]) == 'S':
        break


for calculated_point in main_queue:
    if map.get_coords(calculated_point[0]) != 'X' and map.get_coords(calculated_point[0]) != 'F' \
            and map.get_coords(calculated_point[0]) != 'S':

        map.update_matrix(calculated_point[0], calculated_point[1])

print()
map.draw_map()











