import math


def calculate_time(speed, distances) -> int | float:
    time = 0

    for dist in distances:
        time_taken = dist / speed
        time += math.ceil(time_taken)

    return time


def optimal_speed(s1, s2, h, dist):
    plus = (s2 - s1) / 2
    time = calculate_time((s2 + plus) / 2, dist)

    return time > h


def find_best_speed(h: int, distances: list) -> int | float:
    speed = sum(distances) / h
    prev_speed = speed - 1

    while True:
        time1, time2 = calculate_time(prev_speed, distances), calculate_time(speed, distances)

        if time2 == h:
            return speed

        elif time1 > h and time2 < h:
            if optimal_speed(prev_speed, speed, h, distances):
                return speed

            else:
                plus = (speed - prev_speed) / 2
                prev_speed, speed = speed, speed + plus
        else:
            prev_speed, speed = speed, speed + 1


if __name__ == '__main__':
    res = find_best_speed(3, [5, 3, 1])
    print(res)