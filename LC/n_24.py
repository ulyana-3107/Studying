# task: в связном списке из четного количества элементов поменять местами все близлежащие, например:
# [1, 2, 3, 4, 5, 6] -> [2, 1, 4, 3, 6, 5]
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
# the values in the list's nodes (i.e., only nodes themselves may be changed.)


def solution1(arr: list) -> list:
    n, i = len(arr), 1
    while i < n:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i += 2
    return arr


class Node:
    def __init__(self, val=0):
        self.val, self.next, self.prev = val, None, None

    def __str__(self):
        return f'{self.val} -> {self.next}'


lst = [1, 2, 3, 4, 5, 6]
nodes = [Node(el) for el in lst]
i = 0
while i != len(lst) - 1:
    nodes[i].next = nodes[i + 1]
    if i > 0:
        nodes[i + 1].prev = nodes[i]
    i += 1


def solution2(head: Node) -> Node:
    prev, cur = head, head.next
    start = prev
    while True:
        if not cur.next and not prev.prev:
            prev.next, prev.prev = None, cur
            cur.next, cur.prev = prev, None
            return cur
        elif not cur.next:
            prev.prev.next = cur
            cur.prev = prev.prev
            cur.next = prev
            prev.prev = cur
            prev.next = None
            return start.prev
        elif not prev.prev:
            n = cur.next
            prev.next = n
            n.prev = prev
            cur.prev = None
            cur.next = prev
            prev.prev = cur
            prev, cur = n, n.next
        else:
            p = prev.prev
            n = cur.next
            nn = n.next
            cur.next = prev
            prev.prev = cur
            cur.prev = p
            p.next = cur
            prev.next = n
            n.prev = prev
            prev, cur = n, nn


# unknown solution
def solution3(head: Node) -> Node:
    if not head or not head.next:
        return head
    a = b = head
    c = d = Node()
    z = None
    while head and head.next:
        x = head.next
        head.next = z
        z = head
        head = x
        y = head.next
        head.next = z
        z = head
        head = y
        c.next = z
        c = c.next.next
        z = None
    if head:
        c.next = head
    return d.next


head = nodes[0]
print(head)
print(solution3(head))