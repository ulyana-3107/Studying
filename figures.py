"""
Class hierarchy for representing geometric figures.
"""
from accessify import private
import math


class Vector(list):

    """
    Additional class.
    Converts an iterable type to string type.
    Can be used to display a figure.
    """

    def __str__(self):
        return ' '.join(map(str, self))


class Figure(object):
    """
    Abstract class Figure.
    Implements a basic interface for successor classes.
    Methods can be extended, overriden, remain unchanged.
    """

    def __init__(self):
        """
        Constructor.
        Creates boarders along x-axis and y-axis, field for displaying a shape.
        :param self._boarder_x: boarder of x-axis for creating a field.
        :param: self._boarder_y: boarder of y-axis for creating a field.
        :param: self.middle: tuple of 2 elements: (x, y) - coordinates of zero point.
        :param: self._field: list of lists, filled with '.' for displaying geometric figures.
        """
        self._boarder_x = self._boarder_y = 11
        self.middle = self._boarder_x//2, self._boarder_y//2
        self._field = [['.' for i in range(self._boarder_x)] for i in range(self._boarder_y)]
        self._field[self.middle[1]][self.middle[0]] = '0'
        self.coords = []

    def index_to_coord_x(self, index_x: int, middle: int) -> int:
        if index_x > middle:
            return index_x - middle
        elif index_x < middle:
            return -1 * (middle - index_x)
        else:
            return - middle

    def index_to_coord_y(self, index_y: int, middle: int) -> int:
        if index_y == 0:
            return -middle
        elif index_y > middle:
            return - (middle - index_y)
        else:
            return middle - index_y


    def coord_to_index_x(self, coord_x: int, zero: int) -> int:
        if coord_x < 0:
            return zero - abs(coord_x)
        elif coord_x > 0:
            return zero + coord_x
        else:
            return zero

    def coord_to_index_y(self, coord_y: int, zero: int) -> int:
        if coord_y < 0:
            return zero + abs(coord_y)
        elif coord_y > 0:
            return zero - coord_y
        else:
            return zero

    def display_info(self) -> None:
        print(f'Info: \nstr_type: {self.str_type()}\nsquare: {self.square()}\nperimeter: {self.perimeter()}')

    def __str__(self):
        return '\n'.join(''.join([f for f in f_]) for f_ in self._field)

    def __add__(self, other):
        raise Exception('This method should be overriden in child class.')

    def __sub__(self, other):
        raise Exception('This method should be overriden in child class.')

    def __mul__(self, number: int):
        raise Exception('This method should be overriden in child class.')

    def __eq__(self, other):
        raise Exception('This method should be overriden in child class.')

    def __lt__(self, other):
        raise Exception('This method should be overriden in child class.')

    def __gt__(self, other):
        raise Exception('This method should be overriden in child class.')

    def __le__(self, other):
        raise Exception('This method should be overriden in child class.')

    def __ge__(self, other):
        raise Exception('This method should be overriden in child class.')

    def valid(self, *args):
        """
        Checks whether it is possible to create a figure with given parameters.
        :param args: length of figure.
        :return: bool|string: bool in case given params are valid, string in case params are not valid.
        """
        raise Exception('This method should be overriden in child class.')

    def build_figure(self, *args):
        """
        Depending on the figure that will be created, it finds indexes that will be filled in with signs
        for displaying a figure on the field.
        :param args: coordinates for creating a figure object.
        :return: None
        """
        raise Exception('This method should be overriden in child class.')

    def perimeter(self):
        """
        Calculates perimetr of a figure.
        :return: Perimetr of a figure.
        """
        raise Exception('This method should be overriden in child class.')

    def square(self):
        """
        Calculates square of a figure.
        :return: Square of a figure.
        """
        raise Exception('This method should be overriden in child class.')

    def str_type(self):
        """
        Defines the type of the created object.
        :return: type of created object.
        """
        return f'{type(self).__name__}'


