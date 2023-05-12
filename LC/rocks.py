import heapq
from collections import deque
import bisect


def rocks_heap_solution(seq: list) -> int:
    seq2 = seq.copy()
    heapq.heapify(seq2)

    while len(seq2) > 1:
        n = len(seq2)
        largest = heapq.nlargest(2, enumerate(seq2), key=lambda x: x[1])
        a, b, a_index, b_index = largest[0][1], largest[1][1], largest[0][0], largest[1][0]

        if a == b:
            if a_index in range(n - 2) and b_index in range(n - 2):
                seq2[a_index], seq2[-2] = seq2[-2], seq2[a_index]
                seq2[b_index], seq2[-1] = seq2[-1], seq2[b_index]
            else:
                case1 = a_index in range(n - 2, n) and b_index not in range(n - 2, n)
                case2 = b_index in range(n - 2, n) and a_index not in range(n - 2, n)
                if case1:
                    repl_index = n - 1 if a_index == n - 2 else n - 2
                    seq2[b_index], seq2[repl_index] = seq2[repl_index], seq2[a_index]
                elif case2:
                    repl_index = n - 1 if b_index == n - 2 else n - 2
                    seq2[a_index], seq2[repl_index] = seq2[repl_index], seq2[a_index]

            for i in range(2):
                seq2.pop()
        else:
            diff = abs(a - b)

            if a > b:
                del_index, change_elem_index = b_index, a_index
            else:
                del_index, change_elem_index = a_index, b_index

            seq2[change_elem_index] = diff

            if del_index != n - 1:
                seq2[del_index], seq2[-1] = seq2[-1], seq2[del_index]

            seq2.pop()

    return seq2[0] if len(seq2) else 0


def rocks_heap2(arr: list) -> int:
    arr2 = arr.copy()
    arr2 = [-i for i in arr2]
    heapq.heapify(arr2)

    while len(arr2) > 1:

        a = heapq.heappop(arr2)
        b = heapq.heappop(arr2)

        if a > b:
            diff = -(-b + a)
            bisect.insort(arr2, diff)
        elif b > a:
            diff = -(-a + b)
            bisect.insort(arr2, diff)

    return -arr2[0] if len(arr2) else 0


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


if __name__ == '__main__':
    arr0 = [1, 2, 3, 4, 5]  # 1
    arr1 = [0, 9, 8, 7, 6, 5, 4, 3]  # 0
    arr2 = [-2, 4, 1, 5, 3, 7]  # -2
    arr3 = [0, 0, 0, 0, 0]  # 0
    arr4 = [-1, -1, -1, -1, -3]  # -3
    arr5 = [0, 1, 0, 1]  # 0
    arr6 = [9, 9, 9, 9, 9]  # 9
    for i in range(7):
        name = 'arr' + str(i)
        print(rocks_heap_solution(eval(name)), rocks_solution2(eval(name)),
              rocks_solution3(eval(name)), rocks_deque_solution(eval(name)), sep=' ## ')
