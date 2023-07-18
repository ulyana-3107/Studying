import numpy as np
from multiprocessing import Pool


def multiply_row(row, matrix2):
    result = []
    for col in zip(*matrix2):
        result.append(sum(x * y for x, y in zip(row, col)))
    return result


def mult_matrixes(matrix1, matrix2, num_processes):
    result = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

    with Pool(num_processes) as pool:
        results = pool.starmap(multiply_row, [(matrix1[i], matrix2) for i in range(len(matrix1))])
        for i, row in enumerate(results):
            result[i] = row

    return result


if __name__ == '__main__':
    matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[2, 4], [6, 8], [10, 12]])
    num_processes = 4

    result = mult_matrixes(matrix1, matrix2, num_processes)
    print(result)
