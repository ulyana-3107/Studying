# Написать программу, которая для строк математических выражений (а-ля «1+8*9+3/3-8») вычисляла значение этого
# выражения. Для простоты считаем, что из операций доступны лишь +,-,*,/, а все значения – целые числа. Функция “eval”
# под запретом.


def write_back(expression: str) -> str:
    stack, res_str, num = [], '', ''
    priority = {'(': 1, '*': 3, '/': 3, '+': 2, '-': 2, ')': None}

    for i in expression:

        if i not in priority:
            num += i

        else:
            if len(num):
                # square brackets are used to identify numbers that are > 9.
                res_str += '[' + num + ']'
                num = ''

            if i == '(':
                stack.append(i)

            elif i == ')':

                while stack[-1] != '(':
                    res_str += stack.pop()
                stack.pop()

            else:
                pr = priority[i]

                if not len(stack) or stack[-1] == '(':
                    stack.append(i)

                else:
                    if not len(stack):
                        stack.append(i)

                    elif pr > priority[stack[-1]]:
                        stack.append(i)

                    else:
                        while True:

                            if len(stack):
                                if priority[stack[-1]] >= pr:
                                    res_str += stack.pop()

                                else:
                                    break

                            else:
                                break

                        stack.append(i)

    if len(num):
        res_str += '[' + num + ']'

    while len(stack):
        res_str += stack.pop()

    return res_str


def calc_writeback(writeback: str) -> int:
    operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: int(a/b)}
    stack = []
    el = ''

    for elem in writeback:

        if elem == '[':
            el += ''
            continue

        elif elem in '0123456789':
            el += elem

        elif elem == ']':

            stack.append(el)
            el = ''

        else:
            r_op, l_op = int(stack.pop()), int(stack.pop())
            stack.append(operators[elem](l_op, r_op))

    return int(stack[0])


if __name__ == '__main__':
    tests = ['1*(2+9-8)/3', '1+8*9+3/3-8', '(4+7)+12/3', '2+9*7-4/2', '8/4', '2+2', '1-0']
    results = [1, 66, 63, 2, 4, 1]
    for t in tests:

        wr = write_back(t)
        print(wr, '\n', calc_writeback(wr), '\n\n')