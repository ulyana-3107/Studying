from __future__ import annotations
from collections import deque


# !!! если вызывается ф-я add_heights() - обязательно вызывается ф-я add_parents()
# TODO: добавить балансировку после вставки


# Требования по методам:
# * вставка и удаление по значению (O(logN))
# * создание дерева из любого списка (O(NlogN)) - N*logN -Done
# * обходы дерева (3 штуки за O(N) каждый)  - Done
# * найти элемент по значению (O(logN)) - Done
# * высота ((O(logN)) - Done


class Node(object):
    def __init__(self, value):
        self.par = None
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
        if elems:
            elems.sort()  # O(NlogN)
            self.root = self.tree_build(elems)  # O(logN)
        else:
            self.root = None  # O(1)
        self.parents = None
        self.heights = None
    # O(NlogN)*2 -> O(NlogN)

    def __str__(self, node=None):
        if self.is_empty():
            return f'this tree is empty.'
        else:
            return f'{self.root}'

    def additional_params(self, parents: bool, heights: bool) -> None:
        if parents and heights:
            self.add_parents(self.root)
            self.add_heights()
        elif parents:
            self.add_parents(self.root)
        else:
            self.add_heights()

    def height(self, node: Node = None) -> int:
        if self.heights is None:
            self.add_heights()
        return self.heights[node]

    # Additional function to check if parents are defined right.
    def show_parents(self):
        if not self.parents:
            self.add_parents(self.root)
        print('parents:')
        for k, v in self.parents.items():
            print(k.value, ':', v.value)

    def show_heights(self):
        if not self.heights:
            self.add_heights()
        print('heights:')
        for k, v in self.heights.items():
            print(k.value, ':', v)

    def is_balanced(self) -> bool:
        if not self.heights:
            self.additional_params(False, True)
        a = self.heights[self.root.left] if self.root.left else 0
        b = self.heights[self.root.right] if self.root.right else 0
        return abs(a - b) in range(-1, 2)

    def deepestNode(self, root):
        if root == None:
            return 0
        q = deque()
        q.append(root)
        node = None
        while len(q) != 0:
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return node

    # def add_nodes_depth(self):
    #     pass

    # add balance tracking + balancing if needed
    def insert_by_item(self, item: int) -> None:
        node, new_node = self.root, None
        while True:
            if node.value == item:
                break
            elif node.value < item:
                if node.right:
                    node = node.right
                else:
                    new_node = Node(item)
                    node.right = new_node
                    if self.parents is not None:
                        new_node.par = node
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    new_node = Node(item)
                    node.left = new_node
                    if self.parents is not None:
                        new_node.par = node
                    break
        if new_node:
            if not self.parents and not self.heights:
                self.additional_params(True, True)
            elif not self.parents and self.heights:
                self.add_parents(self.root)
            elif not self.heights:
                self.add_heights()
            else:
                self.update_heights()

    def del_by_item(self, item: int) -> None:
        if not self.heights:
            if not self.parents:
                self.additional_params(True, True)
            self.additional_params(False, True)
        node_del = self.find_node_by_item(item)
        if node_del.left and not node_del.right:
            if node_del.par:
                if node_del.par.left == node_del:
                    node_del.par.left = node_del.left
                else:
                    node_del.par.right = node_del.left
                self.update_heights(node_del.par)
            else:
                self.root = node_del.left
        elif node_del.right and not node_del.left:
            if node_del.par:
                if node_del.par.right == node_del:
                    node_del.par.right = node_del.right
                else:
                    node_del.par.left = node_del.right
                self.update_heights(node_del.par)
            else:
                self.root = node_del.right
        elif not any([node_del.right, node_del.left]):
            if not node_del.par:
                self.root = None
            else:
                if node_del.par.left == node_del:
                    node_del.par.left = None
                else:
                    node_del.par.right = None
                self.update_heights(node_del.par)
        # нужно еще добавить проверку на то, что у родителя удаляемого нода есть ли родители - если да - у всех поменять высоты
        # else:
        #     if node_del.par:
        #         left_son, right_son = node_del.par.left == node_del, node_del.par.right == node_del
        #         left_h, right_h = node_del.left.height, node_del.right.height
        #         if left_h >= right_h:
        #             a, b, c = node_del.left, node_del.left.left, node_del.right
        #         else:
        #             a, b, c = node_del.right, node_del.right.right, node_del.left
        #         if left_son:
        #             node_del.par.left = a
        #             node_del.par.left.left = b
        #             node_del.par.right = c
        #         else:
        #             node_del.par.right = a
        #             node_del.par.right.left = b
        #             node_del.par.right.right = c
        #     else:
        #         pass





    #  эта функция для создания ссылок на родителя у каждого нода
    def add_parents(self, root: Node) -> None:
        visited, parents = set(), {}
        fifo = [root]
        while fifo:
            v = fifo.pop()
            visited.add(v)
            if v.left is not None:
                v.left.par = v
                parents[v.left] = v
                fifo.append(v.left)
            if v.right is not None:
                v.right.par = v
                parents[v.right] = v
                fifo.append(v.right)
        self.parents = parents

    def add_heights(self) -> None:
        if not self.parents:
            self.add_parents(self.root)
        arr, heights = [], {}
        if self.root.left:
            arr.append(self.root.left)
        if self.root.right:
            arr.append(self.root.right)
        for node in arr:
            leaf, h = self.deepestNode(node), 1
            while leaf not in (self.root.left, self.root.right):
                leaf.par.height = h
                heights[leaf.par] = h
                h += 1
                leaf = leaf.par
        left_height, right_height = None, None
        if self.root.left:
            left_height = self.root.left.height
        if self.root.right:
            right_height = self.root.right.height
        if left_height and right_height:
            self.root.height = max(left_height, right_height) + 1
            heights[self.root] = max(left_height, right_height) + 1
        elif left_height:
            self.root.height = left_height + 1
            heights[self.root] = left_height + 1
        else:
            self.root.height = right_height + 1
            heights[self.root] = right_height + 1
        self.heights = heights

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
        if l_ in range(1, 4):
            node = self.small_tree_build(elements)
            return node
        else:
            node, l_side, r_side = Node(elements[l_//2]), elements[:l_//2], elements[l_//2+1:]
            node.left, node.right = self.tree_build(l_side), self.tree_build(r_side)
            return node

    def is_empty(self):
        return not self.root

    #?
    def balance_tree(self, node: Node):
        new = node
        while node.par:
            node = node.par
            l_h, r_h = 0, 0
            if node.left is not None:
                l_h = node.left.height
            if node.right is not None:
                r_h = node.right.height
            bf = l_h - r_h
            if bf not in range(-1, 2):
                first_l, first_r, second_l, second_r = False, False, False, False
                if node.value > new.value:
                    first_l = True
                else:
                    first_r = True
                if first_l:
                    if node.left.value > new.value:
                        second_l = True
                    else:
                        second_r = True
                else:
                    if node.right.value > new.value:
                        second_l = True
                    else:
                        second_r = True
                parent = node.par
                if first_l and second_l:
                    self.ll_rotation(node, parent)
                elif first_r and second_r:
                    self.rr_rotation(node, parent)
                elif first_r and second_l:
                    self.rl_rotation(node, parent)
                else:
                    self.lr_rotation(node, parent)
    #?
    def ll_rotation(self, critical_node: Node, parent: Node):
        left = critical_node.left
        a, b, c = left.left, left.right, critical_node.right
        a_, b_ = critical_node.left, critical_node.right
        a_.left = a
        b_.left, b_.right = b, c
        a_.right = b_
        if not parent:
            self.root = a_
        else:
            if parent.left == critical_node:
                parent.left = a_
            else:
                parent.right = a_
    #?
    def rr_rotation(self, critical_node: Node, parent: Node):
        right = critical_node.right
        a, b, c = critical_node.left, right.left, right.right
        a_, b_ = critical_node.right, critical_node
        b_.left, b_.right = a, b
        a_.left, a_.right = b_, c
        if not parent:
            self.root = a_
        else:
            if parent.left == critical_node:
                parent.left = a_
            else:
                parent.right = a_
    #?
    def lr_rotation(self, critical_node: Node, parent: Node):
        left = critical_node.left
        a, b, c, d = left.left, left.right.left, left.right.right, critical_node.right
        a_, b_, c_ = left.right, critical_node.left, critical_node
        b_.left, b_.right = a, b
        c_.left, c_.right = c, d
        a_.left, a_.right = b_, c_
        if not parent:
            self.root = a_
        else:
            if parent.left == critical_node:
                parent.left = a_
            else:
                parent.right = a_
    #?
    def rl_rotation(self, critical_node: Node, parent: Node):
        right = critical_node.right
        a, b, c, d = critical_node.left, right.left.left, right.left.right, right.right
        a_, b_, c_ = right.left, critical_node.right, critical_node
        b_.left, b_.right = a, b
        c_.left, c_.right = c, d
        a_.left, a_.right = b_, c_
        if not parent:
            self.root = a_
        else:
            if parent.left == critical_node:
                parent.left = a_
            else:
                parent.right = a_

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


elements = [1, 2, 3]
tree = AvlTree(elements)
print(tree)
tree.show_heights()
tree.del_by_item(3)
print(tree)
tree.show_heights()