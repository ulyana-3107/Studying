# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


def reverse_list(lst: list) -> list:
    n = len(lst)
    if n < 2:
        return lst
    for i in range(n//2):
        j = -(i + 1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst


# arr1, arr2, arr3 = [0, 1, 2, 3], [1, 2], [9, 8, 7, 6, 5, 4]
# name = 'arr'
# for i in range(1, 4):
#     print(reverse_list(eval(name + str(i))))
class Node:
    def __init__(self, val):
        self.val, self.next = val, None


def solution1(l1: Node, l2: Node) -> int:
    a, b = [], []
    n1, n2 = l1, l2
    while n1.next:
        a.append(n1.val)
        n1 = n1.next
    a.append(n1.val)
    while n2.next:
        b.append(n2.val)
        n2 = n2.next
    b.append(n2.val)
    l_a, l_b, res, rest = len(a), len(b), [], 0
    if l_a > 1 and len(set(a)) == l_a:
        for i in range(l_a // 2):
            j = -(i + 1)
            a[i], a[j] = a[j], a[i]
    if l_b > 1 and len(set(b)) == l_b:
        for i in range(l_b // 2):
            j = -(i + 1)
            b[i], b[j] = b[j], b[i]
    if l_a > l_b:
        a, b = b, a
    for i in range(len(a)):
        summ = str(a[i] + b[i] + rest)
        if len(summ) > 1:
            res.append(int(summ[-1]))
            rest = int(summ[: -1])
        else:
            res.append(int(summ))
            rest = 0
    if abs(l_b - l_a) > 0:
        start = -abs((l_b - l_a))
        end = 0
        for i in range(start, end):
            summ = str(rest + b[i])
            if len(summ) > 1:
                res.append(int(summ[-1]))
                rest = int(summ[: -1])
            else:
                res.append(int(summ))
    if rest != 0:
        res.append(rest)
    return res


# l1, l2 = [2, 4, 3], [5, 6, 4]
# l1, l2 = [0], [0]
l1, l2 = [9 for _ in range(7)], [9 for _ in range(4)]
n1, n2 = [Node(i) for i in l1], [Node(i) for i in l2]
h1, h2 = n1[0], n2[0]
for i in range(len(n1) - 1):
    n1[i].next = n1[i + 1]
for i in range(len(n2) - 1):
    n2[i].next = n2[i + 1]


print(solution1(h1, h2))
