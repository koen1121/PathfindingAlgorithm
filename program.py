import queue

class Map:
    def __init__(self, matrix):
        self.matrix = matrix
        self.print()

    def get_start(self):
        x, y = 1, 1

        for row in self.matrix:
            for item in row:
                if item == 2:
                    return x, y
                else:
                    x += 1
            x = 1
            y += 1

    def get_finish(self):
        x, y = 1, 1

        for row in self.matrix:
            for item in row:
                if item == 3:
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

    def print(self):
        for row in self.matrix:
            for item in row:
                if item == 0:
                    print('_', end=" ")
                elif item == 1:
                    print('X', end=" ")
                elif item == 2:
                    print('S', end=" ")
                elif item == 3:
                    print('F', end=" ")
                else:
                    print(item, end=" ")

            print()


map_array = [
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [2, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 3, 0, 1, 0, 0, 0]
]

map = Map(map_array)

main_queue = []
main_queue.append((map.get_finish(), 0))


for point in main_queue:
    if map.get_coords(point[0]) == 2:
        break

    temp_list = []

    # left point
    temp_list.append(((point[0][0] - 1, point[0][1]), point[1] + 1))

    # right point
    temp_list.append(((point[0][0] + 1, point[0][1]), point[1] + 1))

    # top point
    temp_list.append(((point[0][0], point[0][1] + 1), point[1] + 1))

    # bottom point
    temp_list.append(((point[0][0], point[0][1] - 1), point[1] + 1))

    for temp in temp_list.copy():
        try:
            value = map.get_coords(temp[0])

            if value == 1 or map.outofbounds(temp[0]):
                temp_list.remove(temp)

            for item in main_queue.copy():
                if item[0] == temp[0] and item[1] <= temp[1]:
                    temp_list.remove(temp)

        except IndexError:
            temp_list.remove(temp)

    for item in temp_list:
        main_queue.append(item)


for calculated_point in main_queue:
    if map.get_coords(calculated_point[0]) != 2 and map.get_coords(calculated_point[0]) != 3:
        # map.matrix[calculated_point[0][1] - 1][calculated_point[0][0] - 1] \
        #     = calculated_point[1]
        map.update_matrix(calculated_point[0], calculated_point[1])

print()
print()
map.print()

print()
print()

for row in map.matrix:
    print(row)


# map.print()










