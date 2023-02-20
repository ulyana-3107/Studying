class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        currentOdd = head
        count = 2
        node = head
        pre = node
        node = node.next
        while node is not None:  # O(N)
            if count % 2 == 0:
                pre = node
                node = node.next
            else:
                next = node.next
                pre.next = next
                temp = currentOdd.next
                currentOdd.next = node
                node.next = temp
                currentOdd = node
                node = next
            count += 1
        return head
# O(1) + max(O(1), O(N) * (O(1) + max(O(1), O(1))) -> O(1) + O(N) -> O(N)


def first_approach(head: list) -> list:
    n, new_head = len(head), list()
    n2 = n//2
    if n % 2:
        n1 = n2 + 1
    else:
        n1 = n2
    i, start = 0, 0
    while i != n1:  # O(N//2) -> O(N)
        new_head.append(head[start])
        start += 2
        i += 1
    i, start = 0, 1
    while i != n2:  # O(N//2) -> O(N)
        new_head.append(head[start])
        start += 2
        i += 1
    return new_head
# O(N) + O(N) -> O(2N) -> O(N).


def second_approach(head: list) -> list:
    i, f, s = 0, [], []
    for elem in head:  # O(N)
        if i % 2:
            s.append(elem)
        else:
            f.append(elem)
        i += 1
    return f + s  # O(N//2) + O(N//2) -> O(N) + O(N) ->  O(2N) -> O(N)
# O(N) + O(N) -> O(2N) -> O(N).


def third_odd_approach(head: list) -> list:
    new_head, i = [[], []], 0
    for elem in head:  # O(N)
        if i % 2:
            new_head[1].append(elem)
        else:
            new_head[0].append(elem)
        i += 1
    return [i for row in new_head for i in row]  # O(N)
# O(N) + O(N) -> O(2N) -> O(N)


# arr = [1, 2, 3, 4, 5]
# print(first_approach(arr))
# print(second_approach(arr))
# print(third_odd_approach(arr))


class Node(object):
    def __init__(self, v,  next=None):
        self.value, self.next = v, next
    # O(1)

    def __repr__(self) -> str:
        return f'{self.value} -> {self.next}'
    # O(1)


class LinkedList(object):
    def __init__(self, arr: list):
        if not len(arr):
            self.root = None
        else:
            self.root = self.build_list(arr)  # O(N), where N - len(arr)
            self.nodes_list = self.nodes_lst(arr)  # O(N)
    # O(1) + max(O(1), O(N)) -> O(1) + O(N) -> O(N)

    def __repr__(self) -> str:
        return f'{self.root}'
    # O(1)

    def nodes_lst(self, arr: list) -> list:
        lst = [Node(i) for i in arr]
        return lst
    # O(len(arr)) -> if len(arr) is N -> O(N)

    def build_list(self, arr: list) -> Node:
        if len(arr) == 1:
            return Node(arr[0])
        node_list = [Node(el) for el in arr]  # O(N)
        i = 0
        while i != len(node_list) - 1:  # O(N - 1) -> O(N)
            node_list[i].next = node_list[i + 1]
            i += 1
        return node_list[0]
    # O(1) + max(O(1), (O(N) + O(N)) -> O(1) + O(2N) -> O(N)

    def rebuild_1(self, nodes: list) -> Node:
        f, s, i =[], [], 0  # O(1)
        for i in range(len(nodes)):  # O(len(nodes)) -> if len(nodes) is N -> O(N)
            if i % 2:
                s.append(nodes[i])
            else:
                f.append(nodes[i])
        for i in range(len(f) - 1):
            f[i].next = f[i + 1]
        for i in range(len(s) - 1):
            s[i].next = s[i + 1]
        try:
            f[-1].next = s[0]
        except IndexError:
            pass
        return f[0]
# 119 - 123:  O(N) * (O(1) + max(O(1), O(1)) -> O(N) * O(1) -> O(N)
# 124 - 127:  O(N - 1) + O(N - 1) -> O(N) + O(N) -> O(2N) -> O(N)
# 128 - 232:  O(1)
# 118 - 132:  O(1) + O(N) + O(N) + O(1) -> O(N).


# ll = LinkedList([1, 2, 3, 4, 5])
# print(ll)
# print(ll.rebuild_1(ll.nodes_list))










