class CircQueueNode(object):
    def __init__(self, v, n, p):
        self.value, self.next, self.prev = v, n, p


class CircQueue(object):
    def __init__(self, k: int):
        self.capacity = k
        self.left = CircQueueNode('lol', None, None)
        self.right = CircQueueNode('lol', None, self.left)
        self.left.next = self.right

    def enQueue(self, elem) -> bool:
        if self.isFull():
            return False
        new = CircQueueNode(elem, self.right, None)
        self.right.prev.next = new
        self.right.prev = new
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.capacity += 1
        return True

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.capacity == 0

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.value


# Everything - O(1)