class Point(Figure):
    """
    Creates a point object on the field.
    Inherited from the class Figure.
    """
    def __init__(self, x, y, sign='#'):
        super().__init__()
        self.x, self.y = x, y
        self.sign = sign
        self.build_figure()

    def __add__(self, other):
        self.x3 = (self.x + other.x)//2
        self.y3 = (self.y + other.y)//2
        return Point(self.x3, self.y3)

    def __sub__(self, other):
        self.x3 = (self.x + other.x) // 2
        self.y3 = (self.y + other.y) // 2
        return Point(self.x3, self.y3)

    def __mul__(self, number: int):
        self.x3, self.y3 = self.x * number, self.y * number
        return Point(self.x3, self.y3)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other) -> bool:
        return self.x < other.y and self.y < other.y

    def __gt__(self, other) -> bool:
        return self.x > other.x and self.y > other.y

    def __le__(self, other) -> bool:
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other) -> bool:
        return self.x >= other.x and self.y >= other.y

    def valid(self, x: int, y: int) -> tuple:
        x_right, y_right = abs(self.x) <= self.middle[0], abs(self.y) <= self.middle[1]
        res = (x_right, y_right)
        d = {(1, 1): True, (1, 0): 'Y', (0, 1): 'X', (0, 0): 'X and Y'}
        res = d[res]
        if type(res) == bool:
            return res, None
        return False, res

    def build_figure(self):
        validated = self.valid(self.x, self.y)
        if validated[0]:
            x1, y1 = self.middle[0] + self.x, self.middle[1] - self.y
            self._field[y1][x1] = self.sign
        else:
            raise ValueError(f'coordinate {validated[1]} should be changed')

    def perimeter(self) -> int:
        return 0

    def square(self) -> int:
        return 0


