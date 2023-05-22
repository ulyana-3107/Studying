def selection_sort1(seq: list) -> None:
    seq2 = seq.copy()
    res_seq = []
    while len(seq):
        m = seq[0]
        for el in seq:
            if el < m:
                m = el
        res_seq.append(m)
        seq = list(filter(lambda x: x != m, seq))
    print(seq2, res_seq, sep='\n')


# selection_sort(seq)

def selection_sort2(seq: list) -> list:
    n = len(seq)
    if n < 2:
        return seq
    for i in range(n):
        m = seq[i], i
        for j in range(i + 1, n):
            if seq[j] < m[0]:
                m = seq[j], j
        if m[0] < seq[i]:
            seq[i], seq[m[1]] = seq[m[1]], seq[i]
    return seq


# print(selection_sort2([5, 1, 3, 9, 0, 3]))


def insertion_sort(seq: list) -> list:  # O(N**2)
    n = len(seq)
    if n < 2:
        return seq
    for i in range(1, n):
        for j in range(i, 0, -1):
            if seq[j] < seq[j - 1]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]
            else:
                break
    return seq


# insertion_sort(seq)

def bubble_sort(seq: list) -> None:
    n, seq2 = len(seq), seq.copy()
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j + 1] < seq[j]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    print(f'{seq2} -> \n{seq}')


# bubble_sort(seq)

def shaker_sort(seq: list) -> None:
    n, seq2 = len(seq), seq.copy()
    start, end = 0, n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if seq[i + 1] < seq[i]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if seq[i + 1] < seq[i]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        start += 1

    print(f'{seq2} ->\n{seq}')


# shaker_sort(seq)


def merge_two_sorted(seq1: list, seq2: list) -> list:
    l1, l2 = len(seq1), len(seq2)
    merged_list, i, j = [], 0, 0
    while i < l1 or j < l2:
        if i < l1 and j < l2:
            if seq1[i] <= seq2[j]:
                merged_list.append(seq1[i])
                i += 1
            else:
                merged_list.append(seq2[j])
                j += 1
        elif i < l1 and j == l2:
            merged_list.extend(seq1[i:])
            i = l1
        else:
            merged_list.extend(seq2[j:])
            j = l2
    return merged_list


def merge_two_sorted2(seq1: list, seq2: list) -> None:
    n, m = len(seq1), len(seq2)
    merged_list, i, j = [], 0,  0
    while i < n and j < m:
        if seq1[i] <= seq2[j]:
            merged_list.append(seq1[i])
            i += 1
        else:
            merged_list.append(seq2[j])
            j += 1
    merged_list += seq1[i:] + seq2[j:]
    print(merged_list)


# s1, s2 = [1, 2, 4, 7], [0, 3, 6]
# merge_two_sorted(s1, s2)
# merge_two_sorted2(s1, s2)

def fast_merge_sort(seq: list) -> list:
    n = len(seq)
    a, b = seq[: n//2], seq[n//2:]
    if len(a) > 1:
        a = fast_merge_sort(a)
    if len(b) > 1:
        b = fast_merge_sort(b)
    return merge_two_sorted(a, b)


# seq = [9, 4, 2, 0, -1, 3]
# print(fast_merge_sort(seq))


def quick_sort(arr: list) -> list:
    if len(arr) > 1:
        x = arr[len(arr)//2]
        less, eq, higher = [i for i in arr if i < x], [i for i in arr if i == x], [i for i in arr if i > x]
        arr = quick_sort(less) + eq + quick_sort(higher)
    return arr


# arr = [5, 2, 8, 0, 1, 6, 2]
# print(quick_sort(arr))
