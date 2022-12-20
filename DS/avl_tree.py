# TODO: REMOVE COMMENTS -> CREATE TESTS


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = self.get_height()

    def __repr__(self):
        return '{}(l:{}, r:{})'.format(self.value, self.left, self.right)

    def has_left_node(self):
        if self.left is None:
            return False
        else:
            return True

    def has_right_node(self):
        if self.right is None:
            return False
        else:
            return True

    def is_leaf(self):
        if self.left or self.right:
            return False
        else:
            return True

    def get_balance(self):
        if self.is_leaf():
            return 0
        elif self.has_right_node() is False:
            return -self.left.height - 1
        elif self.has_left_node() is False:
            return self.right.height + 1
        else:
            return self.right.height - self.left.height

    def get_height(self):
        if self.is_leaf():
            self.height = 0
        elif not self.has_left_node():
            self.height = self.right.get_height() + 1
        elif not self.has_right_node():
            self.height = self.left.get_height() + 1
        else:
            if self.left.get_height() > self.right.get_height():
                self.height = self.left.get_height() + 1
            else:
                self.height = self.right.get_height() + 1
        return self.height

    def left_rotation(self):
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        self.get_height()
        right_child.get_height()
        return right_child

    def right_rotation(self):
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        self.get_height()
        left_child.get_height()
        return left_child

    def is_parent(self):
        if self.left or self.right:
            return True
        else:
            return False

    def min_value_node(self):
        if self.left:
            left_child = self.left
            while left_child.left:
                left_child = left_child.left
            return left_child
        else:
            return self


class AvlTree:
    def __init__(self, elements=None):
        self.root = None
        self.size = 0
        if elements is not None:
            for elem in elements:
                self.insert(elem)

    def __str__(self, node=None):
        if self.is_empty():
            return f'this tree is empty.'
        else:
            return f'{self.root}'

    def is_empty(self):  # ++
        return self.root is None

    def height(self):  # ++
        if not self.root:
            return 0
        else:
            return self.root.get_height()

    def insert(self, item, node=None):  # ++
        if self.is_empty():
            self.root = Node(item)
            self.size += 1
            return

        if node is None:
            node = self.root
            self.size += 1

        if item == node.value:
            self.size -= 1
            return

        elif item < node.value:
            if node.has_left_node():
                added_subtree = self.insert(item, node.left)
                if added_subtree is not None:
                    node.left = added_subtree
            else:
                added_node = Node(item)
                node.left = added_node
        else:
            if node.has_right_node():
                added_subtree = self.insert(item, node.right)
                if added_subtree is not None:
                    node.right = added_subtree
            else:
                added_node = Node(item)
                node.right = added_node
        node.get_height()
        return self.balance_tree(node)

    def balance_tree(self, node):  # ++
        b_factor = node.get_balance()
        if b_factor in range(-1, 2):
            return None
        if b_factor < -1:
            if node.left.get_balance() < 0:
                new_root = node.right_rotation()
            else:
                node.left = node.left.left_rotation()
                new_root = node.right_rotation()
        else:
            if node.right.get_balance() > 0:
                new_root = node.left_rotation()
            else:
                node.right = node.right.right_rotation()
                new_root = node.left_rotation()
        if node is self.root:
            self.root = new_root
        return new_root

    def find_node_recursively(self, item, node):  # ++
        if node is None:
            return None
        elif item == node.value:
            return node
        elif item < node.value:
            return self.find_node_recursively(item, node.left)
        elif item > node.value:
            return self.find_node_recursively(item, node.right)

    def find_parent_node(self, item, node, parent=None):  # ++
        if node is None:
            return parent
        if item == node.value:
            return parent
        elif item < node.value:
            return self.find_parent_node(item, node=node.left, parent=node)
        elif item > node.value:
            return self.find_parent_node(item, node=node.right, parent=node)

    def traverse_in_order(self, node, arr):
        if arr is None:
            arr = []
        if node:
            self.traverse_in_order(node.left, arr)
            arr.append(node.value)
            self.traverse_in_order(node.right, arr)
        return arr

    def traverse_pre_order(self, node, arr):
        if arr is None:
            arr = []
        if node:
            arr.append(node.value)
            if node.left:
                self.traverse_pre_order(node.left, arr)
            if node.right:
                self.traverse_pre_order(node.right, arr)
        return arr

    def traverse_post_order(self, node, arr):
        if arr is None:
            arr = []
        if node:
            self.traverse_post_order(node.left, arr)
            self.traverse_post_order(node.right, arr)
            arr.append(node.value)
        return arr

    def delete_item(self, root, item):
        if root is None:
            return root
        if item < root.value:
            root.left = self.delete_item(root.left, item)
            self.balance_tree(root)
            return root
        elif item > root.value:
            root.right = self.delete_item(root.right, item)
            self.balance_tree(root)
            return root
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            temp = root.right
            root = None
            self.balance_tree(temp)
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            self.balance_tree(temp)
            return temp
        s_parent = root
        s = root.right
        while s.left is not None:
            s_parent = s
            s = s.left
        if s_parent != root:
            s_parent.left = s.right
        else:
            s_parent.right = s.right
        root.value = s.value
        self.balance_tree(root)
        return root

# Additional functions (not used mostly):

# def has(self, item):   # +
#     node = self.find_node_recursively(item, self.root)
#     return node is not None

# def find_node_iteratively(self, item):  # +
#     node = self.root
#     while node is not None:
#         if item == node.value:
#             return node
#         elif item < node.value:
#             node = node.left
#         elif item > node.value:
#             node = node.right
#     return None
#
# def find_parent_node_iteratively(self, item):  # +
#     node = self.root
#     parent = None
#     while node is not None:
#         if node.value == item:
#             return parent
#         elif item < node.value:
#             parent = node
#             node = node.left
#         elif item > node.value:
#             parent = node
#             node = node.right
#     return parent


# Old
# if not node:
#     node = self.root
# if node.value == item:
#     if node.is_leaf():
#         node = None
#         return
#     elif node.left and not node.right:
#         node = node.left
#         return
#     elif node.right and not node.left:
#         node = node.right
#         return
#     else:
#         if node.right.is_parent():
#             anc = node.right.min_value_node()
#             anc_val = anc.value
#             left_sub, right_sub = node.left, node.right
#             node = anc
#             node.left, node.right = left_sub, right_sub
#             self.delete_item(anc_val, right_sub)
#             return
#         else:
#             subtree = node.left
#             node = node.right
#             node.left = subtree
#             return
# else:
#     parent = self.find_parent_node(item, node)
#     if parent.left.value == item:
#         l_node = parent.left
#         if l_node.is_leaf():
#             parent.left = None
#         else:
#             if l_node.left and not l_node.right:
#                 l_node = l_node.left
#             elif l_node.right and not l_node.left:
#                 l_node = l_node.right
#             else:
#                 if l_node.right.is_leaf():
#                     sub = l_node.left
#                     l_node = l_node.right
#                     l_node.left = sub
#                 elif
