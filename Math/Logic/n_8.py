# То же что и 7, но с добавлением операций эквивалентности (~), исключающее ИЛИ (+), импликация (>).


from n_9_3 import create_truth_table


def implication(a: int | bool, b: int | bool) -> int:
    return 0 if (a, b) == (1, 0) else 1


def write_back(expression: str) -> str:
    # + - XOR/(+)
    priority = {'(': 0, '!': 5, '&': 4, '^': 4, '|': 3, '>': 2, '~': 1, '+': 1}
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
                    if priority[stack[-1]] >= pr:
                        res_str += stack.pop()
                        continue
                    break
                else:
                    break

            stack.append(elem)

    while len(stack):
        res_str += stack.pop()

    return res_str


def calc_writeback(writeback: str, values: list) -> int | bool:
    writeback = writeback.lower()
    signs = {'!': lambda x: int(not(x)), '&': lambda x, y: int(x and y), '^': lambda x, y: int(x and y), '>': implication,
             '~': lambda x, y: int(x == y), '+': lambda x, y: int(x != y), '|': lambda x, y: int(x or y)}
    vals = ''.join([v for v in writeback if v not in signs])
    ind, stack = {}, []

    for k, v in enumerate(vals):
        if v not in ind:
            ind[v] = k

    for elem in writeback:
        if elem not in signs:
            stack.append(values[ind[elem]])
            continue

        if elem == '!':
            op = stack.pop()
            stack.append(signs[elem](op))
            continue

        r_op, l_op = stack.pop(), stack.pop()
        stack.append(signs[elem](l_op, r_op))

    return stack[-1]


if __name__ == '__main__':
    expressions = ['A|B&!C~B', 'B>A^B~A', 'A>B|(!A^B)']
    signs = '|&!~^>()'

    for exp in expressions:
        values = [v for v in exp if v not in signs]
        table = create_truth_table(len(set(values)))
        result = []
        wr = write_back(exp)
        print(wr)
        for t in table:
            result.append(calc_writeback(wr, t))
        print(result, '\n', '_'*30)

