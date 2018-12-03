from termcolor import colored
from prettytable import PrettyTable
from graphics import *


class Map:
    def __init__(self, matrix, tile_width, tile_height):
        self.matrix = matrix
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.win = GraphWin("My Screen", 900, 600)

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

    def draw_map(self):
        width = 30
        height = 30
        x, y = 0, 0
        for row in self.matrix:
            for item in row:
                r = Rectangle(Point(x, y), Point(x + width, y + height))
                if item == 'X':
                    r.setFill("black")
                elif item == '_':
                    r.setFill('yellow')
                elif item == 'S':
                    text_x = x + (width / 2)
                    text_y = y + (height / 2)
                    t = Text(Point(text_x, text_y), 'Start')
                    t.draw(self.win)
                elif item == 'F':
                    text_x = x + (width / 2)
                    text_y = y + (height / 2)
                    t = Text(Point(text_x, text_y), 'Finish')
                    t.draw(self.win)
                else:
                    text_x = x + (width / 2)
                    text_y = y + (height / 2)
                    t = Text(Point(text_x, text_y), item)
                    t.draw(self.win)

                r.draw(self.win)
                x = x + width
            x = 0
            y = y + height

        self.draw_path(self.get_start())
        self.win.getMouse()
        self.win.close()

    def draw_path(self, coords):
        finished = False
        adjacent_cells = self.get_adjacent_cells(coords)

        for temp in adjacent_cells.copy():
            try:
                value = self.get_coords(temp)

                if value == 'X' or value == 'S' or self.outofbounds(temp):
                    adjacent_cells.remove(temp)

            except IndexError:
                adjacent_cells.remove(temp)

        values = []
        for cell in adjacent_cells:
            value = self.get_coords(cell)
            if value != 'X' and value != '_':
                if value == 'F':
                    finished = True
                values.append((cell, value))
        print(values)
        if not finished:
            min_value = min(values, key=lambda t: t[1])
            coords = self.get_map_coords(min_value[0][0], min_value[0][1])
            r = Rectangle(Point(coords[0], coords[1]), Point(coords[0] + self.tile_width, coords[1] + self.tile_height))
            r.setFill("green")
            r.draw(self.win)
            self.draw_path(min_value[0])

    def get_map_coords(self, x, y):
        x_point = (x - 1) * self.tile_width
        y_point = (y - 1) * self.tile_height

        return x_point, y_point
