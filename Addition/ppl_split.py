def possible(n, matrix) -> bool:
    if n == 2:
        return True
    m = len(matrix[0])
    all_ppl = set([i for i in range(1, n + 1)])
    gr1, gr2, known = set(), set(), dict()
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                if i in known:
                    known[i].add(j)
                else:
                    known[i] = {j}
    while all_ppl:
        p = all_ppl.pop()
        if not len(gr1):
            gr1.add(p)
        elif not len(gr2):
            gr2.add(p)
        else:
            if p in known:
                known_ = known[p]
            else:
                known_ = set()
            if len(gr1 & known_):
                if len(gr2 & known_):
                    return False
                else:
                    gr2.add(p)
            else:
                gr1.add(p)
    return True


n1, m1 = 4, [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]
n2, m2 = 4, [[0 for _ in range(4)] for _ in range(4)]
n3, m3 = 5, [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]
n4, m4 = 6, [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0]]
n_, m_ = n1, m1

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

result = 'Yes' if possible(_n, arr) else 'No'
print('Result is ready.')

with open('ppl_split_output.txt', 'w', encoding='utf-8-sig') as out_writer:
    out_writer.write(result)
    print('Result is written.')




