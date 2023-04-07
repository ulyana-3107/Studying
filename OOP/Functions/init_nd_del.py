# В каждом классе языка Python есть магические методы, они начинаются и заканчиваются 2мя подчеркиваниями
class Point:
    # данный магический метод (инициализатор) вызывается автоматически при создании объекта данного класса
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    # данный магический метод (финализатор) вызывается автоматически при удалении экземпляров класса, интерпретатор Pyth
    # on имеет сборщик мусора - это алгоритм, который отслеживает объект на необходимость, и как только тот или иной
    # объект перестает быть нужным - сборшик удаляет объект через функцию __del__. 
    def __del__(self):
        print(f'удаление объекта : {str(self)}')


p = Point(3, 3)
print(f'coordinates: {p.x, p.y}')
del p