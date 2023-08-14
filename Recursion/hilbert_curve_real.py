import matplotlib.pyplot as plt


def get_end(x, y, length: int, direction: str ='right') -> tuple:
    if direction == 'right':
        x1, y1 = x + length, y
    elif direction == 'up':
        x1, y1 = x, y + length
    elif direction == 'left':
        x1, y1 = x - length, y
    else:
        x1, y1 = x, y - length

    return x1, y1


def change_coords(coords, location: str=None, position = 1):
    line = coords.pop()
    x, y = line[0], line[1]
    x0, x1 = x
    y0, y1 = y

    if location == 'down':
        if position == 2:
            new_size = (x1 - x0) / 3
            l1 = ([x0, x0 + new_size], [y0, y1])
            coords.append(l1)
            # change_coords(coords, location='down', position=2)
            l2 = ([x1 - new_size, x1], [y0, y1])
            coords.append(l2)
            # change_coords(coords, location='down', position=2)
            l3 = ([x0 + new_size, x0 + new_size], [y0, y0 + new_size])
            coords.append(l3)
            # change_coords(coords, location='right', position=3)
            l4 = ([x1 - new_size, x1 - new_size], [y0, y0 + new_size])
            coords.append(l4)
            # change_coords(coords, location='left', position=3)
            l5 = ([x0 + new_size, x1 - new_size], [y0 + new_size, y0 + new_size])
            coords.append(l5)
            change_coords(coords, 'down', position=4)
        elif position == 4:
            new_size = (x1 - x0) / 3
            l1 = ([x0, x0 + new_size], [y0, y0])
            coords.append(l1)
            # change_coords(coords, location='down', position=4)
            l2 = ([x1 - new_size, x1], [y0, y0])
            coords.append(l2)
            # change_coords(coords, location='down', position=4)
            l3 = ([x0 + new_size, x1 - new_size], [y0 - new_size, y0 - new_size])
            coords.append(l3)
            # change_coords(coords, location='down', position=2)
            l4 = ([x0 + new_size, x0 + new_size], [y0, y0 - new_size])
            coords.append(l4)
            # change_coords(coords, location='left', position=1)
            l5 = ([x1 - new_size, x1 - new_size], [y0, y0 - new_size])
            coords.append(l5)
            # change_coords(coords, location='right', position=3)
        elif position == 1:
            new_size = (y0 - y1) / 3
            l1 = ([x0, x0], [y0, y0 - new_size])
            coords.append(l1)
            # change_coords(coords, location='down', position=1)
            l2 = ([x0, x0 + new_size], [y0 - new_size, y0 - new_size])
            coords.append(l2)
            # change_coords(coords, location='right', position=4)
            l3 = ([x0 + new_size, x0 + new_size], [y0 - new_size, y1 + new_size])
            coords.append(l3)
            # change_coords(coords, location='down', position=3)
            l4 = ([x0, x0 + new_size], [y1 + new_size, y1 + new_size])
            coords.append(l4)
            # change_coords(coords, location='left', position=2)
            l5 = ([x0, x0], [y1 + new_size, y1])
            coords.append(l5)
            # change_coords(coords, location='down', position=1)
        elif position == 3:
            new_size = (y0 - y1) / 3
            l1 = ([x0, x0], [y0,  y0 - new_size])
            coords.append(l1)
            # change_coords(coords, location='down', position=3)
            l2 = ([x0 - new_size, x0], [y0 - new_size, y0 - new_size])
            coords.append(l2)
            # change_coords(coords, location='left', position=4)
            l3 = ([x0 - new_size, x0 - new_size], [y0 - new_size, y1 + new_size])
            coords.append(l3)
            # change_coords(coords, location='down', position=1)
            l4 = ([x0 - new_size, x0], [y1 + new_size, y1 + new_size])
            coords.append(l4)
            # change_coords(coords, location='right', position=2)
            l5 = ([x0, x0], [y1 + new_size, y1])
            coords.append(l5)
            # change_coords(coords, location='down', position=3)

    elif location == 'left':
        if position == 1:
            new_size = (y0 - y1) / 3
            l1 = ([x0, x0 + new_size], [y0, y0])
            coords.append(l1)
            # change_coords(coords, location='right', position=4)
            l2 = ([x0 + new_size, x0 + new_size], [y0, y0 - new_size])
            coords.append(l2)
            # change_coords(coords, location='down', position=3)
            l3 = ([x0, x0 + new_size], [y0 - new_size, y0 - new_size])
            coords.append(l3)
            # change_coords(coords, location='left', position=2)
            l4 = ([x0, x0], [y0 - new_size, y1 + new_size])
            coords.append(l4)
            l5 = ([x0, x0], [y1 + new_size, y1])
            coords.append(l5)
            # change_coords(coords, location='left', position=1)
        elif position == 4:
            new_size = (x1 - x0) / 3
            l1 = ([x1, x1], [y1, y1 - new_size])
            coords.append(l1)
            # change_coords(coords, location='right', position=3)
            l2 = ([x1 - new_size, x1], [y1 - new_size, y1 - new_size])
            coords.append(l2)
            # change_coords(coords, location='down', position=2)
            l3 = ([x1 - new_size, x1 - new_size], [y1, y1 - new_size])
            coords.append(l3)
            # change_coords(coords, location='left', position=1)
            l4 = ([x1 - new_size, x0 + new_size], [y1, y1])
            coords.append(l4)
            l5 = ([x0 + new_size, x0], [y1, y1])
            coords.append(l5)
            # change_coords(coords, location='left', position=4)
        elif position == 3:
            new_size = (y0 - y1) / 3
            l1 = ([x0 - new_size, x0], [y1, y1])
            coords.append(l1)
            # change_coords(coords, location='right', position=2)
            l2 = ([x0 - new_size, x0 - new_size], [y1 + new_size, y1])
            coords.append(l2)
            # change_coords(coords, location='down', position=1)
            l3 = ([x0 - new_size, x0], [y1 + new_size, y1 + new_size])
            coords.append(l3)
            # change_coords(coords, location='left', position=4)
            l4 = ([x0, x0], [y0 - new_size, y1 + new_size])
            coords.append(l4)
            l5 = ([x0, x0], [y0, y0 - new_size])
            coords.append(l5)
            # change_coords(coords, location='left', position=3)
        elif position == 2:
            new_size = (x1 - x0) / 3
            l1 = ([x0, x0], [y0 + new_size, y0])
            coords.append(l1)
            # change_coords(coords, location='right', position=1)
            l2 = ([x0 + new_size, x0], [y0 + new_size, y0 + new_size])
            coords.append(l2)
            # change_coords(coords, location='down', position=4)
            l3 = ([x0 + new_size,  x0 + new_size], [y0 + new_size, y0])
            coords.append(l3)
            # change_coords(coords, location='left', position=3)
            l4 = ([x1 - new_size, x0 + new_size], [y0, y0])
            coords.append(l4)
            l5 = ([x1, x1 - new_size], [y0, y0])
            coords.append(l5)
            # change_coords(coords, location='left', position=2)

    elif location == 'right':
        if position == 3:
            new_size = (y0 - y1) / 3
            l1 = ([x0 - new_size, x0], [y0, y0])
            coords.append(l1)
            # change_coords(coords, location='left', position=4)
            l2 = ([x0 - new_size, x0 - new_size], [y0, y0 - new_size])
            coords.append(l2)
            change_coords(coords, location='down', position=1)
            l3 = ([x0 - new_size, x0], [y0 - new_size, y0 - new_size])
            coords.append(l3)
            # change_coords(coords, location='right', position=2)
            l4 = ([x0, x0], [y0 - new_size, y1 + new_size])
            coords.append(l4)
            l5 = ([x0, x0], [y1 + new_size, y1])
            coords.append(l5)
            # change_coords(coords, location='right', position=3)
        elif position == 2:
            new_size = (x0 - x1) / 3
            l1 = ([x0, x0], [y0 + new_size, y0])
            coords.append(l1)
            # change_coords(coords, location='left', position=3)
            l2 = ([x0, x0 - new_size], [y0 + new_size, y0 + new_size])
            coords.append(l2)
            # change_coords(coords, location='down', position=4)
            l3 = ([x0 - new_size, x0 - new_size], [y0 + new_size, y0])
            coords.append(l3)
            # change_coords(coords, location='right', position=1)
            l4 = ([x0 - new_size, x1 + new_size], [y0, y0])
            coords.append(l4)
            l5 = ([x1 + new_size, x1], [y0, y0])
            coords.append(l5)
            # change_coords(coords, location='right', position=2)
        elif position == 4:
            new_size = (x0 - x1) / 3
            l1 = ([x1, x1], [y1, y1 - new_size])
            coords.append(l1)
            # change_coords(coords, location='left', position=1)
            l2 = ([x1 + new_size, x1], [y1 - new_size, y1 - new_size])
            coords.append(l2)
            # change_coords(coords, location='down', position=2)
            l3 = ([x1 + new_size, x1 + new_size], [y0, y0 - new_size])
            coords.append(l3)
            # change_coords(coords, location='right', position=3)
            l4 = ([x0 - new_size, x1 + new_size], [y0, y0])
            coords.append(l4)
            l5 = ([x0, x0 - new_size], [y0, y0])
            coords.append(l5)
            # change_coords(coords, location='right', position=4)
        elif position == 1:
            new_size = (y0 - y1) / 3
            l1 = ([x1 + new_size, x1], [y1, y1])
            coords.append(l1)
            # change_coords(coords, location='left', position=2)
            l2 = ([x1 + new_size, x1 + new_size], [y1 + new_size, y1])
            coords.append(l2)
            # change_coords(coords, location='down', position=3)
            l3 = ([x1 + new_size, x1], [y1 + new_size, y1])
            coords.append(l3)
            # change_coords(coords, location='right',  position=4)
            l4 = ([x1, x1], [y0 - new_size, y1 + new_size])
            coords.append(l4)
            l5 = ([x1, x1], [y0,  y0 - new_size])
            coords.append(l5)
            # change_coords(coords, location='right', position=1)


def draw(x: int, y: int, depth: int, length: int | float):
    fig, ax = plt.subplots()
    coords = []

    x1, y1 = get_end(x, y, length)
    print(x, x1)
    coords.append(([x, x1], [y, y1]))
    change_coords(coords, location='down', position=2)

    x2, y2 = get_end(x, y, length, 'up')
    coords.append(([x2, x], [y2, y]))
    change_coords(coords, location='left', position=1)

    x3, y3 = get_end(x1, y1, length, 'up')
    coords.append(([x3, x1], [y3, y1]))
    change_coords(coords, location='right', position=3)

    for arr in coords:
        x, y = arr
        ax.plot(x, y, color='green')

    plt.show()


draw(1, 1, 3, 3)
# Note! coordinates of single lines are being added from up to down, left to right not to get confused calculating new size