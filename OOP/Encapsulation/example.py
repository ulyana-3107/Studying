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