# В этой функции обязательно одно из условий:
# 1) X1 == X2
# 2) Y1 == Y2
class Line(Figure):
    """
    Creates a line object on the field.
    Inherited from the class Figure.
    """
    def __init__(self, x1, y1, x2, y2, sign='#'):
        super().__init__()
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.sign, self.coords = sign, []
        self.side_len = self.get_len()
        self.validated = self.valid(self.x1, self.y1, self.x2, self.y2)
        self.build_figure()

    def get_len(self) -> int:
        if self.y1 == self.y2:
            # There are 4 cases:
            if self.x1 < 0 and self.x2 < 0:
                return abs(self.x1) - abs(self.x2)
            elif self.x1 < 0 < self.x2:
                return abs(self.x1) + self.x2
            elif self.x1 + self.x2 == self.x1 or self.x2 + self.x1 == self.x1:
                return abs(self.x1) + abs(self.x2)
            else:
                return self.x2 - self.x1
        else:
            # 4 cases
            if self.y1 < 0 and self.y2 < 0:
                if self.y1 > self.y2:
                    return abs(self.y2) - abs(self.y1)
                else:
                    return abs(self.y1) - abs(self.y2)
            elif self.y1 < 0 < self.y2:
                return self.y2 + abs(self.y1)
            elif self.y1 > 0 and self.y2 > 0:
                return abs(self.y2 - self.y1)
            elif self.y1 + self.y2 == self.y1 or self.y2 + self.y1 == self.y2:
                return abs(self.y1) + abs(self.y2)

    def build_figure(self):
        if not self.validated[0]:
            raise ValueError(f'{self.validated[1]} should be changed.')
        if self.y1 == self.y2:
            x1, x2 = self.coord_to_index_x(self.x1, self.middle[0]), self.coord_to_index_x(self.x2, self.middle[0])
            y = self.coord_to_index_y(self.y1, self.middle[1])
            for x in range(x1, x2 + 1):
                self._field[y][x] = self.sign
                self.coords.append((y, x))
        elif self.x1 == self.x2:
            y1, y2 = self.coord_to_index_y(self.y1, self.middle[1]), self.coord_to_index_y(self.y2, self.middle[1])
            x = self.coord_to_index_x(self.x1, self.middle[0])
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                self._field[y][x] = self.sign
                self.coords.append((y, x))

    def __add__(self, other):
        # Сначала проверка на наличие общей части
        # Случай, когда линии не пересекаются -> возврат первой.
        if set(self.coords).isdisjoint(set(other.coords)) is True:
            return self
        # В обратном случае - индексы объединяются, затем определяется общая координата, затем поиск крайних индексов
        common = self.coords + other.coords
        xy = [common[0][1] == common[1][1], common[0][0] == common[1][0]]
        # если 2 линии пересекаются по оси X -> 1) определяется X, Y1, Y2 - это индексы -> перевод индексов в координаты
        if xy[0]:
            _x, _y1, _y2 = common[0][1], min([t[0] for t in common]), max([t[0] for t in common])
            x = self.index_to_coord_x(_x, self.middle[0])
            y1, y2 = self.index_to_coord_y(_y1, self.middle[1]), self.index_to_coord_y(_y2, self.middle[1])
            return Line(x, y1, x, y2)
        else:
            _y, _x1, _x2 = common[0][0], min([t[1] for t in common]), max([t[1] for t in common])
            y = self.index_to_coord_y(_y, self.middle[1])
            x1, x2 = self.index_to_coord_x(_x1, self.middle[0]), self.index_to_coord_x(_x2, self.middle[0])
            return Line(x1, y, x2, y)

    # Сначала нужно узнать, пересекаются ли линии -> если нет то None, если да то из индексов первой линии убираются те,
    # что есть во второй -> определяется общая координата -> находятся крайние индексы -> переводятся индексы в координа
    # ты -> возврат новой линии.
    def __sub__(self, other):
        # Lines do not cross -> impossible to subtract.
        if set(self.coords).isdisjoint(set(other.coords)) is True:
            return None
        # В обратном случае собираются индексы первой линии при условии что они не во второй
        new_indexes = [xy for xy in self.coords if xy not in other.coords]
        # Затем идет проверка, не точка ли это
        if len(new_indexes) == 1:
            _yx = new_indexes[0]
            y, x = self.index_to_coord_y(_yx[0], self.middle[1]), self.index_to_coord_x(_yx[1], self.middle[0])
            return Point(x, y, self.sign)
        # Затем определяется общая координата, если это не точка
        xy = [new_indexes[0][1] == new_indexes[1][1], new_indexes[0][0] == new_indexes[1][0]]
        if xy[0]:
            x = self.index_to_coord_x(new_indexes[0][1], self.middle[0])
            y1 = self.index_to_coord_y(min([tup[0] for tup in new_indexes]), self.middle[1])
            y2 = self.index_to_coord_y(max([tup[0] for tup in new_indexes]), self.middle[1])
            return Line(x, y1, x, y2)
        else:
            y = self.index_to_coord_y(new_indexes[0][0], self.middle[1])
            x1 = self.index_to_coord_x(min([tup[1] for tup in new_indexes]), self.middle[0])
            x2 = self.index_to_coord_x(max([tup[1] for tup in new_indexes]), self.middle[0])
            return Line(x1, y, x2, y)

    # Сначала определяется общая координата: X/Y, затем, получение новой длины линии, потом исходя из разницы между но
    # вой и старой длиной линии общая координата 1 - сдвигается вниз на (разница)//2, 2- сдвигается вверх на (разн.)//2
    def __mul__(self, number: int):
        new_length = self.side_len * number
        diff = new_length - self.side_len
        xy = [self.x1 == self.x2, self.y1 == self.y2]
        print(f'xy: {xy}, new_length: {new_length, self.side_len}, diff: {diff}')
        if xy[0]:
            y1, y2 = self.y1 - diff//2, self.y2 + diff//2
            x = self.x1
            if abs(y1) + abs(y2) > self._boarder_y:
                return None
            print(x, y1, x, y2)
            return Line(x, y1, x, y2)
        else:
            x1, x2 = self.x1 - diff//2, self.x2 + diff//2
            y = self.y1
            if abs(x1) + abs(x2) > self._boarder_x:
                return None
            return Line(x1, y, x2, y)

    def __eq__(self, other) -> bool:
        return self.side_len == other.side_len

    def __lt__(self, other) -> bool:
        return self.side_len < other.side_len

    def __gt__(self, other) -> bool:
        return self.side_len > other.side_len

    def __le__(self, other) -> bool:
        return self.side_len <= other.side_len

    def __ge__(self, other) -> bool:
        return self.side_len >= other.side_len

    def valid(self, x1, y1, x2, y2) -> tuple:
        xy_right = (abs(x1) <= self.middle[0] and abs(x2) <= self.middle[0],
                    abs(y1) <= self.middle[1] and abs(y2) <= self.middle[1])
        d, d2 = {(1, 1): True, (1, 0): False, (0, 1): False, (0, 0): False}, {0: 'X', 1: 'Y'}
        if d[xy_right]:
            return d[xy_right], None
        string = ' and '.join(d2[i] for i in range(len(xy_right)) if xy_right[i] == 0)
        return d[xy_right], string

    def perimeter(self) -> int:
        return self.side_len + 1

    def square(self) -> int:
        return 0


