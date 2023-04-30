import os
import numpy


# Генерация выборки нормального распределения размером N и запись в файл.
N = 10
normal = numpy.random.normal(size=N)

with open('../normal_distribution.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write('Normal\n')
    writer.write(','.join([str(n) for n in normal]))


# Генерация выборки равномерного распределения размером N и запись в файл.
N = 10
uniform = numpy.random.uniform(size=N)

with open('../uniform_distribution.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write('Uniform\n')
    writer.write(','.join([str(n) for n in uniform]))


# Генерация выборки экспоненциального распределения размером N и запись в файл.
N = 10
exponential = numpy.random.exponential(size=N)

with open('../exponential_distribution.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write('Exponential\n')
    writer.write(','.join([str(n) for n in exponential]))
