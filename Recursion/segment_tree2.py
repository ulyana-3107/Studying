from collections import deque


class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None

    def __repr__(self):
        return f'{self.val}: ({self.left}, {self.right})'


class SegmentTree:
    def __init__(self, arr: list):
        self.tree_list = self.create_tl(arr)
        self.head = self.build_tree(self.tree_list)

    def __repr__(self):
        return f'{self.head}'

    def append(self, elem):
        arr.append(elem)
        self.tree_list = self.create_tl(arr)
        self.head = self.build_tree(self.tree_list)

    def pop(self):
        arr.pop()
        self.tree_list = self.create_tl(arr)
        self.head = self.build_tree(self.tree_list)

    def calculate(self, i, j):
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


    def build_tree(self, tree_list):
        queue = deque([(Node(tree_list[0]), 0)])
        head = None

        while queue:
            elem, index = queue.popleft()
            if index == 0:
                head = elem
            i1, i2 = index * 2 + 1, index * 2 + 2
            if i1 >= len(tree_list) or i2 >= len(tree_list):
                break
            el1, el2 = Node(tree_list[i1]), Node(tree_list[i2])
            elem.left, elem.right = el1, el2
            queue.extend([(el1, i1), (el2, i2)])

        return head

    def create_tl(self, arr):
        n = len(arr)
        if n % 2:
            arr = [arr[0] - 1] + arr
            n += 1
        tree_list = [None for _ in range(n * 2)]

        for i in range(n):
            tree_list[n + i] = arr[i]

        for i in range(n - 1, 0, -1):
            tree_list[i] = tree_list[i * 2] + tree_list[i * 2 + 1]

        return tree_list[1:]


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    st = SegmentTree(arr)
    print(st)
    st.pop()
    print(st)
