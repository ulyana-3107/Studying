def create_dict(m: list, n: int) -> dict:
    d = {}
    for i in range(n):
        d[i + 1] = set([j + 1 for j in range(n) if m[i][j] == 1 and i != j])
    return d


def dividible(matrix: list, n: int) -> tuple:
    if n < 3:
        return True, {1}, {2}
    known, ppl = create_dict(matrix, n), [False for i in range(n)]
    g1, g2 = set(), set()
    for i in range(n):
        if len(known[i + 1]) > 0:
            p = known[i + 1].pop()
            g1.add(i + 1)
            g2.add(p)
            ppl[i], ppl[p - 1] = True, True
            known[i + 1].add(p)
            break
    if len(g1) == 0:
        return 'Yes', [i + 1 for i in range(n//2)], [i + 1 for i in range(n//2, n)]
    temp = set()
    for i in range(n):
        if not ppl[i]:
            p = i + 1
            nbrs = known[p]
            if not len(nbrs):
                g1.add(p)
                ppl[i] = True
            else:
                a, b = nbrs & g1, nbrs & g2
                if len(a) > 0 and len(b) == 0:
                    g2.add(p)
                    ppl[p - 1] = True
                elif len(b) > 0 and len(a) == 0:
                    g1.add(p)
                    ppl[p - 1] = True
                elif len(a) > 0 and len(b) > 0:
                    return 'No', set(), set()
                else:
                    temp.add(p)
    if not len(temp):
        return 'Yes', g1, g2
    else:
        g1_, g2_ = set(), set()
        temp_, c = set(), 0
        while len(temp):
            p1 = temp.pop()
            nbrs = known[p1]
            if c == 0:
                p2 = nbrs.pop()
                temp -= {p2}
                g1_.add(p1)
                g2_.add(p2)
                ppl[p1 - 1], ppl[p2 - 1] = True, True
                c += 1
            else:
                a, b = nbrs & g1_, nbrs & g2_
                if not len(a) and not len(b) or len(a) and len(b):
                    temp_.add(p1)
                else:
                    if len(b) and not len(a):
                        g1_.add(p1)
                    elif len(a) and not len(b):
                        g2_.add(p1)
                    ppl[p1 - 1] = True
        if not len(temp_):
            g1.update(g1_)
            g2.update(g2_)
            return 'Yes', g1, g2
        else:
            return 'No', set(), set()


m = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]  # True
m1 = [[1, 0, 0, 1, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 1]]  # True
m2 = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]  # False
m3 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 0]]

with open('acquaintances.input.txt', 'w', encoding='utf-8-sig') as writer:
    writer.write(str(len(m3)) + '\n')
    for arr in m3:
        writer.write(' '.join([str(i) for i in arr]) + '\n')

with open('acquaintances.input.txt', 'r', encoding='utf-8-sig') as reader:
    num = int(reader.readline().strip())
    matrix = []
    for line in reader.readlines():
        matrix.append([int(i) for i in line.strip().split(' ')])

with open('acquaintances.result.txt', 'w', encoding='utf-8-sig') as writer:
    bool_res, gr1, gr2 = dividible(matrix, num)
    writer.write(str(bool_res) + '\n')
    writer.write('Group 1: ' + ','.join([str(i) for i in gr1]) + '\n')
    writer.write('Group 2: ' + ','.join([str(i) for i in gr2]) + '\n')




