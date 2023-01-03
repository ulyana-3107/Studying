

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return '{}(l:{}, r:{})'.format(self.value, self.left, self.right)

    def is_leaf(self):
        return not self.left and not self.right


class AvlTree:
    def __init__(self, elems=None):
        self.root = None
        if elems:
            elems.sort()
            self.root = self.tree_build(elems)
        else:
            self.root = None

    def __str__(self, node=None):
        if self.is_empty():
            return f'this tree is empty.'
        else:
            return f'{self.root}'

    def is_balanced(self) -> bool:
        return abs(self.node_height(self.root.left) - self.node_height(self.root.right)) in range(-1, 2)

    def small_tree_build(self, elements):
        l_ = len(elements)
        node = Node(elements[len(elements)//2])
        if l_ == 2:
            node.left = Node(elements[0])
        elif l_ == 3:
            node.left, node.right = Node(elements[0]), Node(elements[2])
        return node

    def tree_build(self, elements):
        l_ = len(elements)
        if l_ in range(1, 3 + 1):
            node = self.small_tree_build(elements)
            return node
        else:
            node, l_side, r_side = Node(elements[l_//2]), elements[:l_//2], elements[l_//2+1:]
            node.left, node.right = self.tree_build(l_side), self.tree_build(r_side)
            return node

    def is_empty(self):
        return not self.root

    def insert(self, item, node=None):
        if self.is_empty():
            self.root = Node(item)
            return
        if not node:
            node = self.root
        if item == node.value:
            return
        elif item < node.value:
            if node.left:
                self.insert(item, node.left)
            else:
                node.left = Node(item)
                parent = self.find_parent_node(node.value)
                if not abs(parent.node_height(self.root.left) - parent.node_height(self.root.right)) in range(-1, 2):
                    self.balance_tree(parent)
        elif item > node.value:
            if node.right:
                self.insert(item, node.right)
            else:
                node.right = Node(item)
                parent = self.find_parent_node(node.value)
                if not abs(parent.node_height(self.root.left) - parent.node_height(self.root.right)) in range(-1, 2):
                    self.balance_tree(parent)

    def balance_tree(self, node: Node):
        pass



    def find_node_by_item(self, item):
        root = self.root
        if root.value == item:
            return root
        while True:
            if item == root.value:
                return root
            if item < root.value:
                root = root.left
            else:
                root = root.right

    def find_parent_node(self, item):
        if item == self.root.value:
            return None
        if self.root.left == item or self.root.right == item:
            return self.root
        parent = self.root
        if item < parent.value:
            child = parent.left
        else:
            child = parent.right
        while True:
            if child.value == item:
                break
            parent = child
            if item < child.value:
                child = child.left
            else:
                child = child.right
        return parent

    def lnr(self, node, arr):
        if node:
            self.lnr(node.left, arr)
            arr.append(node)
            self.lnr(node.right, arr)
        return arr

    def nlr(self, node, arr):
        if node:
            arr.append(node)
            self.nlr(node.left, arr)
            self.nlr(node.right, arr)
        return arr

    def lrn(self, node, arr):
        if node:
            self.lrn(node.left, arr)
            self.lrn(node.right, arr)
            arr.append(node)
        return arr

    def delete_leaf(self, node, leaf):
        if node.value == leaf.value:
            node = None
            return
        else:
            parent = node
            if leaf.value < node.value:
                child = node.left
            else:
                child = node.right
            while True:
                if child.value == leaf.value:
                    if parent.right == child:
                        parent.right = None
                    else:
                        parent.left = None
                    return
                parent = child
                if leaf.value < child.value:
                    child = child.left
                else:
                    child = child.right

    def find_pr(self, node):
        while node.right:
            node = node.right
        return node

    def del_by_item(self, item, node=None):
        parent = self.find_parent_node(item)
        if not node:
            item_node = self.find_node_by_item(item)
        else:
            item_node = node
        if not parent:  # it means that the item to be deleted is root
            a, b, c = item_node.is_leaf(), item_node.left and item_node.right, item_node.left or item_node.right
            if a:
                self.root = None
            elif b:
                pr = self.find_pr(item_node.left)
                pr_val = pr.value
                l_side, r_side = item_node.left, item_node.right
                self.delete_leaf(l_side, pr)
                self.root = Node(pr_val)
                self.root.left, self.root.right = l_side, r_side
            else:
                if item_node.left:
                    self.root = item_node.left
                else:
                    self.root = item_node.right
            return
        else:
            parent_ = self.find_parent_node(parent.value)
            if not parent_:
                parent_ = parent
            a, b, c = item_node.is_leaf(), item_node.left and item_node.right, item_node.left or item_node.right
            if a:
                if parent.left == item_node:
                    parent.left = None
                else:
                    parent.right = None
            elif b:
                pr = self.find_pr(item_node.left)
                pr_val = pr.value
                l_side, r_side = item_node.left, item_node.right
                self.delete_leaf(l_side, pr)
                if parent.left == item_node:
                    parent.left = Node(pr_val)
                    parent.left.left, parent.left.right = l_side, r_side
                else:
                    parent.right = Node(pr_val)
                    parent.right.left, parent.right.right = l_side, r_side
            else:
                if item_node.left:
                    if parent.left == item_node:
                        parent.left = item_node.left
                    else:
                        parent.right = item_node.left
                else:
                    if parent.right == item_node:
                        parent.right = item_node.right
                    else:
                        parent.left = item_node.right
            if not abs(self.node_height(parent_.left) - self.node_height(parent_.right)) in range(-1, 2):
                self.balance_tree(parent_)
            return

    def node_height(self, node):
        if not node:
            return 0
        return max(self.node_height(node.left), self.node_height(node.right)) + 1


elements = [1, 2, 3, 4, 5]
tree = AvlTree(elements)
print(tree)
print(tree.node_height(tree.root))


# def height(self):  # ++
    #     if not self.root:
    #         return 0
    #     else:
    #         return self.root.height


# def is_parent(self):
    #     if self.left or self.right:
    #         return True
    #     else:
    #         return False


# def get_height(self):
    #     if self.is_leaf():
    #         self.height = 0
    #     elif not self.has_left_node():
    #         self.height = self.right.get_height() + 1
    #     elif not self.has_right_node():
    #         self.height = self.left.get_height() + 1
    #     else:
    #         if self.left.get_height() > self.right.get_height():
    #             self.height = self.left.get_height() + 1
    #         else:
    #             self.height = self.right.get_height() + 1
    #     return self.height


# def has_left_node(self):
#     return self.left is not None
#
# def has_right_node(self):
#     return self.right is not None

# def get_balance(self):
#     if self.is_leaf():
#         return 0
#     elif self.has_right_node() is False:
#         return -self.left.height - 1
#     elif self.has_left_node() is False:
#         return self.right.height + 1
#     else:
#         return self.right.height - self.left.height

# def left_rotation(self):
#     right_child = self.right
#     self.right = right_child.left
#     right_child.left = self
#     self.get_height()
#     right_child.get_height()
#     return right_child
#
# def right_rotation(self):
#     left_child = self.left
#     self.left = left_child.right
#     left_child.right = self
#     self.get_height()
#     left_child.get_height()
#     return left_child
#
# def min_value_node(self):
#     if self.left:
#         left_child = self.left
#         while left_child.left:
#             left_child = left_child.left
#         return left_child
#     else:
#         return self

# def balance_tree(self, node):
#     b_factor = node.get_balance()
#     if b_factor in range(-1, 2):
#         return None
#     if b_factor < -1:
#         if node.left.get_balance() < 0:
#             new_root = node.right_rotation()
#         else:
#             node.left = node.left.left_rotation()
#             new_root = node.right_rotation()
#     else:
#         if node.right.get_balance() > 0:
#             new_root = node.left_rotation()
#         else:
#             node.right = node.right.right_rotation()
#             new_root = node.left_rotation()
#     if node is self.root:
#         self.root = new_root
#     return new_root