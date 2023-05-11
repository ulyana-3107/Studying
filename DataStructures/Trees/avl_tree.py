from collections import deque


# Самому присваивать ноды нельзя - только если создание через список или вставка через функцию.

# вставка и удаление по значению (O(logn))  - вставка - Done. удаление - Done
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
        node_found = self.find_node_by_item(item)
        child_num = 2

        if not node_found.right or not node_found.left:
            child_num -= 1
        if not node_found.right and not node_found.left:
            child_num -= 1

        # leaf case
        if child_num == 0:

            parent = node_found.par

            if not parent:
                self.root = None
                return
            else:

                if parent.left == node_found:
                    parent.left = None
                    parent.height -= int(bool(parent.right is None))
                    self.heights[parent] = parent.height

                else:
                    parent.right = None
                    parent.height -= int(bool(parent.left is None))
                    self.heights[parent] = parent.height

            self.check_balance(parent)

        # node to be deleted has 1 child tree
        elif child_num == 1:

            parent = node_found.par
            del self.heights[node_found]

            if node_found.left is not None:
                new_child = node_found.left
            else:
                new_child = node_found.right

            if parent:
                if parent.left == node_found:
                    parent.left = new_child
                    self.parents[parent.left] = parent.left.par = parent
                    self.update_heights(parent.left, 2)
                    self.check_balance(parent.left)

                else:
                    parent.right = new_child
                    self.parents[parent.right] = parent.right.par = parent
                    self.update_heights(parent.right, 2)
                    self.check_balance(parent.right)

            else:
                self.root = new_child
                new_child.par = None
                del self.parents[new_child]

        else:
            # left and right childs
            parent = node_found.par
            new_part = None
            node_link_to_update, node_link_to_check_bf = None, None

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

                node_link_to_check_bf = new_part

            else:
                if lr_h >= rl_h:
                    repl_tree = node_found.left.right
                    pr = self.find_pr(repl_tree)

                    if pr == repl_tree:
                        node_found.left.right = None
                        node_link_to_update = node_link_to_check_bf = node_found.left

                    else:
                        par_pr = pr.par
                        par_pr.right = None
                        node_link_to_update = node_link_to_check_bf = par_pr

                else:
                    repl_tree = node_found.right.left
                    pr = self.find_pr(repl_tree)

                    if pr == repl_tree:
                        node_found.right.left = None
                        node_link_to_update = node_link_to_check_bf = node_found.right

                    else:
                        par_pr = pr.par
                        par_pr.right = None
                        node_link_to_update = node_link_to_check_bf = par_pr

                del self.parents[pr]
                pr.left, pr.right = node_found.left, node_found.right
                node_found.left.par = node_found.right.par = pr
                self.parents[node_found.left] = self.parents[node_found.right] = pr
                new_part = pr

            if parent:
                self.parents[new_part] = new_part.par = parent
                if parent.left == node_found:
                    parent.left = new_part
                else:
                    parent.right = new_part

                par_l_h = parent.left.height if parent.left else 0
                par_r_h = parent.right.height if parent.right else 0
                self.heights[parent] = parent.height = max(par_l_h, par_r_h) + 1

            else:
                new_part.par = None
                self.root = new_part

            self.update_heights(node_link_to_update, 3)
            self.check_balance(node_link_to_check_bf)

        if node_found in self.parents:
            del self.parents[node_found]

        if node_found in self.heights:
            del self.heights[node_found]

    def update_heights(self, node: Node, mode: int):
        """
        Function to update heights in a tree after changing it
        :param node: new_inserted node/parent of deleted node  depending on mode
        :param mode: 1 - update after insertion, 2 - after deletion a node with exactly 1 child,
        3 - deleting a node with 2 childs
        :return: None
        """
        if mode == 1:
            # updating heights after insertion: go bottom-up and change height if needed and it's garanteed that the
            # given node has parent at the beginning
            parent, child = node.par, node

            if parent.right and parent.left:
                return

            while parent != self.root:
                self.change_parent_height_after_insertion(parent, child, self.heights)
                parent, child = parent.par, parent

            self.change_parent_height_after_insertion(parent, child, self.heights)

        elif mode == 2:
            # ONLY BOTTOM UP MANNER
            # mode 2 is being used for deletion cases, when we delete node which has exactly one node to go bottom up
            # untill we encounter a node that has stable height
            start = node
            parent = start.par
            stopped = False

            if not parent:
                self.change_height(node, self.heights)

            while parent != self.root:

                curr_height = parent.height
                self.change_height(parent, self.heights)

                if curr_height == self.heights[parent]:
                    stopped = True
                    break
                else:
                    parent = parent.par

            if not stopped:
                self.change_height(parent, self.heights)

        else:
            start = node
            parent = start.par

            while parent != self.root:
                self.change_height(parent, self.heights)
                parent = parent.par

            self.change_height(parent, self.heights)

    def change_parent_height_after_insertion(self, parent: Node, child: Node, heights: dict):
        if parent.left == child:

            if not parent.right:
                parent.height += 1
                heights[parent] = parent.height
            else:
                heights[parent] = parent.height = max(parent.left.height, parent.right.height) + 1

        else:
            if not parent.left:
                parent.height += 1
                heights[parent] = parent.height
            else:
                heights[parent] = parent.height = max(parent.left.height, parent.right.height) + 1

    def change_height(self, node: Node, heights: dict) -> None:
        l_h = node.left.height if node.left else 0
        r_h = node.right.height if node.right else 0
        heights[node] = node.height = max(l_h, r_h) + 1

    # Эта функция рассчитана на то, что дерево сбалансированно
    def add_heights(self, root: Node, sub_tree: bool = False):
        if not sub_tree:
            self.heights = {}

        dl, dr = self.find_deepest_node(root.left), self.find_deepest_node(root.right)

        if dl is not None:
            self.heights[dl] = dl.height = 1
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
            self.heights[dr] = dr.height = 1
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
        self.heights[root] = root.height = max(l_h, r_h) + 1

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

        curr = node

        while curr != self.root:

            parent = curr.par
            l_h = parent.left.height if parent.left else 0
            r_h = parent.right.height if parent.right else 0
            bf = l_h - r_h

            if bf not in range(-1, 2):
                self.balance_tree(bf, parent)

            curr = parent

        l_h = curr.left.height if curr.left else 0
        r_h = curr.right.height if curr.right else 0
        bf = l_h - r_h

        if bf not in range(-1, 2):
            self.balance_tree(bf, curr)

    def balance_tree(self, bf: int, parent: Node):
        if bf > 1:
            ll_h = parent.left.left.height if parent.left.left else 0
            lr_h = parent.left.right.height if parent.left.right else 0

            if ll_h >= lr_h:
                self.right_rotate(parent)
            else:
                self.left_rotate(parent.left)
                self.right_rotate(parent)

        elif bf < -1:
            rl_h = parent.right.left.height if parent.right.left else 0
            rr_h = parent.right.right.height if parent.right.right else 0

            if rr_h >= rl_h:
                self.left_rotate(parent)
            else:
                self.right_rotate(parent.right)
                self.left_rotate(parent)

    def left_rotate(self, node: Node):

        p = node.par

        right_part = node.right
        right_left = right_part.left

        node.right = right_left
        if right_left:
            self.parents[right_left] = right_left.par = node
        right_part.left = node
        self.parents[node] = node.par = right_part

        if p:
            if p.right == node:
                p.right = right_part
            else:
                p.left = right_part

            self.parents[right_part] = right_part.par =  p
            self.add_heights(right_part, True)

            r_h = p.right.height if p.right else 0
            l_h = p.left.height if p.left else 0

            self.heights[p] = p.height = max(r_h, l_h) + 1

        else:
            right_part.par = None
            del self.parents[right_part]
            self.root = right_part
            self.add_heights(self.root)

    def right_rotate(self, node: Node):
        p = node.par

        left_part = node.left
        right_part = node.left.right

        node.left = None
        left_part.right = node
        self.parents[node] = node.par = left_part

        if right_part:
            node.left = right_part
            self.parents[right_part] = right_part.par = node

        if p:
            if p.left == node:
                p.left = left_part
                left_part.par = p
            else:
                p.right = left_part
                left_part.par = p

            self.parents[left_part] = p
            self.add_heights(left_part, True)

            l_h = p.left.height if p.left else 0
            r_h = p.right.height if p.right else 0

            self.heights[p] = p.height = max(l_h, r_h) + 1

        else:
            left_part.par = None
            del self.parents[left_part]
            self.root = left_part
            self.add_heights(self.root)

    def add_parents(self, root: Node):
        queue = []

        if root.left:
            self.parents[root.left] = root.left.par = root
            queue.append(root.left)

        if root.right:
            self.parents[root.right] = root.right.par = root
            queue.append(root.right)

        while len(queue):
            parent = queue.pop()

            if parent.left:
                self.parents[parent.left] = parent.left.par = parent
                queue.append(parent.left)

            if parent.right:
                self.parents[parent.right] = parent.right.par = parent
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
                self.parents[new] = new.par = root

                self.update_heights(root.left, 1)
                self.check_balance(root.left)

                return

            self.insert_by_item(root.left, item)

        else:
            if not root.right:

                new = Node(item)
                root.right = new
                self.parents[new] = new.par = root

                self.update_heights(root.right, 1)
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

    elems = [-7, -6, 0, 8]
    tree = AvlTree(elems)
    tree.add_parents(tree.root)
    tree.add_heights(tree.root, True)
    tree.insert_by_item(tree.root, -4)
    tree.root.left.left.left = Node(-9)
    tree.root.left.left.left.par = tree.parents[tree.root.left.left.left] = tree.root.left.left
    tree.root.left.left.height, tree.root.left.height, tree.root.height = 2, 3, 4
    tree.heights[tree.root.left.left], tree.heights[tree.root.left], tree.heights[tree.root] = 2, 3, 4
    tree.root.left.right.left = Node(-5)
    tree.parents[tree.root.left.right.left] = tree.root.left.right.left.par = tree.root.left.right
    tree.root.left.right.height = tree.heights[tree.root.left.right] = 2
    tree.delete_by_item(tree.root, -6)
    print(tree)
    tree.show_parents()
    tree.show_heights()


