class Horse(object):
    is_horse = bool(1)


class Donkey(object):
    is_donkey = bool(1)


class Mule(Donkey, Horse):
    is_mule = bool(1)


# animal = Mule()
# print(animal.is_horse, animal.is_donkey)

class Mammal(object):
    class_name = 'Mammal'


class Dog(Mammal):
    species = 'dog_type1'


# doggy = Dog()
# print(doggy.species, doggy.class_name)


