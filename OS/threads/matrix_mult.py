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


def mult_rows(rows: list, matrix2: list, results):
    result = []
    for i in range(len(rows)):
        for col in zip(*matrix2):
            result.append(sum(x * y for x, y in zip(rows[i], col)))

    results.append(result)


def mult_matrixes(matrix1, matrix2, num_processes):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError('Number of matrix1 columns != number of matrix2 rows.')

    matrix1, jobs = deque(matrix1), []

    manager = multiprocessing.Manager()
    res_matrix = manager.list()

    if len(matrix1) <= num_processes:
        t1, t2, rest = len(matrix1), 1, None
    else:
        t1, t2, rest = num_processes, len(matrix1) // num_processes, len(matrix1) % num_processes

    for i in range(t1):
        rows = []
        if i == t2 - 1 and rest:
            rng = rest
        else:
            rng = t2

        for j in range(rng):
            rows.append(matrix1.popleft())

        process = multiprocessing.Process(target=mult_rows, args=(rows, matrix2, res_matrix,))
        process.start()
        jobs.append(process)

    for i in range(t1):
        jobs[i].join()

    return res_matrix


if __name__ == '__main__':
    matrix1 = np.array(read_matrix('file1.txt'))
    matrix2 = np.array(read_matrix('file2.txt'))

    num_processes = 4

    result = mult_matrixes(matrix1, matrix2, num_processes)
    print(result)
