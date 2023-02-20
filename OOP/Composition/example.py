class WinDoor(object):
    def __init__(self, x, y):
        self.square = x*y


class Room(object):
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        new_square = self.square
        for _ in self.wd:
            new_square -= _.square
        return new_square


r1 = Room(5, 6, 7)
print(f'surface square at the beginning: {r1.square}')
r1.add_wd(2, 3)
r1.add_wd(3, 4)
print(f'surface square after subtracting squares of win_door\'s: {r1.work_surface()}')
