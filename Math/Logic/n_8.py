# То же что и 7, но с добавлением операций эквивалентности (~), исключающее ИЛИ (+), импликация (>).


from n_9_3 import create_truth_table


def equivalence(a: int | bool, b: int | bool) -> int:
    return int(a == b)


def xor(a: int | bool, b: int | bool) -> int:
    return 1 if a != b else 0


def implication(a: int | bool, b: int | bool) -> int:
    return 0 if (a, b) == (1, 0) else 1


def inversion(a: int | bool) -> int:
    return int(not a)


def conjugation(a: int | bool, b: int | bool) -> int:
    return a and b


def disjunction(a: int | bool, b: int | bool) -> int:
    return a or b


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
    signs = {'!': inversion, '&': conjugation, '^': conjugation, '>': implication, '~': equivalence, '+': xor, '|':disjunction}
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
    expressions = ['A|B&!C~B', 'B>A^B~A']
    signs = '|&!~^>'

    for exp in expressions:
        values = [v for v in exp if v not in signs]
        table = create_truth_table(len(set(values)))
        result = []
        wr = write_back(exp)
        print(wr)
        for t in table:
            result.append(calc_writeback(wr, t))
        print(result, '\n', '_'*30)

