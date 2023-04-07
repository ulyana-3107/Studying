# Лесенки - конструкция из кубиков, где каждый следующий уровень состоит из строго большего количества кубиков, чем пред
# ыдущий. Необходимо подсчитать, сколько лесенок можно построить из n кубиков.


def number_of_ladders(n: int, count, prev: int=0, last: int=0):
    if n == last:
        return count
    else:
        if last <= prev:
            return count
        elif last > prev:
            