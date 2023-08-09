import sys

import numpy as np
from sys import setrecursionlimit
sys.setrecursionlimit(1000000)


def exists_path_swamp(lst, r):
    if r < 0 or r > lst.shape[0] or lst[r, 0] == 'w':
        return False
    elif lst.shape[1] == 1:
        return True
    else:
        return (exists_path_swamp(lst[:, 1:], r - 1)
                or exists_path_swamp(lst[:, 1:], r)
                or exists_path_swamp(lst[:, 1:], r + 1))


def exists_path_swamp2(lst, r):
    if lst.shape[1] == 1:
        return lst[r, 0] != 'w'
    else:
        if r == 0 or lst[r - 1, 1] == 'w':
            diag_up = False
        else:
            diag_up = exists_path_swamp2(lst[:, 1:], r - 1)

        if not diag_up:
            if r == lst.shape[0] - 1 or lst[r + 1, 1] == 'w':
                diag_down = False
            else:
                diag_down = exists_path_swamp2(lst[:, 1:], r + 1)

            if not diag_down:
                if lst[r, 1] == 'w':
                    horizontal = False
                else:
                    horizontal = exists_path_swamp2(lst[:, 1:], r)

    return diag_up or diag_down or horizontal


def exists_path_swamp3(lst, r, c) -> bool:
    n, m = lst.shape[0], lst.shape[1]

    if lst[r, c] == 'w':
        return False
    elif c == m - 1:
        return lst[r, c] != 'w'
    else:
        return (exists_path_swamp3(lst, r - 1, c + 1)
                or exists_path_swamp3(lst, r, c + 1)
                or exists_path_swamp3(lst, r + 1, c + 1))


def exists_path4(lst, r, c, steps=0) -> int:
    """
    Moving from left to right, you can move vertically and horizontally to the right
    """
    n, m = lst.shape[0], lst.shape[1]

    if r not in range(n) or c not in range(m):
        return -1

    if lst[r, c] == 'w':
        return -1

    elif c == m - 1:

        if lst[r, c] != 'w':
            return steps
    else:
        return (exists_path4(lst, r - 1, c + 1, steps + 1) or
                exists_path4(lst, r, c + 1, steps + 1) or
                exists_path4(lst, r + 1, c + 1, steps + 1) or
                exists_path4(lst, r - 1, c, steps + 1) or
                exists_path4(lst, r + 1, c, steps + 1))

        # results = [exists_path4(lst, r - 1, c + 1, steps + 1),
        #         exists_path4(lst, r, c + 1, steps + 1),
        #         exists_path4(lst, r + 1, c + 1, steps + 1),
        #         exists_path4(lst, r - 1, c, steps + 1),
        #         exists_path4(lst, r + 1, c, steps + 1)]
        #
        # results = [i for i in results if i >= 0]
        #
        # return min(results) if len(results) else -1


if __name__ == '__main__':

    arr = np.array([['w', 'd', 'w', 'w'],
                    ['d', 'd', 'd', 'd'],
                    ['d', 'w', 'd', 'w'],
                    ['w', 'w', 'd', 'w']])

    print(exists_path4(arr, 2, 2))


