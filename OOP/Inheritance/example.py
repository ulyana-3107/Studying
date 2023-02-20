# Наследование - один класс определяется на основе другого
# Вызов методов базового класса через функцию super() называется делегированием.


class Geom:
    name = 'Geom'

    # параметр self в базовых классах может ссылаться не только на объекты этого же класса, но и на объекты дочерних
    # классов, в том случае когда метод вызван через объект дочернего класса, все зависит от того, от куда этот метод
    # был вызван

    def set_coords(self, x1, y1, x2, y2):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def draw(self):
        print('drawing of rectangle')


g = Geom()
l = Line()
print(l.name)


# class Horse(object):
#     is_horse = bool(1)
#
#
# class Donkey(object):
#     is_donkey = bool(1)
#
#
# class Mule(Donkey, Horse):
#     is_mule = bool(1)
#
#
# # animal = Mule()
# # print(animal.is_horse, animal.is_donkey)
#
# class Mammal(object):
#     class_name = 'Mammal'
#
#
# class Dog(Mammal):
#     species = 'dog_type1'
#
#
# # doggy = Dog()
# # print(doggy.species, doggy.class_name)
#
# class Table(object):
#     color = 'grey'
#
#
# class Chair(object):
#     size = 'small'
#
#
# class Furniture(Table, Chair):
#     type = 'new'


# f = Furniture()
# print(f.type, f.size, f.color)


