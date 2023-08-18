import math


def calculate_time(speed, distances) -> int | float:
    time = 0

    for dist in distances:
        time_taken = dist / speed
        time += math.ceil(time_taken)

    return time


def find_best_speed(h: int, distances: list, error: float = 0.0001) -> int | float:
    if h - len(distances) < 0:
        return -1

    prev_speed = sum(distances) / h
    speed = sum(distances) / max((h - len(distances)), error)
    mid = (speed + prev_speed) / 2

    while (speed - prev_speed > error):
        mid = (speed + prev_speed) / 2
        time = calculate_time(mid, distances)
        if time > h:
            prev_speed = mid
        elif time < h:
            speed = mid
        else:
            if (speed - prev_speed) <= error:
                return mid
            else:
                speed = mid

    return mid


if __name__ == '__main__':
    res = find_best_speed(3, [1, 2, 3])
    res2 = find_best_speed(7, [1, 1, 1, 1, 1, 15])
    print(res2)