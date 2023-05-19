def implication(a: int | bool, b: int | bool) -> bool:
    if a and not b:
        return False

    return True


def inversion(a: int | bool) -> bool:
    return not a


def equivalence(a: int | bool, b: int | bool) -> bool:
    return a == b


def conjugation(a: int | bool, b: int | bool) -> bool:
    return a and b


def disjunction(a: int | bool, b: int | bool) -> bool:
    return a or b


def create_truth_table(n: int) -> list:
    """
    n - number of parameters in a formula
    """
    num = 2 ** n
    table = [[] for _ in range(num)]
    val, counter = 0, 0

    for i in range(n):
        mid = int(num/2**(i + 1))

        for t in table:
            t.append(val)
            counter += 1

            if counter == mid:
                counter = 0
                val = 1 if val == 0 else 0

    return table


def prove_tautology1(table: list):
    ind, params, result = {}, 'xyz', []

    for k, v in enumerate(params):
        ind[v] = k

    for t in table:

        a = implication(t[ind['x']], inversion(ind['y']))
        b = inversion(implication(t[ind['x']], t[ind['z']]))
        c = implication(a, b)
        d = inversion(implication(t[ind['z']], t[ind['y']]))
        e = conjugation(c, d)

        if not e:
            print(f'{t} gives 0')
            return

    print('Tautology proved')


def prove_tautology2(table: list):
    params, ind = 'pqrs', {}
    for k, v in enumerate(params):
        ind[v] = k

    for t in table:
        a = implication(inversion(t[ind['r']]), inversion(t[ind['s']]))
        b = conjugation(t[ind['p']], t[ind['q']])
        c = implication(a, b)
        d = implication(t[ind['p']], inversion(t[ind['q']]))
        e = implication(d, c)
        f = inversion(implication(t[ind['r']], t[ind['p']]))
        g = conjugation(e, f)

        if not g:
            print(f'{t} gives 0')
            return

    print('Tautology proved')


def prove_tautology3(table: list):
    params, ind = 'pq', {}

    for k, v in enumerate(params):
        ind[v] = k
    for t in table:
        a = implication(t[ind['q']], inversion(t[ind['q']]))
        b = conjugation(inversion(t[ind['p']]), a)
        c = disjunction(t[ind['p']], t[ind['q']])
        d = equivalence(c, b)

        if not d:
            print(f'{t} gives 0')
            return

    print('Tautology proved')


if __name__ == '__main__':
    t = create_truth_table(3)
    prove_tautology1(t)
    t2 = create_truth_table(4)
    prove_tautology2(t2)
    t3 = create_truth_table(2)
    prove_tautology3(t3)






