import math


def calculate_time(speed, distances) -> int | float:
    time = 0

    for dist in distances:
        time_taken = dist / speed
        time += math.ceil(time_taken)

    return time


def find_best_speed(h: int, distances: list, error: float = 0.0001) -> int | float:
    prev_speed = sum(distances) / h
    speed = prev_speed + 1
    mid = (speed + prev_speed) / 2

    while (speed - prev_speed > error):
        mid = (speed + prev_speed) / 2
        time = calculate_time(mid, distances)
        if time > h:
            prev_speed = mid
        elif time < h:
            speed = mid
        else:
            return mid

    return mid


if __name__ == '__main__':
    res = find_best_speed(3, [1, 2, 3])
    print(res)