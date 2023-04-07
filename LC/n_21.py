# Описание: Даны головы двух отсортированных связных списков. Требуется соединить два списка в один отсортированный спи
# сок путем сращивания нодов каждого списка и вернуть голову нового списка. Элементы каждого из исходных списков
# расположены в неубывающем порядке. Количество элементов каждого из исходных списков не превышает 50. Значение любого
# из элементов находится в диапазоне (-100;100).
# Решение:
# 1) Решение на обычных списках.
# 2)Реализация класса Node.
# 3) Реализация класса LinkedList.
# 4) Применение решения к связным спискам.
# Если не получается решить через рекурсию - то нужно решить сначала не через рекурсию.


class Node:

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next, self.prev = next, prev

    def __str__(self):
        return f'{self.value} -> {self.next}'


class LinkedList:

    def __init__(self, arr=None):
        if not arr:
            self.head = None
        else:
            self.head = self.create_chain(arr)

    def __str__(self):
        return f'{self.head}'

    def create_chain(self, arr) -> Node:
        nodes = [Node(v) for v in arr]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].prev = nodes[i - 1]
        return nodes[0]


# def new_list(list1, list2) -> list:
#     new_list = list()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next

