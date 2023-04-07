class Vector:
    # атрибуты класса
    min_coord, max_coord = 0, 100

    # произошла проверка на валидность и если она не пройдена то новые координаты будут равны 0
    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x, self.y = x, y

    # обычный метод
    def get_coords(self):
        return self.x, self.y

    # кроме обычных методов есть статические и методы класса (@classmethod, @staticmethod)
    # @classmethod работает исключительно с методами класса, но не может обращаться к локальным экземплярам класса, так
    # же этот метод можно вызывать через имя класса Vector.validate(3) например.
    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    # с помощью декоратора @staticmethod создаются методы не имеющие доступа ни к атрибутам класса, ни к его экземплярам
    # тоесть создается некая независимая отдельная функция внутри класса (для удобства), она функционально связана с те
    # матикой самого класса

    @staticmethod
    def norm2(x, y):
        return x*x + y*y
    # создали сервисную вспомогательную функцию которая вычисляет квадратичную норму вектора


v = Vector(3, 4)
print(v.norm2(4, 4))

# Итоги:
# обычные методы в классе (тоесть с параметром self) вызываются через экземпляры классов и работают как с ними так и с
# атрибутами самого класса.
# если нужен метод который работает только с атрибутами класса, то его следует определять как метод класса с помощъю
# декоратора @classmethod
# а если нам нужна какая-либо сервисная независимая функция которая работает с параметрами определенными непосредственно
# в ней, то ее следует определить как статическую с помощью декоратора @staticmethod