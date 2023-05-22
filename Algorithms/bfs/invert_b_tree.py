class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def __str__(self):
        return f'{self.value}(l: {self.left},r: {self.right})'


class AvlTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f'{self.root}'


tree = AvlTree()
nodes = [i for i in range(2, 9)]
nodess = [Node(i) for i in nodes]
tree.root = nodess[3]
tree.root.left, tree.root.left.left = nodess[1], nodess[0]
tree.root.left.right, tree.root.right = nodess[2], nodess[5]
tree.root.right.left, tree.root.right.right = nodess[4], nodess[6]
print(tree)


def invertTree(root: Node):
    if not root:
        return root
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root

invertTree(tree.root)
print(tree)



