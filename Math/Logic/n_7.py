# Основываясь на решении 6, написать программы для построения таблицы истинности для заданной функции в виде формулы
# (а-ля «A & B | C»). Для простоты ограничимся операциями: конъюнкция (&), дизъюнкция (|), отрицание (!), а переменные
# состоят из одной заглавной буквы.
from n_9_3 import create_truth_table
from collections import deque


def calc_expression(expression: str, table: list) -> list:
    signs = {'!': lambda x: int(not x), '&': lambda x, y: int(x and y), '^': lambda x, y: int(x and y),
             '|': lambda x, y: int(x or y)}
    priority = {'(': 0, '!': 3, '&': 2, '^': 2, '|': 1}
    stack, expr, res, vals, ind = [], [], [], set(), {}

    for elem in expression:
        if elem not in priority:

            if elem == ')':

                while stack[-1] != '(':
                    expr.append(stack.pop())
                stack.pop()
                continue

            expr.append(elem)

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
                    pr_ = priority[stack[-1]]
                    if pr_ >= pr:
                        expr.append(stack.pop())
                        continue

                    break

                else:
                    break

            stack.append(elem)

    while len(stack):
        expr.append(stack.pop())

    for elem in expr:
        if elem not in signs:
            vals.add(elem)
    vals = ''.join(vals)

    for i in range(len(vals)):
        ind[vals[i]] = i

    for t in table:
        rpn = deque(expr)
        lst = []

        while len(rpn) > 1:
            while rpn[0] not in signs:
                lst.append(rpn.popleft())

            lst.append(rpn.popleft())

            if lst[-1] == '!':
                operand, r = lst.pop(), lst.pop()

                if not type(r) == int:
                    r = t[ind[r]]

                rpn.appendleft(signs[operand](r))

            else:
                operand, r, l = lst.pop(), lst.pop(), lst.pop()

                if not type(l) == int:
                    l = t[ind[l]]
                if not type(r) == int:
                    r = t[ind[r]]

                rpn.appendleft(signs[operand](l, r))

        res.append(rpn[0])

    return res


if __name__ == '__main__':
    expressions = ['A&B|C', 'A^B^!C|B^A', 'P|(Q^!T)']
    signs = '!&|^()'

    for exp in expressions:

        nums = [num for num in exp if num not in signs]
        table = create_truth_table(len(set(nums)))

        print(calc_expression(exp, table))