class Square(Figure):
    def __init__(self, side: int, sign: str = '#'):
        super().__init__()
        self.side, self.sign = side, sign
        self.validated = self.valid(self.side)
        self.build_figure()

    def __add__(self, other):
        new_side_length = (self.side + other.side)//2
        return Square(new_side_length)

    def __sub__(self, other):
        new_side_length = self.side - other.side
        if new_side_length < 1:
            return None
        elif new_side_length == 1:
            return Point(self.middle[0], self.middle[1])
        else:
            return Square(new_side_length)

    def __mul__(self, number: int):
        new_side_length = self.side * number
        if new_side_length > self._boarder_x:
            raise ValueError('Reduce the multiplier.')
        else:
            return Square(new_side_length)

    def __eq__(self, other) -> bool:
        return self.side == other.side

    def __lt__(self, other) -> bool:
        return self.side < other.side

    def __gt__(self, other) -> bool:
        return self.side > other.side

    def __le__(self, other) -> bool:
        return self.side <= other.side

    def __ge__(self, other) -> bool:
        return self.side >= other.side

    def build_figure(self):
        if not self.validated[0]:
            raise ValueError(f'Length of {self.str_type()} side should be reduced.')
        x1, x2 = self.middle[0] - self.side//2, self.middle[0] + self.side//2
        y1, y2 = self.middle[1] - self.side//2, self.middle[1] + self.side//2
        for i in range(y1, y2):
            if i in (y1, y2 - 1):
                for j in range(x1, x2):
                    self._field[i][j] = self.sign
            else:
                self._field[i][x1], self._field[i][x2 - 1] = self.sign, self.sign

    def valid(self, side_length) -> tuple:
        bool_ = side_length <= self._boarder_x and side_length <= self._boarder_y
        return bool_, None

    def perimeter(self) -> int:
        return self.side * 4

    def square(self) -> int:
        return self.side * self.side


