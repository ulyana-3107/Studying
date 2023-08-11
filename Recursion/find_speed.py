import math


def calculate_time(speed, distances) -> int | float:
    time = 0

    for dist in distances:
        time_taken = dist / speed
        time += math.ceil(time_taken)

    return time


def find_best_speed(h: int, distances: list, error: float = 0.25) -> int | float:
    speed = sum(distances) / h
    prev_speed = speed - 1

    while True:
        time1, time2 = calculate_time(prev_speed, distances), calculate_time(speed, distances)

        diff = time2 - h

        if diff <= error:
            return speed

        elif time2 > h:
            mid = (speed - prev_speed) / 2
            prev_speed, speed = prev_speed + mid, speed + mid


if __name__ == '__main__':
    res = find_best_speed(3, [1, 2, 3])
    print(res)