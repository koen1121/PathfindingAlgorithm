from termcolor import colored
from prettytable import PrettyTable

class Map:
    def __init__(self, matrix):
        self.matrix = matrix
        self.print()

    def get_start(self):
        x, y = 1, 1

        for row in self.matrix:
            for item in row:
                if item == 'S':
                    return x, y
                else:
                    x += 1
            x = 1
            y += 1

    def get_finish(self):
        x, y = 1, 1

        for row in self.matrix:
            for item in row:
                if item == 'F':
                    return x, y
                else:
                    x += 1

            x = 1
            y += 1

    def outofbounds(self, coords):
        if coords[0] > len(self.matrix[0]) or coords[0] < 1:
            return True

        elif coords[1] > len(self.matrix) or coords[1] < 1:
            return True

        else:
            return False

    def get_coords(self, coords):
        row = self.matrix[coords[1] - 1]

        return row[coords[0] - 1]

    def update_matrix(self, coords, value):
        self.matrix[coords[1] - 1][coords[0] - 1] = value

    def get_adjacent_cells(self, coords):

        point_list = []
        # left point
        point_list.append((coords[0] - 1, coords[1]))

        # right point
        point_list.append((coords[0] + 1, coords[1]))

        # top point
        point_list.append((coords[0], coords[1] + 1))

        # bottom point
        point_list.append((coords[0], coords[1] - 1))

        return point_list

    def print(self):
        for row in self.matrix:
            for item in row:
                if item == 'X' or item == '_' or item == 'S' or item == 'F':
                    print(item, end=" ")

                else:
                    print(colored(item, 'red'), end=" ")

            print()

    def print_table(self):
        x = PrettyTable()

        for row in self.matrix:
            x.add_row(row)

        print(x)




map_array = [
    ['S', '_', '_', 'X', 'X', '_', 'X', '_'],
    ['_', 'X', '_', '_', 'X', '_', '_', '_'],
    ['_', 'X', 'X', '_', '_', '_', 'X', '_'],
    ['X', 'X', '_', '_', 'X', '_', '_', '_'],
    ['_', 'X', '_', 'X', 'X', '_', 'X', '_'],
    ['_', 'X', '_', '_', 'X', '_', 'X', '_'],
    ['X', 'X', 'X', '_', '_', '_', 'X', '_'],
    ['X', '_', '_', 'F', 'X', '_', '_', '_']
]

map = Map(map_array)

main_queue = []
main_queue.append((map.get_finish(), 0))

for point in main_queue:


    # if count > 1000:
    #     break

    temp_list = []
    print(point[0])
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
print()
map.print_table()

print(map.get_adjacent_cells((3, 4)))











