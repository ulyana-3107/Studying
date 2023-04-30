import os
import numpy
import argparse


# Генерация выборки нормального распределения размером size
def generate_normal_dist(size: int):
    normal = numpy.random.normal(size=size)
    return normal


# Генерация выборки равномерного распределения размером size
def generate_uniform_dist(size: int):
    uniform = numpy.random.uniform(size=size)
    return uniform


# Генерация выборки экспоненциального распределения размером size
def generate_exponential_dist(size: int):
    exponential = numpy.random.exponential(size=size)
    return exponential


def generate_and_write(d_type: str, path: str, size: int):
    distribution = eval(f'generate_{d_type.strip().lower()}_dist')(size)

    with open(path, 'w', encoding='utf-8-sig') as writer:
        writer.write(d_type + '\n')
        writer.write(','.join([str(d) for d in distribution]))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generating distribution')
    parser.add_argument('dist_type', type=str, help='type of distribution')
    parser.add_argument('path', type=str, help='path to the file with generated distribution')
    parser.add_argument('-s', '--size', type=int, default=10, help='size of a distribution, (default=10)')
    arguments = parser.parse_args()

    generate_and_write(arguments.dist_type, arguments.path, arguments.size)


