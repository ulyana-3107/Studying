def ropes(coords: list, n) -> int:  # N - length of nails
    """
    defines minimum possible length of ropes needed to link all nails
    :param coords: list with digits, where each digit - coordinate, coord(i - 1) < coord(i) < coord(i + 1), i - index
    :param n: number of nails
    :return: minimum rope length
    """
    # dictionary, key - name of nail(digit), value - the coordinate of the nail
    nail_coord = {i + 1: coords[i] for i in range(n)}  # O(N)
    # list with booleans, False - nail has no rope attached, True - on the contrary
    nails_with_rope = [False for _ in range(n)]  # O(N)
    # list with names of nails which have no rope attached(free), rate - current length of rope used
    nails_free, rate = [i for i in range(1, n + 1)], 0  # O(N)
    while not all(nails_with_rope):  # O(N//2) -> O(N)
        nail = nails_free[0]
        nails_free.remove(nail)  # O(1) так как всегда из свободных берется крайний
        # if nail has both left and right neighbour
        if nail in range(2, n):
            # length of the rope needed to use left nail/right nail
            len1, len2 = nail_coord[nail] - nail_coord[nail - 1], nail_coord[nail + 1] - nail_coord[nail]
            a, b, c_ = len1 < len2, len2 < len1, len1 == len2
            if a:
                c, d, nail_ = nail - 1, nail - 2, nail - 1
                rate += len1
            else:
                c, d, nail_ = nail - 1, nail, nail + 1
                rate += len2
            if nail_ in nails_free:  # O(2) -> O(1) - так как nail_ - это всегда сосед и при проверке на вхождение (перебор)
                # нужный элемент будет максимум на 2м месте.
                nails_free.remove(nail_)  # O(2) -> O(1) - тоже самое - максимум 2й по счету элемент
            nails_with_rope[c], nails_with_rope[d] = True, True
        else:
            # if nail has only left/right nail neighbour
            if nail == 1:
                rate += (nail_coord[nail + 1] - nail_coord[nail])
                a, b = nail, nail - 1
                nail_ = nail + 1
            else:
                rate += (nail_coord[nail] - nail_coord[nail - 1])
                a, b = nail - 1, nail - 2
                nail_ = nail - 1
            nails_with_rope[a], nails_with_rope[b] = True, True
            if nail_ in nails_free:  # O(2) -> O(1)
                nails_free.remove(nail_)  # O(2) -> O(1)
    return round(rate, 2)
# O(N).


axis1 = [11, 12, 13, 16, 17]
axis2 = [6.34, 6.82, 15.89, 24.58]
axis3 = [11, 12, 14, 16, 18]
print(ropes(axis3, len(axis3)))








