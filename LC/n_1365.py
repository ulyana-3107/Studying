def num_of_less(seq: list) -> list:
    n, res, seq2 = len(seq), [], seq.copy()
    if n < 2:
        return [0]
    for i in range(1, n):
        for j in range(i, 0, -1):
            if seq[j] < seq[j - 1]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]
            else:
                break
    print(f'seq after sorting: {seq}, seq2: {seq2}')
    visited = {}
    for el in seq2:
        if el in visited:
            res.append(visited[el])
        else:
            for i in range(n):
                if seq[i] == el:
                    res.append(i)
                    visited[el] = i
                    break
    return res


print(num_of_less([8, 1, 2, 2, 3]))  # 4 0 1 1 3