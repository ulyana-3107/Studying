def possible(n, matrix) -> tuple:
    if n == 2:
        return [1], [2], True
    m = n
    all_ppl = set([i for i in range(n)])
    gr1, gr2, known = set(), set(), dict()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and i != j:
                if i in known:
                    known[i].add(j)
                else:
                    known[i] = {j}
    while all_ppl:
        p = all_ppl.pop()
        if p in known:
            known_ = known[p]
        else:
            known_ = {}
        if len(gr1 & known_):
            if len(gr2 & known_):
                return [i + 1 for i in gr1], [i + 1 for i in gr2], False
            else:
                gr2.add(p)
        else:
            gr1.add(p)
    return [i + 1 for i in gr1], [i + 1 for i in gr2], True


n1, m1 = 4, [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]
n2, m2 = 4, [[0 for _ in range(4)] for _ in range(4)]
n3, m3 = 5, [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]
n4, m4 = 6, [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0]]
n5, m5 = 5, [[0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0]]
n_, m_ = n5, m5

with open('ppl_split_input.txt', 'w', encoding='utf-8-sig') as in_writer:
    in_writer.write(str(n_) + '\n')
    for arr in m_:
        to_write = ' '.join([str(i) for i in arr])
        in_writer.write(to_write + '\n')
    print('Input is written.')

with open('ppl_split_input.txt', 'r', encoding='utf-8-sig') as reader:
    _n, arr = int(reader.readline().strip()), []
    for line in reader.readlines():
        arr.append([int(i) for i in line.strip().split(' ')])
    print('Input is read.')

result = possible(_n, arr)
print('Result is ready.')

with open('ppl_split_output.txt', 'w', encoding='utf-8-sig') as out_writer:
    for r in result:
        out_writer.write(str(r) + '\n')
    print('Result is written.')
