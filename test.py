class Fruit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Fruit: {self.name}'


fr = Fruit('banana')
print(fr.__repr__())