# Основываясь на решении 6, написать программы для построения таблицы истинности для заданной функции в виде формулы
# (а-ля «A & B | C»). Для простоты ограничимся операциями: конъюнкция (&), дизъюнкция (|), отрицание (!), а переменные
# состоят из одной заглавной буквы.
from n_9_3 import create_truth_table


def write_back(expression: str) -> str:
    priority = {'(': 0, '!': 3, '&': 2, '^': 2, '|': 1}
    stack, res_str = [], ''

    for elem in expression:
        if elem not in priority:
            if elem == ')':

                while stack[-1] != '(':
                    res_str += stack.pop()
                stack.pop()
                continue

            res_str += elem
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
                        res_str += stack.pop()
                        continue

                    break

                else:
                    break

            stack.append(elem)

    while len(stack):
        res_str += stack.pop()

    return res_str


def calc_writeback(writeback: str, values: list) -> bool:
    writeback = writeback.lower()
    vals, ind = '', {}
    signs = {'!': lambda x: int(not x), '&': lambda x, y: int(x and y), '^': lambda x, y: int(x and y),
             '|': lambda x, y: int(x or y)}

    for elem in writeback:
        if elem not in signs:
            vals += elem

    for k, v in enumerate(vals):
        if v not in ind:
            ind[v] = k

    stack = []

    for elem in writeback:
        if elem in vals:
            stack.append(values[ind[elem]])
            continue

        if elem == '!':
            op = stack.pop()
            stack.append(signs[elem](op))
            continue

        r_op, l_op = stack.pop(), stack.pop()
        stack.append(signs[elem](l_op, r_op))
        continue

    return stack[-1]


if __name__ == '__main__':
    expressions = ['A&B|C', 'A^B^!C|B^A', 'P|(Q^!T)']
    signs = '!&|^()'

    for exp in expressions:

        nums = [num for num in exp if num not in signs]
        table = create_truth_table(len(set(nums)))
        wr = write_back(exp)
        results = []

        for t in table:
            results.append(calc_writeback(wr, t))

        print(exp, results, sep = '\n')
        print('\n' + '-'*30)