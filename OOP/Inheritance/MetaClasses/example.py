class MetaClass(type):
    def __new__(cls, name, bases, dict):
        print(f'Creating of new class: {name}')
        return type.__new__(cls, name, bases, dict)

    def __init__(cls, name, bases, dict):
        print(f'Initialization of new class {name}')
        # wth?
        return super(MetaClass, cls).__init__(name, bases, dict)


# Creating of MetaClass
SomeClass = MetaClass('SomeClass', (), {})


# Simple Inheritance
class Child(SomeClass):
    def __init__(self, elem):
        print(elem)


o = Child('Inheritance')


