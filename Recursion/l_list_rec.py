class Node:
    def __init__(self, elem):
        self.elem, self.next = elem, None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, value):
        if index == 0:
            new_n = Node(value)
            new_n.next = self.head
            self.head = new_n

        elif self.head is None:
            raise IndexError

        else:
            self._insert_rec(self.head, index, value)

    def _insert_rec(self, curr, index, value):
        if index == 1:
            n_node = Node(value)
            n_node.next = curr.next
            curr.next = n_node
        elif curr.next is None:
            raise IndexError
        else:
            self._insert_rec(curr.next, index - 1, value)

    def remove(self, index):
        if self.head is None:
            raise IndexError
        elif index == 0:
            self.head = self.head.next
        else:
            self._remove_rec(self.head, index)

    def _remove_rec(self, curr, index):
        if curr.next is None:
            raise IndexError
        elif index == 1:
            curr.next = curr.next.next
        else:
            self._remove_rec(curr.next, index - 1)

    def swap(self, i1, i2):
        if self.head is None:
            raise IndexError
        else:
            self._swap_rec(self.head, i1, i2)

    def _swap_rec(self, curr, i1, i2):
        if curr is None:
            raise IndexError
        elif i1 == 0 or i2 == 0:
            temp = curr.elem
            curr.elem = curr.next.elem
            curr.next.elem = temp
        else:
            self._swap_rec(curr.next, i1 - 1, i2 - 1)


if __name__ == '__main__':
    ll = LinkedList()