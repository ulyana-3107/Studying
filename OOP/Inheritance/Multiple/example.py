#  Множественное наследование, пример: идея миксинов в Python.  Пример: создается магазин по продеже каких либо товаров
# и у каждого товара есть свой класс, все эти товары наследуются от общего класса Goods


class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1)
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        return f'{self.name} {self.weight} {self.price}'


# еще один класс, который работает совершенно независимо от всех остальных классов. Вот такие независимые классы и полу
# чили название миксинов.
class MixinLog:
    ID = 0

    def __init__(self, p1):
        super().__init__(1, 2)
        print('MixinLog initialised.')
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'товар {self.id} продан.')


class MixinLog2:
    ID = 0

    def __init__(self, p2, p3):
        super().__init__()
        print('MixinLog2 initialised.')
        MixinLog2.ID += 1
        self.id = MixinLog2.ID


class SSD(Goods):
    pass


class Notebook(Goods, MixinLog, MixinLog2):
    pass


class CPU(Goods):
    pass


n = Notebook('acer', 1.5, 1000)
print(n.id)
# при создании объекта инициализатор ищется сначала в дочерних классах, а затем в базовых, поэтому инициализатор MixinLo
# g не вызвался, так как достаточно инициализатора из класса Goods (а Goods стоит первым в цепочке наследования). Для
# этого в инициализаторе базового класса создают объект посредник с помощью функции super() который делегирует вызов ини
# циализатора соответствующего базового класса. И для того, чтобы функция super() знала, что нужно обратиться именно к
# инициализатору MixinLog, а не к базовому классу object, в Python существует специальный алгоритм обхода базовых классо
# в MRO (method resolution order). Т.Е. есть 4 класса OBJECT, A, B, C и A,B наследуются от OBJECT, а C наследуется от
# A, B. Получается, что при создании объекта C цепочка поиска инициализатора следующая: C, A, B, OBJECT.  И эту цепочку
# из классов можно вывести в виде списка с помощью Имя класса.переменная __mro__.
# При использовании множественного наследования то структуру классов следует продумывать так, чтобы инициализаторы вспо
# могательных классов, т.е. тех, что наследуются не в первую очередь имели только один параметр self.



# это список классов которые обходятся при поиске того или иного атрибута.
print(Notebook.__mro__)

