import heapq
from collections import deque


def rocks_heap_solution(seq: list) -> int:
    heapq.heapify(seq)

    while len(seq) > 1:
        n = len(seq)
        largest = heapq.nlargest(2,  enumerate(seq), key=lambda x: x[1])
        a, b, a_index, b_index = largest[0][1], largest[1][1], largest[0][0], largest[1][0]

        if a == b:
            if a_index in range(n - 2) and b_index in range(n - 2):
                seq[a_index], seq[-2] = seq[-2], seq[a_index]
                seq[b_index], seq[-1] = seq[-1], seq[b_index]
            else:
                case1 = a_index in range(n - 2, n) and b_index not in range(n - 2, n)
                case2 = b_index in range(n - 2, n) and a_index not in range(n - 2, n)
                if case1:
                    repl_index = n - 1 if a_index == n - 2 else n - 2
                    seq[b_index], seq[repl_index] = seq[repl_index], seq[a_index]
                elif case2:
                    repl_index = n - 1 if b_index == n - 2 else n - 2
                    seq[a_index], seq[repl_index] = seq[repl_index], seq[a_index]

            for i in range(2):
                seq.pop()
        else:
            diff = abs(a - b)

            if a > b:
                del_index, change_elem_index = b_index, a_index
            else:
                del_index, change_elem_index = a_index, b_index

            seq[change_elem_index] = diff

            if del_index != n - 1:
                seq[del_index], seq[-1] = seq[-1], seq[del_index]

            seq.pop()

    return seq[0] if len(seq) else 0


def rocks_deque_solution(seq: list) -> int:
    seq = deque(seq)
    n = len(seq)
    removed = True

    while n > 1:
        r = 2 if removed else 1
        for i in range(r):
            for j in range(n - 1, 0, -1):
                if seq[j] > seq[j - 1]:
                    seq[j], seq[j - 1] = seq[j - 1], seq[j]

        elem1, elem2 = seq[0], seq[1]
        diff = abs(elem1 - elem2)

        if diff > 0:
            if elem1 > elem2:
                seq[0], seq[1] = seq[1], seq[0]

            seq[1] = diff
            seq.popleft()
            n -= 1
            removed = False

        else:
            for i in range(2):
                seq.popleft()

            n -= 2
            removed = True

    return seq[0] if len(seq) else 0


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
