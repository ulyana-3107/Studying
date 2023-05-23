# Написать программу, которая для строк математических выражений (а-ля «1+8*9+3/3-8») вычисляла значение этого
# выражения. Для простоты считаем, что из операций доступны лишь +,-,*,/, а все значения – целые числа. Функция “eval”
# под запретом.


def calc_expression(expression: str) -> str:
    operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b,
                 '/': lambda a, b: int(a / b)}
    stack, res, num = [], [], ''
    priority = {'(': 1, '*': 3, '/': 3, '+': 2, '-': 2, ')': None}

    for i in expression:

        if i not in priority:
            num += i

        else:
            if len(num):
                res.append(int(num))
                num = ''

            if i == '(':
                stack.append(i)

            elif i == ')':

                while stack[-1] != '(':
                    res.append(stack.pop())
                    operand, r, l = res.pop(), res.pop(), res.pop()
                    res.append(operators[operand](l, r))
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
                                    res.append(stack.pop())
                                    operand, r, l = res.pop(), res.pop(), res.pop()
                                    res.append(operators[operand](l, r))
                                else:
                                    break

                            else:
                                break

                        stack.append(i)
    if num:
        res.append(int(num))

    while len(stack):
        res.append(stack.pop())
        operand, r, l = res.pop(), res.pop(), res.pop()
        res.append(operators[operand](l, r))

    return res[0]


if __name__ == '__main__':
    tests = ['1*(2+9-8)/3', '1+8*9+3/3-8', '(4+7)+12/3', '2+9*7-4/2', '8/4', '2+2', '1-0']
    results = [1, 66, 15, 63, 2, 4, 1]
    for t in tests:

        wr = calc_expression(t)
        print(wr, '\n')