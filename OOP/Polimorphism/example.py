class Mammal(object):
    def move(self):
        print('I move')


class Hare(Mammal):
    def move(self):
        print('I jump')


# animal1, animal2 = Mammal(), Hare()
# animal1.move()
# animal2.move()


class Parent(object):
    def __init__(self):
        print('Parent init')

    def method(self):
        print('Parent method')


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super(Child, self).method()


# o = Child()
# o.method()


class Russian(object):
    def say_hello(self):
        print('привет')


class English(object):
    def say_hello(self):
        print('hi')


def intro(language):
    language.say_hello()


# person1, person2 = Russian(), English()
# person1.say_hello()
# person2.say_hello()
