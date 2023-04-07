from collections import defaultdict


# Разница в defaultdict/dict - defaultdict сделал доступным динамичное создание несуществующего ключа, пример:
arr = [('Hello', 3), ('Ulyana', 9), ('Ilya', 9), ('Hello', 6)]
d = defaultdict(list)
for k, v in arr:
    d[k].append(v)
print(d)
# Этот метод гораздо проще и удобнее, чем эквивалентный ему setdefaultdict:

d = {}
for k, v in arr:
    d.setdefault(k, []).append(v)
print(d, '\n', sorted(d.items()))


# Установка функции int() в качестве функции defaultfactory, генерирующей значение по умолчанию, делает defaultdict по
# лезным для чего-либо.
s = 'missisipi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d)


# Более быстрый и гибкий способ создания постоянных функций заключается в использовании лямбда-функции, которая может
# предоставлять любое постоянное значение, не только равное нулю
def constant_factory(value):
    return lambda: value


d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print(d)
print('%(name)s %(action)s to %(object)s' % d)
