from __future__ import annotations
import os
import numpy
import argparse


def find_parameters(dist: list) -> dict:
    parameters = {}

    mean_value = find_mean_value(dist)
    variance = find_variance(dist)
    standart_deviation = find_standart_deviation(dist)

    parameters['mean_value'] = mean_value
    parameters['variance'] = variance
    parameters['standart_deviation'] = standart_deviation

    return parameters


def find_mean_value(dist: list) -> float|int:
    dist = numpy.array(dist)
    return dist.mean()


def find_variance(dist: list) -> float|int:
    dist = numpy.array(dist)
    return dist.var()


def find_standart_deviation(dist: list) -> float|int:
    dist = numpy.array(dist)
    return dist.std()


def read_and_output(in_path: str, out_path: str) -> None:

    with open(in_path, 'r', encoding='utf-8-sig') as reader:
        type = reader.readline().strip().lower()

        dist = []
        for line in reader.readlines():
            dist.extend([float(n) for n in [i for i in line.split(',')]])

    parameters = find_parameters(dist)

    with open(out_path, 'w', encoding='utf-8-sig') as writer:
        for k, v in parameters.items():
            writer.write(k + ' - ' + str(v) + '\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Distribution parameters finding')
    parser.add_argument('input_path', type=str, help='Path to the file with distribution')
    parser.add_argument('output_path', type=str, help='Path to the file for output to be written')
    arguments = parser.parse_args()

    read_and_output(arguments.input_path, arguments.output_path)