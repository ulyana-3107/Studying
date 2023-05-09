from collections import deque


# Самому присваивать ноды нельзя - только если создание через список или вставка через функцию.

# вставка и удаление по значению (O(logn))
# создание дерева из любого списка (O(nlogn))
# обходы дерева (3 штуки за O(n) каждый)
# найти элемент по значению (O(logn))
# высота ((O(logn))


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
            elems.sort()
            self.root = self.tree_build(elems)
        else:
            self.root = None
        self.parents, self.heights = None, None

    def __str__(self, node=None):
        if self.is_empty():
            return f'this tree is empty.'
        else:
            return f'{self.root}'

    def get_bf(self, node: Node) -> bool:
        if node.left and not node.right:
            if node.left.height > 0:
                return False
            return True
        elif node.right and not node.left:
            if node.left.height > 0:
                return False
            return True
        else:
            l_h, r_h = node.left.height, node.right.height
            return abs(l_h - r_h) in range(2)

    def insert_by_item(self, item: int) -> None:
        if not self.heights:
            self.add_heights()
        node, new_node = self.root, Node(item)
        while True:
            if node.value < item:
                if node.right is None:
                    node.right = new_node
                    new_node.par = node
                    self.parents[new_node] = node
                    self.update_heights1(new_node)
                    self.balance_tree(new_node)
                else:
                    node = node.right
            elif node.value > item:
                if node.left is None:
                    node.left = new_node
                    new_node.par = node
                    self.parents[new_node] = node
                    self.update_heights1(new_node)
                    self.balance_tree(new_node)
                else:
                    node = node.left
            else:
                break

    def balance_tree(self, node: Node) -> None:
        while node != self.root:
            parent = node.par
            bf = self.get_bf(parent)
            if not bf:
                if parent == self.root:
                    new_tree = self.new_tree_build(parent)
                    self.root = new_tree.root
                    self.heights, self.parents = new_tree.heights, new_tree.parents
                    return
                else:
                    parent_2 = parent.par
                    l, r = parent_2.left == parent, parent_2.right == parent
                    new_tree = self.new_tree_build(parent, True)
                    new_tree.add_heights(new_tree.root)
                    if l:
                        parent_2.left = new_tree.root
                        new_tree.root.par = parent_2
                        other_h = parent_2.right.height if parent_2.right else 0
                        parent_2.height = max(parent_2.left.height, other_h) + 1
                    else:
                        parent_2.right = new_tree.root
                        new_tree.root.par = parent_2
                        other_h = parent_2.left.height if parent_2.left else 0
                        parent_2.height = max(parent_2.right.height, other_h) + 1
                    for k, v in new_tree.parents.items():
                        self.parents[k] = v
                    for k, v in new_tree.heights.items():
                        self.heights[k] = v
                    self.parents[new_tree.root] = parent_2
                    self.heights[parent_2] = parent_2.height
            node = parent
        bf = self.get_bf(node)
        if not bf:
            new_tree = self.new_tree_build(node)
            self.root = new_tree.root
            self.heights, self.parents = new_tree.heights, new_tree.parents

    def new_tree_build(self, node: Node, delete=False):  # O(NlogN)
        arr = self.lnr(node, [])
        elements = [el.value for el in arr]
        if delete is True:
            for el in arr:
                self.parents[el] = None
                self.heights[el] = None
        new_root = AvlTree(elements)
        new_root.add_heights()
        return new_root

    def balance_tree2(self, node: Node) -> None:
        pass

    def del_by_item(self, item: int) -> None:
        if not self.parents:
            self.add_parents(self.root)
        if not self.heights:
            self.add_heights()
        node = self.find_node_by_item(item)
        if not node.left and not node.right:
            if not node.par:
                del self.heights[self.root]
                self.root = None
            else:
                parent = node.par
                l, r = parent.left == node, parent.right == node
                if l:
                    parent.left = None
                    self.update_heights2(parent, 1)
                else:
                    parent.right = None
                    self.update_heights2(parent, 1)
                self.balance_tree(parent)
        elif node.left and not node.right:
            if not node.par:
                node.left.par = None
                del self.parents[node.left]
                del self.heights[self.root]
                self.root = node.left
            else:
                parent = node.par
                node.left.par = parent
                self.parents[node.left] = parent
                del self.parents[node]
                del self.heights[node]
                l, r = parent.left == node, parent.right == node
                if l:
                    parent.left = node.left
                    h1 = parent.left.height
                    h2 = parent.right.height if parent.right else 0
                else:
                    parent.right = node.left
                    h1 = parent.right.height
                    h2 = parent.left.height if parent.left else 0
                self.update_heights2(parent, 2, [h1, h2])
                self.balance_tree(node.left)
        elif node.right and not node.left:
            if not node.par:
                node.right.par = None
                del self.parents[node.right]
                del self.heights[self.root]
                self.root = node.right
            else:
                parent = node.par
                node.right.par = parent
                self.parents[node.right] = parent
                del self.parents[node]
                del self.heights[node]
                l, r = parent.left == node, parent.right == node
                if l:
                    parent.left = node.right
                    h1 = parent.left.height
                    h2 = parent.right.height if parent.right else 0
                else:
                    parent.right = node.right
                    h1 = parent.right.height
                    h2 = parent.left.height if parent.left else 0
                self.update_heights2(parent, 2, [h1, h2])
                self.balance_tree(parent)
        # node.right and node.left
        else:
            if not node.par:
                r, l = node.right.height, node.left.height
                rl = node.right.left.height if node.right.left else 0
                lr = node.left.right.height if node.left.right else 0
                # root = node.right
                if r + lr >= l + rl:  # так вероятнее, что дерево останется сбалансированным
                    self.root = node.right
                    del self.parents[node.right]
                    node.right.par = None
                    if node.right.left:
                        pr = self.find_pr(node.right.left)
                        pr.left = node.left
                        node.left.par = pr
                        self.parents[node.left] = pr
                    else:
                        self.root.left = node.left
                        node.left.par = self.root
                        self.parents[node.left] = self.root
                else:
                    self.root = node.left
                    del self.parents[node.left]
                    node.left.par = None
                    if node.left.right:
                        pr = self.find_pr(node.left.right)
                        pr.right = node.right
                        node.right.par = pr
                        self.parents[node.right] = pr
                    else:
                        self.root.right = node.right
                        node.right.par = self.root
                        self.parents[node.right] = self.root
                self.add_heights()
                pr = self.find_pr(self.root)
                self.balance_tree(pr)
            else:
                parent = node.par
                l, r = parent.left == node, parent.right == node
                # составляем новое дерево:
                if l:
                    pr = self.find_pr(parent.left.left)
                    pr.right = node.right
                    parent.left.left.par = parent
                    self.parents[parent.left.left] = parent
                    parent.left = node.left
                    del self.parents[node]
                    del self.heights[node]
                    self.update_heights3(parent, parent.left)
                else:
                    pr = self.find_pr(parent.right.right)
                    pr.left = node.left
                    parent.right.right.par = parent
                    self.parents[parent.right.right] = parent
                    parent.right = node.right
                    del self.parents[node]
                    del self.heights[node]
                    self.update_heights3(parent, parent.right)
                pr = self.find_pr(parent)
                self.balance_tree(pr)

    def new_heights(self, node: Node) -> None:
        arr = []
        if node.left:
            arr.append(node.left)
        if node.right:
            arr.append(node.right)
        if len(arr):
            for n in arr:
                dn, h = self.deepestNode(n), 1
                if dn in (node.left, node.right):
                    node.height = 1
                    self.heights[node] = 1
                    break
                while dn not in (node.left, node.right):
                    dn.par.height = h
                    self.heights[dn.par] = dn.par.height
                    dn = dn.par
                    h += 1
        if len(arr) == 2:
            node.height = max(node.left.height, node.right.height) + 1
        elif node.left:
            node.height = node.left.height + 1
        else:
            node.height = node.right.height + 1
        self.heights[node] = node.height

    def update_heights3(self, parent: Node, new_root: Node) -> None:
        # 1. перезаписать все высоты нового корня 2. проверить кто новый корень- л или п ребенок 3.поменять высоту у ро
        # дителя если надо.
        self.new_heights(new_root)
        l, r = parent.left == new_root, parent.right == new_root
        if l:
            other_h = parent.right.height if parent.right else 0
        else:
            other_h = parent.left.height if parent.left else 0
        if other_h < new_root.height:
            parent.height = new_root.height + 1
            self.heights[parent] = parent.height

    def update_heights1(self, node: Node) -> None:
        parent, child = node.par, node
        while parent != self.root:
            l, r = parent.left == child, parent.right == child
            if l:
                if not parent.right:
                    parent.height += 1
                    self.heights[parent] = parent.height
                    parent, child = parent.par, parent
                else:
                    parent.height = max(parent.left.height, parent.right.height) + 1
                    self.parents[parent] = parent.height
                    parent, child = parent.par, parent
            elif r:
                if not parent.left:
                    parent.height += 1
                    self.heights[parent.height] = parent.height
                    parent, child = parent.par, parent
                else:
                    parent.height = max(parent.left.height, parent.right.height) + 1
                    self.heights[parent] = parent.height
                    parent, child = parent.par, parent
        l, r = parent.left == child, parent.right == child
        if l:
            if not parent.right:
                parent.height += 1
                self.heights[parent] = parent.height
        elif r:
            if not parent.left:
                parent.height += 1
                self.heights[parent.height] = parent.height

    def update_heights2(self, node: Node, case: int, heights: list = []) -> None:
        if case == 1:
            # это значит - что переданный нод явно имеет 0 или 1го ребенка
            if node.left or node.right:
                pass
            else:
                self.heights[node] -= 1
                node.height -= 1
                if node.par:
                    p = node.par
                    l, r = p.left == node, p.right == node
                    if l:
                        h1 = p.left.height
                        h2 = p.right.height if p.right else 0
                        p.height = max(h1, h2) + 1
                        self.heights[p] = p.height
                    elif r:
                        h1 = p.left.height if p.left else 0
                        h2 = p.right.height
                        p.height = max(h1, h2) + 1
                        self.heights[p] = p.height
        else:
            self.heights[node] = max(heights) + 1
            node.height = max(heights) + 1
            # это случай удаления нода с двумя детьми: в таком случае у дерева(новый сын родителя) лучше заново создать
            # высоты и потом у родителя тоже поменять высоту если надо.

    def deepestNode(self, root):
        if root == None:
            return 0
        q, node = deque([root]), None
        while len(q) != 0:
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return node

    def add_parents(self, root):
        self.parents = {}
        visited, fifo = set(), [root]
        while fifo:
            v = fifo.pop()
            visited.add(v)
            if v.left:
                fifo.append(v.left)
                v.left.par = v
                self.parents[v.left] = v
            if v.right:
                fifo.append(v.right)
                v.right.par = v
                self.parents[v.right] = v

    def show_parents(self):
        if not self.parents:
            if not self.is_empty():
                self.add_parents(self.root)
        print('Parents: ' + '\n')
        for k, v in self.parents.items():
            if v:
                print(f'{k.value}:{v.value}')

    def add_heights(self, new=False):
        self.heights = {}
        if not self.parents:
            self.add_parents(self.root)
        arr = []
        if self.root.left:
            arr.append(self.root.left)
        if self.root.right:
            arr.append(self.root.right)
        for node in arr:
            leaf, h = self.deepestNode(node), 1
            if leaf == node and self.root.left == leaf and not self.root.right or self.root.right == leaf and not self.root.left:
                self.root.height = 1
                self.heights[self.root] = self.root.height
            while leaf not in (self.root.left, self.root.right):
                leaf.par.height = h
                self.heights[leaf.par] = h
                h += 1
                leaf = leaf.par
        left_h = self.root.left.height if self.root.left else 0
        right_h = self.root.right.height if self.root.right else 0
        if left_h and right_h:
            self.root.height = max(left_h, right_h) + 1
        elif left_h and not right_h:
            self.root.height = left_h + 1
        elif right_h and not left_h:
            self.root.height = right_h + 1
        else:
            self.root.height = 1
        self.heights[self.root] = self.root.height

    def show_heights(self):
        if self.is_empty():
            print('tree is empty')
            return
        elif not self.heights:
            self.add_heights()
        print('Heights:')
        for k, v in self.heights.items():
            if v:
                print(f'{k.value} : {v}')

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

    def lnr(self, node, arr): # O(logN)
        if node:
            self.lnr(node.left, arr)
            arr.append(node)
            self.lnr(node.right, arr)
        return arr

    def nlr(self, node, arr):  # O(logN)
        if node:
            arr.append(node)
            self.nlr(node.left, arr)
            self.nlr(node.right, arr)
        return arr

    def lrn(self, node, arr):  # O(logN)
        if node:
            self.lrn(node.left, arr)
            self.lrn(node.right, arr)
            arr.append(node)
        return arr

    def find_pr(self, node):  # O(logN)
        while node.right:
            node = node.right
        return node

    def node_height(self, node):  # O(1)
        if not self.heights:
            self.add_heights()
        return self.heights[node]


# elems = [1, 2, 3, 4, 5, 6, 7]
# tree = AvlTree(elems)
# tree.root.left.left.left = Node(-3)
# tree.root.left.left.left.right = Node(-2)
# tree.add_parents(tree.root)
# tree.add_heights()
# tree.del_by_item(6)
# print(tree)
# tree.show_heights()
# tree.show_parents()
