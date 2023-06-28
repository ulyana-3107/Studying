from calculator import Calculator


actions = {'plus': (5, 8), 'minus': (7, 2), 'multiply': (2, 6), 'divide': (9, 3)}
calc = Calculator()


for k, v in actions.items():
    res = eval(f'calc.{k}')(v[0], v[1])
    print(res)