# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n/2⌋ times. You may assume that the majority element
# always exists in the array.


# Решение: заводится словарь со счетчиком количества вхождений и переменная - массив, содержащий элемент, входящий в
# массив максимльное количество раз, и это количество, и если найден новый элемент, то он просто добавляется в словарь,
# если найден уже встретившийся элемент, то: 1. инкрементируется его значение в словаре 2. проверяется, не превосходит
# ли оно текущее максимальное значение, если да - то меняется переменная, если нет - продолжить.


def solution(nums: list) -> int:
    counter = {}
    m = []
    for n in nums:
        if not len(m):
            m = [n, 1]
            counter[n] = 1
        else:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
                if counter[n] > m[1]:
                    m = [n, counter[n]]
    return m[0]



