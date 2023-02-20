import itertools


def permutations(elements: list, min_elems, max_elems) -> list:
    result = list()
    for i in range(min_elems, max_elems + 1):
        perm = itertools.permutations(elements, i)
        result.extend(perm)
    return result


def permutations_iterator(elems: list, min_, max_):
    for i in range(min_, max_ + 1):
        perms = itertools.permutations(elems, i)
        for p in perms:
            yield p


def tickets(matrix_costs: list) -> int:
    n = len(matrix_costs)
    arr, min_elems, max_elems = [1, 2, 3], 1, 3
    basic_permutations = permutations(arr, min_elems, max_elems)
    min_, max_ = 1, len(basic_permutations)
    print(basic_permutations)
    main_permutations, ways = permutations_iterator(basic_permutations, min_, max_), list()
    while True:
        try:
            case = next(main_permutations)
            if len(case) == 1:
                if sum(case[0]) == n:
                    ways.append(case)
            else:
                c = 0
                for c_ in case:
                    c += sum(c_)
                if c == n:
                    ways.append(case)
        except StopIteration:
            break
    print(ways)


def get_time(time_costs: list, way: list) -> int:
    result_cost, index = 0, 0
    iter_ = 0
    for step in way:
        if iter_ == 0:
            result_cost += time_costs[index][step - 1]
            index += step
        else:
            result_cost += time_costs[index][step - 1]
            index += step
        iter_ += 1
    return result_cost


# time_costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [1, 4, 8], [3, 2, 5], [-2, 4, 6], [7, 2, 2]]
# ways = [[3, 1, 3], [1, 3, 3], [2, 2, 3], [3, 3, 1], [1, 1, 1, 2, 2]]
# for way in ways:
#     print(get_time(time_costs, way))
test = [[1, 2, 3], [3, 2, 1], [1, 1, 1], [2, 2, 2], [3, 1, 0]]
test = [[1, 2, 3], [3, 2, 1]]
tickets(test)

