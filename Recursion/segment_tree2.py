from collections import deque


class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None

    def __repr__(self):
        return f'{self.val}:   ({self.left}, {self.right})'


class SegmentTree:
    def __init__(self, arr: list, func):
        self.func = func
        self.arr = sorted(arr)
        self.height = 0
        self.head = self.build_tree(self.arr)

    def __repr__(self):
        return f'{self.head}'

    def append(self, elem):
        arr.append(elem)

    def pop(self):
        case1 = len(arr) % 2 == 0
        elem = arr.pop()

        if case1:
            visited = []
            root = self.head

            while root.right.val != elem:
                visited.append(root)
                root = root.right

            root.right = None
            visited.append(root)

            while visited:
                node = visited.pop()
                node.val -= elem

        else:
            self.head = self.head.left
            self.height -= 1

    def create_tl(self, arr, func):
        n = len(arr)
        if n % 2:
            arr = [arr[0] - 1] + arr
            n += 1
        tree_list = [None for _ in range(n * 2)]

        for i in range(n):
            tree_list[n + i] = arr[i]

        for i in range(n - 1, 0, -1):
            tree_list[i] = func(tree_list[i * 2], tree_list[i * 2 + 1])

        return tree_list[1:]

    def calculate(self, i, j):
        self.tree_list = self.create_tl(self.arr, self.func)
        summ = 0
        i += len(arr)
        j += len(arr)

        while i < j:
            if (i & 1) > 0:
                summ += self.tree_list[i]
                i += 1

            if (j & 1) > 0:
                j -= 1
                summ += self.tree_list[j]

            i //= 2
            j //= 2

        return summ

    def build_tree(self, arr):
        nodes = deque([Node(i) for i in arr])
        new_nodes = deque([])
        while True:
            while nodes:
                left = nodes.popleft()
                if not nodes:
                    new_node = Node(left.val)
                    new_node.left = left
                    new_nodes.append(new_node)
                else:
                    right = nodes.popleft()
                    new_node = Node(left.val + right.val)
                    new_node.left, new_node.right = left, right
                    new_nodes.append(new_node)
            self.height += 1

            if len(new_nodes) == 1:
                return new_nodes[0]
            else:
                nodes, new_nodes = new_nodes, deque([])


def summ(a, b):
    return a + b


if __name__ == '__main__':
    arr = [1, 2]
    st = SegmentTree(arr, summ)
    print(st)
    print(st.height)