import numpy as np
from multiprocessing import Pool
import multiprocessing
from collections import deque


def read_matrix(file: str) -> list:
    matrix = []
    with open(file, 'r', encoding='utf-8-sig') as file:
        for line in file.readlines():
            arr = [int(i) for i in line.strip().split(',')]
            matrix.append(arr)

    return matrix


def mult_rows(rows: list, matrix2: list, results, id: int):
    curr, result = [id], []

    for i in range(len(rows)):
        for col in zip(*matrix2):
            result.append(sum(x * y for x, y in zip(rows[i], col)))

        curr.append(result)
        result = []

    results.append(curr)


def mult_matrixes(matrix1, matrix2, num_processes):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError('Number of matrix1 columns != number of matrix2 rows.')

    matrix1, jobs = deque(matrix1), []

    manager = multiprocessing.Manager()

    if len(matrix1) <= num_processes:
        t1, t2, rest = len(matrix1), 1, None
    else:
        t1, t2, rest = num_processes, len(matrix1) // num_processes, len(matrix1) % num_processes

    res_matrix = manager.list()

    for i in range(t1):
        rows = []
        if i == t1 - 1 and rest:
            rng = rest + t2
        else:
            rng = t2

        for j in range(rng):
            rows.append(matrix1.popleft())
        process = multiprocessing.Process(target=mult_rows, args=(rows, matrix2, res_matrix, i))
        process.start()
        jobs.append(process)

    for i in range(t1):
        jobs[i].join()

    matrix = []
    sorted_arr = sorted(res_matrix, key=lambda arr: arr[0])
    for arr in sorted_arr:
        for i in range(len(arr)):
            if i != 0:
                matrix.append(arr[i])

    return matrix


if __name__ == '__main__':
    matrix1 = np.array(read_matrix('file1'))
    matrix2 = np.array(read_matrix('file2'))

    num_processes = 4

    result = mult_matrixes(matrix1, matrix2, num_processes)
    for r in result:
        print(r)
