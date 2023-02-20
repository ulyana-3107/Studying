# Механизм инкапсуляции
# * attribute (без одного/двух подчеркиваний вначале) - публичное свойство (public)
# * _attribute (с одним подчеркиванием) - режим доступа protected (служит для обращения внутри класса и во всех его до
# черних классах)
# * __attribute (с двумя подчеркиваниями) - режим доступа private (служит для обращения только внутри класса)

# в Python _ (нижнее подчеркивание) лишь сигнализирует о том, что данное свойство является защищенным, но никак явно не
# ограничивает доступ к нему извне -> _ лишь предостерегает программиста от использования данного свойства вне класса.
# _ указывает нам, что это внутренняя служебная переменная.

# методы set_smth, get_smth в ООП называют сеттерами и геттерами а также интерфейсными методами
# чтобы не нарушить целостность алгоритма работы внутри класса следует взаимодействовать с ним только через публичные
# свойства и методы - в этом суть принципа инкапсуляции

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self._y = y

    def set_coord(self, x, y):
        self._y = y
        self.__x = x

p = Point()
p.set_coord(4, 5)
# для проверки свойств, которые существуют в экземпляре класса есть функция dir(obj), мы получим список свойств, где и
# будет находиться кодовое имя для обращения к приватным атрибутам извне, если все-же нужно защитить атрибуты от лишнего
# использования, то это делается с помощью модуля accessify
print(dir(p))
print(p._Point__x)


class SomeClass(object):
    def _private(self):
        print('This is inner method of a class')


# o = SomeClass()
# o._private()


class SomeClass2(object):
    def __init__(self):
        self.__private_element = 9


# o = SomeClass2()
# try:
#     print(o.__private_element)
# except AttributeError:
#     print('methods with double underscore are unaccessible')
#     print(o._SomeClass2__private_element)


# Special access methods can be used too
class SomeClass3(object):
    def __init__(self, elem):
        self.elem = elem

    def setelem(self, new_elem):
        self.elem = new_elem

    def getelem(self):
        return self.elem

    def delelem(self):
        del self.elem

    elem_ = property(getelem, setelem, delelem, 'elem property')


# Вместо того чтобы создавать геттеры и сеттеры вручную для каждого атрибута, можно перегрузить встроенные методы
# __setattr__,__getattr__,__delattr__.Можно перехватить обращение к свойствам/методам, которых в объекте не существует.

class SomeClass4(object):
    attr = 10

    def __getattr__(self, attr):
        return attr.upper()


# o = SomeClass4()
# print(o.attr)
# print(o.not_exists)


# __getattribute__ intercepts all requests, including existing ones (перехватывает даже существующие атрибуты)
class SomeClass5(object):
    attr = 9

    def __getattribute__(self, attr):
        return attr.upper()


# o = SomeClass5()
# print(o.attr, '\t', o.inexisting_one)