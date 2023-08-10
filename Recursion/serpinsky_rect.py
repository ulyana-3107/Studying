from matplotlib.patches import Polygon
import matplotlib.pyplot as plt


def make_triangles(p1, size):
    x, y = p1[0], p1[1]
    height = size * (3 ** 0.5) / 2
    p2 = (x + size, y)
    p3 = (x + (size / 2), y + height)

    triangle = Polygon([p1, p2, p3], closed=True, fill=None)

    size2 = size / 2
    height2 = size2 * (3 ** 0.5) / 2

    r1_p1 = (x, y)
    r1_p2 = (x + size2, y)
    r1_p3 = (x + (size2 / 2), y + height2)
    triangle1 = Polygon([r1_p1, r1_p2, r1_p3], closed=True, fill=None)

    r2_p1 = (x + (size / 4), y + height2)
    r2_p2 = ((size / 4) * 3, y + height2)
    r2_p3 = (x + (size / 2), y + height2)
    triangle2 = Polygon([r2_p1, r2_p2, r2_p3], closed=True, fill=None)

    r3_p1 = (x + size / 2, y)
    r3_p2 = (x + size, y)
    r3_p3 = (x + (size / 4) * 3, y + height2)
    triangle3 = Polygon([r3_p1, r3_p2, r3_p3], closed=True, fill=None)

    return triangle, triangle1, triangle2, triangle3, size2, r1_p1, r2_p1, r3_p1


def rec_solution(n: int, p1: tuple, size: int, done_num: int, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    if n == 0:
        done_num += 1
    else:
        n -= 1
        tr = make_triangles(p1, size)
        t1, t2, t3, t4 = tr[0], tr[1], tr[2], tr[3]
        for i in range(1, 5):
            ax.add_patch(eval(f't{str(i)}'))

        size2 = tr[4]
        r1_p1, r2_p1, r3_p1 = tr[5], tr[6], tr[7]
        for i in range(1, 4):
            rec_solution(n, eval(f'r{str(i)}_p1'), size2, done_num, ax)
    plt.show()


if __name__ == '__main__':
    rec_solution(4, (0, 0), 1, 0)