class Rectangle(Figure):
    def __init__(self, side1, side2, sign: str = '#'):
        super().__init__()
        self.side1, self.side2, self.sign = side1, side2, sign
        self.validated = self.valid(self.side1, self.side2)
        self.build_figure()

    def __add__(self, other):
        new_side1 = (self.side1 + self.side1) // 2
        new_side2 = (self.side2 + other.side2) // 2
        # Это бесполезно но не нужно удалять.
        # if new_side1 > self._boarder_x:
        #     first, second = self.side1 >= other.side1, other.side1 > self.side1
        #     res = 'first' if first else 'second'
        #     raise ValueError('Reduce length of {} {}'.format(res, self.str_type()))
        # if new_side2 > self._boarder_y:
        #     first, second = self.side2 >= other.side2, other.side2 > self.side2
        #     res = 'first' if first else 'second'
        #     raise ValueError('Reduce width of {} {}'.format(res, self.str_type()))
        return Rectangle(new_side1, new_side2)

    def __sub__(self, other):
        new_side1 = self.side1 - other.side1
        new_side2 = self.side2 - other.side2
        if new_side1 < 1 or new_side2 < 1:
            return None
        # Это случай, когда выходит линия 90 гр -> нужно просто узнать длину линии а потом координаты Y1 Y2, X == 0
        if new_side1 == 1 and new_side2 > 1:
            y1, y2, x = -(new_side2//2), new_side2//2, 0
            return Line(x, y1, x, y2)
        # Точка.
        elif new_side1 == 1 and new_side2 == 1:
            return Point(0, 0)
        elif new_side1 > 1 and new_side2 == 1:
            # Линия 180 гр -> длина это new_side1, находятся координаты x1,2, Y == 0.
            x1, x2, y = -(new_side1//2), new_side1//2, 0
            return Line(x2, y, x2, y)
        else:
            # Возвращается прямоугольник с уменьшенными сторонами
            return Rectangle(new_side1, new_side2)

    def __mul__(self, number: int):
        new_side1, new_side2 = self.side1 * number, self.side2 * number
        if new_side1 > self._boarder_x:
            raise ValueError('Reduce the multiplier.')
        if new_side2 > self._boarder_y:
            raise ValueError('Reduce the multiplier.')
        return Rectangle(new_side1, new_side2)

    def __eq__(self, other) -> bool:
        return self.square() == other.square()

    def __lt__(self, other) -> bool:
        return self.square() < other.square()

    def __gt__(self, other) -> bool:
        return self.square() > other.square()

    def __le__(self, other) -> bool:
        return self.square() <= other.square()

    def __ge__(self, other) -> bool:
        return self.square() >= other.square()

    def valid(self, side1, side2) -> tuple:
        res = (side1 <= self._boarder_x, side2 <= self._boarder_y)
        d, d2 = {(1, 1): True, (1, 0): False, (0, 1): False, (0, 0): False}, {0: 'length', 1: 'width'}
        arr_res = [i for i in range(len(res)) if res[i] == 0]
        if len(arr_res):
            string = ' and '.join([d2[ind] for ind in arr_res])
            return d[res], string.capitalize()
        else:
            return d[res], None

    def build_figure(self):
        if not self.validated[0]:
            raise ValueError(f'{self.validated[1]} should be reduced.')
        else:
            x1, x2 = self.middle[0] - self.side1//2, self.middle[0] + self.side1//2
            y1, y2 = self.middle[1] - self.side2//2, self.middle[1] + self.side2//2
            for i in range(y1, y2):
                if i in (y1, y2 - 1):
                    for j in range(x1, x2):
                        self._field[i][j] = self.sign
                        self.coords.append((i, j))
                else:
                    self._field[i][x1], self._field[i][x2 - 1] = self.sign, self.sign

    def perimeter(self):
        return (self.side1 + self.side2) * 2

    def square(self):
        return self.side1 * self.side2


# side1, side2, side3 - это левая, правая сторона и нижняя часть(всегда берется в качестве основания -> поэтому площадь
# высчитывается с помощью height, side3).
class Triangle(Figure):
    def __init__(self, side1, side2, side3, height, sign='#'):
        super().__init__()
        self.side1, self.side2, self.side3, self.height = side1, side2, side3, height
        self.sign = sign
        self.validated = self.valid(self.height, self.side3)
        self.build_figure()

    def __add__(self, other):
        new_s1, new_s2 = (self.side1 + other.side1)//2, (self.side2 + other.side2)//2
        new_s3, new_h = (self.side3 + other.side3)//2, (self.height + other.height)//2
        return Triangle(new_s1, new_s2, new_s3, new_h, self.sign)

    def __sub__(self, other):
        new_s1, new_s2 = self.side1 - other.side1, self.height - other.height
        new_s3, new_h = self.side3 - other.side3, self.height - other.height
        if new_s1 + new_s2 + new_s3 + new_h < 4:
            return None
        else:
            return Triangle(new_s1, new_s2, new_s3, new_h, self.sign)

    def __mul__(self, number: int):
        new_s1, new_s2 = self.side1 * number, self.side2 * number
        new_s3, new_h = self.side3 * number, self.height * number
        return Triangle(new_s1, new_s2, new_s2, new_h, self.sign)

    def __eq__(self, other) -> bool:
        arr = [self.side1 == other.side1, self.side2 == other.side2,
               self.side3 == other.side3, self.height == other.height]
        return all(arr)

    def __lt__(self, other) -> bool:
        return self.perimeter() < other.perimeter()

    def __gt__(self, other) -> bool:
        return self.perimeter() > other.perimeter()

    def __le__(self, other) -> bool:
        return self.perimeter() <= other.perimeter()

    def __ge__(self, other) -> bool:
        return self.perimeter() >= other.perimeter()

    def valid(self, height, side3) -> tuple:
        res = (self.height <= self._boarder_y, self.side3 <= self._boarder_x)
        d, d2 = {(1, 1): True, (1, 0): False, (0, 1): False, (0, 0): False}, {0: 'height', 1: 'base'}
        if d[res] is True:
            return d[res], None
        else:
            string = ' and '.join([d2[i] for i in range(len(res)) if res[i] == 0])
            return d[res], string.capitalize()

    def build_figure(self):
        if not self.validated[0]:
            raise ValueError(f'{self.validated[1]} should be reduced.')
        x1, x2 = self.middle[0] - self.side3//2, self.middle[0] + self.side3//2
        y1, y2 = self.middle[1] - self.height//2, self.middle[1] + self.height//2
        for i in range(x1 - 1, x2 + 2):
            self._field[y2][i] = self.sign
        if self.side1 == self.side2:
            apex_x = self.middle[0]
        elif self.side1 > self.side2:
            apex_x = self.middle[0] + (self.side1 - self.side2)
        else:
            apex_x = self.middle[0] - (self.side2 - self.side1)
        for i in range(self.side1):
            self._field[y1 + i][apex_x - i] = self.sign
        for i in range(self.side2):
            self._field[y1 + i][apex_x + i] = self.sign

    def perimeter(self) -> int:
        return self.side1 + self.side2 + self.side3

    def square(self) -> int:
        return self.height * self.side3


class Circle(Figure):
    def __init__(self, radius, sign='#'):
        super().__init__()
        self.rad = radius
        self.validated = self.valid(self.rad)
        self.sign = sign
        self.build_figure()

    def __add__(self, other):
        return Circle((self.rad + other.rad)//2)

    def __sub__(self, other):
        if self.rad - other.rad < 1:
            return None
        else:
            return Circle(self.rad - other.rad)

    def __mul__(self, number: int):
        return Circle(self.rad * number)

    def __eq__(self, other) -> bool:
        return self.rad == other.rad

    def __lt__(self, other) -> bool:
        return self.rad < other.rad

    def __gt__(self, other) -> bool:
        return self.rad > other.rad

    def __le__(self, other) -> bool:
        return self.rad <= other.rad

    def __ge__(self, other) -> bool:
        return self.rad >= other.rad

    def valid(self, radius) -> tuple:
        bool_ = radius <= self._boarder_x and radius <= self._boarder_y
        if bool_:
            return bool_, None
        else:
            return bool_, 'Radius'

    def build_figure(self):
        if not self.validated[0]:
            raise ValueError(f'{self.validated[1]} should be reduced.')
        x1, x2 = self.middle[0] - self.rad + 1, self.middle[0] + self.rad - 1
        x3 = x4 = self.middle[0]
        x5, x6 = self.middle[0] - self.rad//2, self.middle[0] + self.rad//2
        y1, y2, y3 = self.middle[1] - self.rad + 1, self.middle[1] - self.rad//2, self.middle[1]
        y4, y5 = self.middle[1] + self.rad//2, self.middle[1] + self.rad - 1
        self._field[y1][x3], self._field[y5][x4] = self.sign, self.sign
        self._field[y2][x5], self._field[y2][x6] = self.sign, self.sign
        self._field[y3][x1], self._field[y3][x2] = self.sign, self.sign
        self._field[y4][x5], self._field[y4][x6] = self.sign, self.sign

    def perimeter(self):
        return int(2 * math.pi * self.rad)

    def square(self):
        return int(math.pi * (self.rad * self.rad))


class Ellipse(Figure):
    def __init__(self, axis1, axis2, sign='#'):
        super().__init__()
        self.axis1, self.axis2, self.sign = axis1, axis2, sign
        self.validated = self.valid(self.axis1, self.axis2)
        self.build_figure()

    def valid(self, axis1, axis2) -> tuple:
        res = (self.axis1 <= self._boarder_x,  self.axis2 <= self._boarder_y)
        d, d2 = {(1, 1): True, (1, 0): False, (0, 1): False, (0, 0): False}, {0: 'width', 1: 'height'}
        if d[res]:
            return d[res], None
        string = ' and '.join(d2[i] for i in range(len(res)) if res[i] == 0)
        return d[res], string.capitalize()

    def build_figure(self):
        if not self.validated[0]:
            raise ValueError(f'{self.validated[1]} should be reduced.')
        y1, y5 = self.middle[1] - self.axis2//2, self.middle[1] + self.axis2//2
        y2, y4 = self.middle[1] - self.axis2//4, self.middle[1] + self.axis2//4
        y3 = self.middle[1]
        x1 = x2 = self.middle[0]
        x3, x4 = self.middle[0] - self.axis1//2, self.middle[0] + self.axis1//2
        x5, x6 = self.middle[0] - self.axis1//4, self.middle[0] + self.axis1//4
        self._field[y1][x1], self._field[y5][x2] = self.sign, self.sign
        self._field[y3][x3], self._field[y3][x4] = self.sign, self.sign
        self._field[y2][x5], self._field[y2][x6] = self.sign, self.sign
        self._field[y4][x5], self._field[y4][x6] = self.sign, self.sign
        self._field[y3][x3], self._field[y3][x4] = self.sign, self.sign

    def __add__(self, other):
        new_ax1, new_ax2 = (self.axis1 + other.axis1)//2, (self.axis2 + other.axis2)//2
        return Ellipse(new_ax1, new_ax2, self.sign)

    def __sub__(self, other):
        new_ax1, new_ax2 = self.axis1 - other.axis1, self.axis2 - other.axis2
        if new_ax1 + new_ax2 < 2:
            return None
        return Ellipse(new_ax1, new_ax2, self.sign)

    def __mul__(self, number: int):
        new_ax1, new_ax2 = self.axis1 * number, self.axis2 * number
        return Ellipse(new_ax1, new_ax2)

    def __eq__(self, other) -> bool:
        res = [self.axis1 == other.axis1, self.axis2 == other.axis2]
        return all(res)

    def __lt__(self, other) -> bool:
        return self.perimeter() < other.perimeter()

    def __gt__(self, other) -> bool:
        return self.perimeter() > other.perimeter()

    def __le__(self, other) -> bool:
        return self.perimeter() <= other.perimeter()

    def __ge__(self, other) -> bool:
        return self.perimeter() >= other.perimeter()

    def perimeter(self):
        return int(math.pi * math.sqrt((self.axis1 * 2 + self.axis2 * 2)//8))

    def square(self):
        return int(math.pi * self.axis1//2 * self.axis2//2)

# objects = [Point(4, 4), Line(-3, 4, -3, 1), Square(4), Rectangle(9, 4), Triangle(5, 5, 5, 5), Circle(6),
# Ellipse(8, 4)]
# for obj in objects:
#     print(obj)
#     obj.display_info()
#     print('\n\n')
