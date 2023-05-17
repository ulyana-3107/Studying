# Написать программу, которая для строк математических выражений (а-ля «1+8*9+3/3-8») вычисляла значение этого
# выражения. Для простоты считаем, что из операций доступны лишь +,-,*,/, а все значения – целые числа. Функция “eval”
# под запретом. Подсказка: польская обратная запись.


def write_back(expression: str) -> str:
    stack, res_str = [], ''
    priority = {'(': 1, '*': 3, '/': 3, '+': 2, '-': 2, ')': None}

    for i in expression:
        if i == '(':
            stack.append(i)

        elif i not in priority:
            res_str += i

        elif i == ')':

            while stack[-1] != '(':
                res_str += stack.pop()
            stack.pop()

        elif i in priority:
            pr = priority[i]
            if not len(stack) or priority[stack[-1]] < pr:
                stack.append(i)

            elif priority[stack[-1]] >= pr:

                while True:
                    if len(stack):
                        if priority[stack[-1]] >= pr:
                            res_str += stack.pop()
                        else:
                            break
                    else:
                        break

    while len(stack):
        res_str += stack.pop()

    return res_str


def sum_op(a: int, b: int) -> int:
    return a + b


def subtract_op(a: int, b: int) -> int:
    return a - b


def mult_op(a: int, b: int) -> int:
    return a * b


def div_op(a: int, b: int) -> float|int:
    return a/b


def calc_writeback(writeback: str) -> int:
    operators = {'+': sum_op, '-': subtract_op, '*': mult_op, '/': div_op}
    stack = []

    for elem in writeback:
        if elem not in operators:
            stack.append(elem)
        else:
            r_op, l_op = int(stack.pop()), int(stack.pop())
            stack.append(operators[elem](l_op, r_op))

    return stack[0]


if __name__ == '__main__':
    tests = ['1*(2+9-8)/3', '1+8*9+3/3-8', '2+9*7-4/2', '8/4', '2+2', '1-0']
    for t in tests:
        wr = write_back(t)
        print(wr)
        print(calc_writeback(wr), '\n')






