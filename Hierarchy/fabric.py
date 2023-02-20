from figures import Point, Line, Square, Circle, Triangle, Rectangle, Ellipse


def create_object(num: int):
    d = {'point': Point, 'line': Line, 'square': Square, 'circle': Circle, 'triangle': Triangle,  'rectangle': Rectangle
         , 'ellipse': Ellipse}
    d2 = {'point': ['X', 'Y'], 'line': ['X1', 'Y1', 'X2', 'Y2'], 'square': ['Length of side'], 'circle': ['Radius'],
          'triangle': ['First (left) side length', 'Second (right) side length', 'Third (base) side length', 'Height'],
          'rectangle': ['Length', 'Width'], 'ellipse': ['First axis (width)', 'Second axis (height)']}
    object_name = input(f'Enter figure n_{num + 1} name(Point, Line, Square, Circle, Triangle, Rectangle, '
                        f'Ellipse):').lower()
    parameters_needed = d2[object_name.strip().lower()]
    parameters = []
    for p in parameters_needed:
        parameters.append(int(input(p + ' :')))
    sign = input('Sign for displaying object: ')
    parameters.append(sign)
    figure = d[object_name](*parameters)
    return figure


def few_objects(num: int):
    collection = []
    for i in range(num):
        collection.append(create_object(i))
    for f in collection:
        print(f, '\n')
        f.display_info()
        print('~'*15)


few_objects(2)