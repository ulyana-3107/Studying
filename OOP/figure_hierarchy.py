# TODO: accessify method install -> use!
# TODO 2: use max methods such as set_value, get_value, validate, new, setattr, getattr, __ and _, @classmethod, @static
# TODO 2: method


from typing import Any
import math


class Figure(object):
    def __init__(self, str_type: str, x: int, y: int, z: int, h: int, r: int, flags=None):
        self.name = str_type
        self.side1, self.side2, self.side3 = x, y, z
        self.height, self.radius, self.flags = h, r, flags

    def calc_perimetr(self):
        pass

    def calc_square(self):
        pass


class Point(Figure):

    def calc_perimetr(self):
        return f'object {type(self).__name__} has no measurable characteristics, except for the coordinates'

    def calc_square(self):
        return f'object {type(self).__name__} has no measurable characteristics, except for the coordinates'


class Line(Point):
    def show(self):
        return '.'*self.side1

    def calc_perimetr(self):
        return f'object {type(self).__name__} has no perimetr.'

    def calc_square(self):
        return f'object {type(self).__name__} has no square.'


class Triangle(Point):
    def calc_perimetr(self):
        if self.flags.lower() == 'equilateral':
            return self.side1 * 3
        elif self.flags.lower() == 'isosceles':
            return self.side1 + self.side2 * 2
        else:
            return self.side1 + self.side2 + self.side3

    def calc_square(self):
        if self.flags.lower() == 'equilateral':
            square3, a2 = math.sqrt(3), self.side1 ** 2
            numerator, denumerator = square3 * a2, 4
            return numerator//denumerator
        else:
            return 0.5 * self.side2 * self.height

    def show(self):
        pass


class Rectangle(Point):
    def calc_perimetr(self):
        return 2 * (self.side1 + self.side2)

    def calc_square(self):
        return self.side1 * self.side2

    def show(self):
        pass


class Square(Point):
    def calc_perimetr(self):
        return self.side1 * 4

    def calc_square(self):
        return self.side1 ** 2

    def show(self):
        pass


class Circle(Point):
    def calc_perimetr(self):
        return math.pi * 2 * self.radius

    def calc_square(self):
        return (self.radius ** 2) * math.pi

    def show(self):
        pass


class Ellipse(Point):
    def calc_perimetr(self):
        pass

    def calc_square(self):
        return math.pi * self.side1 * self.side2

    def show(self):
        pass


# class Point():
#     def __init__(self, x, y, z, r):
#         self.first_side_len = x
#         self.second_side_len = y
#         self.third_side_len = z
#         self.radius = r
#
#     def calc_perimetr(self):
#         return f'object {type(self).__name__} has no measurable characteristics, except for the coordinates.'
#
#     def calc_square(self):
#         return f'object {type(self).__name__} has no measurable characteristics, except for the coordinates.'
#
#     def show_params(self):
#         pass
#
#
# class Line(Point):
#     def calc_perimetr(self):
#         return f'object {type(self).__name__} has only length : {self.first_side_len}'
#
#     def calc_square(self):
#         return f'object {type(self).__name__} has only length : {self.first_side_len}'
#
#     # def get_first_line(self):
#     #     return self.first_side_len
#     #
#     # def get_second_line(self):
#     #     return self.second_side_len
#     #
#     # def get_third_line(self):
#     #     return self.third_side_len
#
#
# class Triangle(Point):
#
#
#
#
#
#
#
# def fabric(name: str, x, y, z, r):
#     obj = eval(name.capitalize())(x, y, z, r)
#     return obj
#
#
# fabric('point', 1, 1, 1, 1)