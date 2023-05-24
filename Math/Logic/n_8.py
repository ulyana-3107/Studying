# То же что и 7, но с добавлением операций эквивалентности (~), исключающее ИЛИ (+), импликация (>).
from collections import deque
from n_9_3 import create_truth_table


def implication(a: int | bool, b: int | bool) -> int:
    return 0 if (a, b) == (1, 0) else 1


def calc_expression(expression: str, table: list) -> list:
    signs = {'!': lambda x: int(not (x)), '&': lambda x, y: int(x and y), '^': lambda x, y: int(x and y),
             '>': implication,
             '~': lambda x, y: int(x == y), '+': lambda x, y: int(x != y), '|': lambda x, y: int(x or y)}
    priority = {'(': 0, '!': 5, '&': 4, '^': 4, '|': 3, '>': 2, '~': 1, '+': 1}
    stack, res = [], []

    for elem in expression:
        if elem not in priority:
            if elem == ')':

                while stack[-1] != '(':
                    res.append(stack.pop())

                stack.pop()
                continue

            res.append(elem)

        else:
            if not len(stack) or elem == '(':
                stack.append(elem)
                continue

            pr = priority[elem]

            if priority[stack[-1]] < pr:
                stack.append(elem)
                continue

            while True:
                if len(stack):
                    if priority[stack[-1]] >= pr:
                        res.append(stack.pop())
                        continue
                    break
                else:
                    break

            stack.append(elem)

    while len(stack):
        res.append(stack.pop())

    res = deque(res)
    answer, ind, i = [], {}, 0

    for elem in res:
        if elem not in ind and elem not in signs:
            ind[elem] = i
            i += 1

    for t in table:
        exp = res
        lst = []

        while len(exp) > 1:

            while exp[0] not in signs:
                lst.append(exp.popleft())

            lst.append(exp.popleft())

            operand = lst.pop()

            if operand == '!':
                r = lst.pop()
                if not type(r) == int:
                    r = t[ind[r]]

                exp.appendleft(signs[operand](r))
                continue

            r, l = lst.pop(), lst.pop()

            if not type(r) == int:
                r = t[ind[r]]
            if not type(l) == int:
                l = t[ind[l]]

            exp.appendleft(signs[operand](l, r))

        answer.append(exp[0])

    return answer


if __name__ == '__main__':
    expressions = ['A|B&!C~B', 'B>A^B~A', 'A>B|(!A^B)']
    signs = '|&!~^>()'

    for exp in expressions:
        values = [v for v in exp if v not in signs]
        table = create_truth_table(len(set(values)))

        res_table = calc_expression(exp, table)
        print(res_table)
