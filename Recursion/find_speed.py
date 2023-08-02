def min_speed_rec(h: int, dist: list, curr):
    if len(dist) == 0:
        return 0
    elif h < curr:
        return -1
    else:
        s1 = dist[0] / (curr + 1)
        s2 = min_speed_rec(h, dist[1:], curr + 1)

        if s2 == -1:
            return s1
        else:
            return max(s1, s2)


def find_speed(h: int, dist: list) -> float|int:
    return min_speed_rec(h, dist, 1)


if __name__ == '__main__':
    r1 = find_speed(3, [1, 2, 3])
    r2 = find_speed(5, [1, 2, 3, 4, 5])
    r3 = find_speed(6, [5, 3, 8, 2, 4])
    print(r1, r2, r3, sep='\n')