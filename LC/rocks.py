import heapq
from collections import deque
import bisect


def rocks_deque_solution(seq: list) -> int:
    seq2 = seq.copy()
    seq2 = deque(seq2)
    n = len(seq2)
    removed = True

    while n > 1:
        r = 2 if removed else 1
        for i in range(r):
            for j in range(n - 1, 0, -1):
                if seq2[j] > seq2[j - 1]:
                    seq2[j], seq2[j - 1] = seq2[j - 1], seq2[j]

        elem1, elem2 = seq2[0], seq2[1]
        diff = abs(elem1 - elem2)

        if diff > 0:
            if elem1 > elem2:
                seq2[0], seq2[1] = seq2[1], seq2[0]

            seq2[1] = diff
            seq2.popleft()
            n -= 1
            removed = False

        else:
            for i in range(2):
                seq2.popleft()

            n -= 2
            removed = True

    return seq2[0] if len(seq2) else 0


def rocks_solution2(seq: list) -> int:
    seq.sort()
    n = len(seq)
    while n > 1:
        elem1, elem2 = seq[-2], seq[-1]
        diff = abs(elem1 - elem2)

        if diff > 0:
            if elem1 < elem2:
                seq[-2], seq[-1] = seq[-1], seq[-2]

            seq[-2] = diff
            seq.pop()
            n -= 1
        else:
            for i in range(2):
                seq.pop()
            n -= 2

    return seq[0] if len(seq) else 0


def rocks_solution3(seq: list) -> int:
    n = len(seq)
    removed = True

    while n > 1:
        r = 2 if removed else 1
        for i in range(r):
            for j in range(n - 1):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]

        elem1, elem2 = seq[-2], seq[-1]
        diff = abs(elem1 - elem2)

        if diff > 0:
            if elem1 < elem2:
                seq[-2], seq[-1] = seq[-1], seq[-2]

            seq.pop()
            seq[-1] = diff

            n -= 1
            removed = False
        else:
            for i in range(2):
                seq.pop()
            removed = True
            n -= 2

    return seq[0] if len(seq) else 0


def rocks_heap2(arr: list) -> int:
    arr = [-i for i in arr]
    heapq.heapify(arr)

    while len(arr) > 1:

        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        if a != b:
            heapq.heappush(arr, -b + a)

    return -arr[0] if len(arr) else 0


if __name__ == '__main__':
    arr0 = [1, 2, 3, 4, 5]  # 1
    arr1 = [0, 9, 8, 7, 6, 5, 4, 3]  # 0
    arr2 = [-2, 4, 1, 5, 3, 7]  # -2
    arr3 = [0, 0, 0, 0, 0]  # 0
    arr4 = [-1, -1, -1, -1, -3]  # -3
    arr5 = [0, 1, 0, 1]  # 0
    arr6 = [9, 9, 9, 9, 9]  # 9
    arr7 = [4, 77, 27, 20, 37, 49, 76, 42, 46, 82]  # 0

    for i in range(0, 8):
        name = 'arr' + str(i)
        print(rocks_heap2(eval(name)))
