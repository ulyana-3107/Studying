# Полиморфизм - возможность работать с разными объектами единым образом, т.е. через единый интерфейс.


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


class Shark(object):
    def swim(self):
        print('The Shark is swimming')

    def swim_backwards(self):
        print('The Shark can not swim backwards!')

    def skeleton(self):
        print('The Shark\'s skeleton is made of cartilage')


class Clownfish(object):
    def swim(self):
        print('The clownfish is swimming')

    def swim_backwards(self):
        print('The clownfish can swim backwards')

    def skeleton(self):
        print('The clownfish\'s skeleton is made of bones')


# wally, casey = Shark(), Clownfish()
# for fish in (wally, casey):
#     fish.swim(), fish.swim_backwards(), fish.skeleton()
#     print('~'*30)


def in_the_pacific(fish):
    fish.swim(), fish.swim_backwards(), fish.skeleton()
    print('~'*30)


# fish1, fish2 = Shark(), Clownfish()
# in_the_pacific(fish1)
# in_the_pacific(fish2)


