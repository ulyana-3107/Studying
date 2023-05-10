from collections import deque


# Самому присваивать ноды нельзя - только если создание через список или вставка через функцию.

# вставка и удаление по значению (O(logn))  - вставка - Done. удаление -
# создание дерева из любого списка (O(nlogn))  - Done
# обходы дерева (3 штуки за O(n) каждый) - Done
# найти элемент по значению (O(logn)) - Done
# высота ((O(logn)) - Done


class Node(object):
    def __init__(self, value):
        self.par = None
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return '{}(l:{}, r:{})'.format(self.value, self.left, self.right)

    def is_leaf(self):
        return not self.left and not self.right


class AvlTree:
    def __init__(self, elems=None):
        if elems:
            elems.sort()
            self.root = self.tree_build(elems)
        else:
            self.root = None
        self.parents, self.heights = {}, {}

    def __str__(self, node=None):
        if self.is_empty():
            return f'this tree is empty.'
        else:
            return f'{self.root}'

    def delete_by_item(self, root: Node, item: int):
        node = root
        node_found, child_num = None, 2

        while node:
            if node.value == item:
                node_found = node
                break
            elif node.value > item:
                node = node.left
            else:
                node = node.right

        if not node_found.right or not node_found.left:
            child_num -= 1
        elif not node_found.right and not node_found.left:
            child_num -= 1

        # leaf case
        if child_num == 0:

            parent = node_found.par

            if not parent:
                self.root = None
            else:
                if parent.left == node_found:
                    parent.left = None
                    parent.height -= int(bool(parent.right is not None))
                    self.heights[parent] = parent.height
                else:
                    parent.right = None
                    parent.height -= int(bool(parent.left is not None))
                    self.heights[parent] = parent.height

                self.update_heights(parent, 2)

        # node to be deleted has 1 child tree
        elif child_num == 1:
            parent = node_found.par
            del self.heights[node_found]

            if node_found.left is not None:
                if parent:
                    if parent.left == node_found:
                        parent.left = node_found.left
                        self.parents[parent.left] = parent.left.par = parent
                        self.update_heights(parent.left, 2)
                    else:
                        parent.right = node_found.left
                        self.parents[parent.right] = parent.right.par = parent
                        self.update_heights(parent.right, 2)

                else:
                    self.root = node_found.left
                    node_found.left.par = None
                    del self.parents[node_found.left]
            else:
                if parent:
                    if parent.left == node_found:
                        parent.left = node_found.right
                        self.parents[parent.left] = parent.left.par = parent
                        self.update_heights(parent.left, 2)
                    else:
                        parent.right = node_found.right
                        self.parents[parent.right] = parent.right.par = parent
                        self.update_heights(parent.right, 2)

                else:
                    self.root = node_found.right
                    node_found.right.par = None
                    del self.parents[node_found.right]

        else:
            # left and right childs
            parent = node_found.par
            new_part = None
            node_link_to_update = None

            lr_h = node_found.left.right.height if node_found.left.right else 0
            rl_h = node_found.right.left.height if node_found.right.left else 0

            if lr_h + rl_h == 0:
                if node_found.left.height >= node_found.right.height:

                    node_found.left.right = node_found.right
                    self.parents[node_found.right] = node_found.right.par = node_found.left
                    new_part = node_found.left

                    h_l = node_found.left.left.height if node_found.left.left else 0
                    h_r = node_found.right.height

                    if h_r > h_l:
                        self.heights[new_part] = new_part.height = h_r + 1
                else:
                    node_found.right.left = node_found.left
                    self.parents[node_found.left] = node_found.left.par = node_found.right
                    new_part = node_found.right

                    l_h = node_found.left.height
                    r_h = node_found.right.right.height if node_found.right.right else 0

                    if l_h > r_h:
                        self.heights[new_part] = new_part.height = l_h + 1

            else:

                if lr_h >= rl_h:
                    repl_tree = node_found.left.right
                    pr = self.find_pr(repl_tree)
                    if pr == repl_tree:
                        node_found.left.right = None
                        node_link_to_update = node_found.left
                    else:
                        par_pr = pr.par
                        par_pr.right = None
                        node_link_to_update = par_pr
                else:
                    repl_tree = node_found.right.left
                    pr = self.find_pr(repl_tree)
                    if pr == repl_tree:
                        node_found.right.left = None
                        node_link_to_update = node_found.right
                    else:
                        par_pr = pr.par
                        par_pr.right = None
                        node_link_to_update = par_pr

                del self.parents[pr]
                pr.left, pr.right = node_found.left, node_found.right
                node_found.left.par = node_found.right.par = pr
                self.parents[node_found.left] = self.parents[node_found.right] = pr
                new_part = pr

            if parent:
                new_part.par = parent
                self.parents[new_part] = parent
                if parent.left == node_found:
                    parent.left = new_part
                else:
                    parent.right = new_part
            else:
                new_part.par = None
                self.root = new_part

            if node_link_to_update:
                self.update_heights(node_link_to_update, 3)

        del self.parents[node_found]

    def update_heights(self, node: Node, mode: int):
        """
        Function to update heights in a tree after changing it
        :param node: new_inserted node/
        :param mode: 1 - update after insertion, 2 - after deletion
        :return: None
        """
        if mode == 1:
            parent, child = node.par, node

            while parent != self.root:

                if parent.left == child:
                    if not parent.right:
                        parent.height += 1
                        self.heights[parent] = parent.height
                        parent, child = parent.par, parent
                    else:
                        parent.height = max(parent.left.height, parent.right.height) + 1
                        self.heights[parent] = parent.height
                        parent, child = parent.par, parent
                else:
                    if not parent.left:
                        parent.height += 1
                        self.heights[parent] = parent.height
                        parent, child = parent.par, parent
                    else:
                        parent.height = max(parent.left.height, parent.right.height) + 1
                        self.heights[parent] = parent.height
                        parent, child = parent.par, parent

            if parent.left == child:
                if not parent.right:
                    parent.height += 1
                    self.heights[parent] = parent.height
                else:
                    self.heights[parent] = parent.height = max(parent.left.height, parent.right.height) + 1
            else:
                if not parent.left:
                    parent.height += 1
                    self.heights[parent] = parent.height
                else:
                    self.heights[parent] = parent.height = max(parent.left.height, parent.right.height) + 1

        elif mode == 2:

            start = node
            parent = start.par
            s = False

            while parent != self.root:
                curr_height = parent.height
                l_h = parent.left.height if parent.left else 0
                r_h = parent.right.height if parent.right else 0
                new_height = max(l_h, r_h) + 1
                if curr_height == new_height:
                    s = True
                    break
                else:
                    parent.height = new_height
                    self.heights[parent] = new_height
                    parent = parent.par
            if not s:
                l_h = parent.left.height if parent.left else 0
                r_h = parent.right.height if parent.right else 0
                new_height = max(l_h, r_h) + 1
                curr_height = parent.height
                if curr_height != new_height:
                    parent.height = new_height
                    self.heights[parent] = new_height

        else:
            start = node
            parent = start.par

            while parent != self.root:
                self.change_height(parent, self.heights)
                parent = parent.par

            self.change_height(parent, self.heights)

    def change_height(self, node: Node, heights: dict) -> None:
        l_h = node.left.height if node.left else 0
        r_h = node.right.height if node.right else 0
        node.height = max(l_h, r_h) + 1
        heights[node] = node.height

    # Эта функция рассчитана на то, что дерево сбалансированно
    def add_heights(self, root: Node, sub_tree: bool=False):
        if not sub_tree:
            self.heights = {}
        dl, dr = self.find_deepest_node(root.left), self.find_deepest_node(root.right)

        if dl is not None:
            h = 2
            if dl == root.left:
                self.heights[root] = h
            else:
                parent = dl.par
                while parent != root:
                    parent.height = h
                    self.heights[parent] = h
                    dl, parent = parent, parent.par
                    h += 1

        if dr is not None:
            h = 2
            if dr == root.right:
                self.heights[root] = h
            else:
                parent = dr.par
                while parent != root:
                    parent.height = h
                    self.heights[parent] = h
                    dl, parent = parent, parent.par
                    h += 1

        l_h = root.left.height if root.left else 0
        r_h = root.right.height if root.right else 0
        root.height = max(l_h, r_h) + 1
        self.heights[root] = root.height

        self.show_heights()

    def show_heights(self):
        print('Heights:\n')
        for k, v in self.heights.items():
            print(f'{k.value} : {v}\n')

    def check_balance(self, node: Node):
        if not self.parents:
            self.add_parents(self.root)
        if not self.heights:
            self.add_heights(self.root)

        self.update_heights(node, 1)

        curr = node
        bf = None
        while curr != self.root:
            parent = curr.par
            l_h = parent.left.height if parent.left else 0
            r_h = parent.right.height if parent.right else 0
            bf = l_h - r_h
            if bf > 1:
                ll_h = parent.left.left.height if parent.left.left else 0
                lr_h = parent.left.right.height if parent.left.right else 0
                if ll_h > lr_h:
                    self.right_rotate(parent)
                    break
                else:
                    self.left_rotate(parent.left)
                    self.right_rotate(parent)
            elif bf < -1:
                rl_h = parent.right.left.height if parent.right.left else 0
                rr_h = parent.right.right.height if parent.right.right else 0
                if rr_h > rl_h:
                    self.left_rotate(parent)
                else:
                    self.right_rotate(parent.right)
                    self.left_rotate(parent)
            curr = parent

    def left_rotate(self, node: Node):

        p = node.par if node.par else None
        l, r = None, None

        if p:
            l, r = p.left == node, p.right == node

        right_part = node.right
        right_left = right_part.left

        node.right = right_left
        right_left.par = node
        self.parents[right_left] = node
        right_part.left = node
        node.par = right_part
        self.parents[node] = right_part

        if p:
            if r:
                p.right = right_part
            else:
                p.left = right_part

            right_part.par = p
            self.parents[right_part] = p
            self.add_heights(right_part, True)
            r_h = p.right.height if p.right else 0
            l_h = p.left.height if p.left else 0
            p.height = max(r_h, l_h) + 1
            self.heights[p] = p.height

        else:
            right_part.par = None
            del self.parents[right_part]
            self.root = right_part
            self.add_heights(self.root)

    def right_rotate(self, node: Node):
        p = node.par if node.par else None
        l, r = None, None
        if p:
            l, r = p.left == node, p.right == node

        left_part = node.left
        right_part = node.left.right

        node.left = None
        left_part.right = node
        node.par = left_part
        self.parents[node] = node.par
        if right_part:
            node.left = right_part
            right_part.par = node
            self.parents[right_part] = node

        if p:
            if l:
                p.left = left_part
                left_part.par = p
            else:
                p.right = left_part
                left_part.par = p

            self.parents[left_part] = p
            self.add_heights(left_part, True)
            l_h = p.left.height if p.left else 0
            r_h = p.right.height if p.right else 0
            p.height = max(l_h, r_h) + 1
            self.heights[p] = p.height

        else:
            left_part.par = None
            del self.parents[left_part]
            self.root = left_part
            self.add_heights(self.root)

    def add_parents(self, root: Node):
        queue = []

        if root.left:
            root.left.par = root
            self.parents[root.left] = root
            queue.append(root.left)

        if root.right:
            root.right.par = root
            self.parents[root.right] = root
            queue.append(root.right)

        while len(queue):
            parent = queue.pop()
            if parent.left:
                parent.left.par = parent
                self.parents[parent.left] = parent
                queue.append(parent.left)
            if parent.right:
                parent.right.par = parent
                self.parents[parent.right] = parent
                queue.append(parent.right)
        self.show_parents()

    def show_parents(self):
        print('Parents:\n')
        for k, v in self.parents.items():
            print(f'{k.value} : {v.value}\n')

    def insert_by_item(self, root: Node, item: int):
        if item < root.value:
            if not root.left:
                new = Node(item)
                root.left = new
                new.par = root
                self.parents[new] = root
                self.check_balance(root.left)
                return

            self.insert_by_item(root.left, item)

        else:
            if not root.right:
                new = Node(item)
                root.right = new
                new.par = root
                self.parents[new] = root
                self.check_balance(root.right)
                return

            self.insert_by_item(root.right, item)

    def find_deepest_node(self, root):
        if root is None:
            return None

        q, node = deque([root]), None

        while len(q):
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return node

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

    def find_node_by_item(self, item):  # O(logN)
        if self.root.value == item:
            return self.root
        node = self.root
        while True:
            if node.value == item:
                return node
            elif node.value < item:
                node = node.right
            elif node.value > item:
                node = node.left

    def lnr(self, node, arr=[]): # O(logN)
        if node:
            self.lnr(node.left, arr)
            arr.append(node)
            self.lnr(node.right, arr)
        return arr

    def nlr(self, node, arr=[]):  # O(logN)
        if node:
            arr.append(node)
            self.nlr(node.left, arr)
            self.nlr(node.right, arr)
        return arr

    def lrn(self, node, arr=[]):  # O(logN)
        if node:
            self.lrn(node.left, arr)
            self.lrn(node.right, arr)
            arr.append(node)
        return arr

    def find_pr(self, node):  # O(logN)
        while node.right:
            node = node.right
        return node

    def get_node_height(self, node):  # O(1)/O(logN)
        if not self.heights:
            queue = deque([node])
            val = node.value
            less, more = 0, 0
            while len(queue):
                elem = queue.pop()
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
                if elem.value < val and elem.left or elem.right:
                    less += 1
                elif elem.value > val and elem.left or elem.right:
                    more += 1
            return max(less, more) + 1

        return self.heights[node]


if __name__ == '__main__':
    elems = [-3, -2, 0, 3, 6, 8, 10]
    tree = AvlTree(elems)
    tree.root.right.left.left, tree.root.right.right.right = Node(5), Node(13)
    tree.root.right.left.height = tree.heights[tree.root.right.left] = 2
    tree.add_parents(tree.root)
    tree.add_heights(tree.root, True)
    tree.root.right.right.left = Node(9)
    tree.root.right.right.left.par = tree.parents[tree.root.right.right.left] = tree.root.right.right
    # tree.root.right.left.right = Node(7)
    # tree.root.right.left.right.par = tree.parents[tree.root.right.left.right] = tree.root.right.left
    tree.delete_by_item(tree.root, 10)
    print(tree)
    tree.show_parents()
    tree.show_heights()


