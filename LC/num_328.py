class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        currentOdd = head
        count = 2
        node = head
        pre = node
        node = node.next
        while node is not None:
            if count % 2 == 0:
                pre = node
                node = node.next
            else:
                next = node.next
                pre.next = next
                temp = currentOdd.next
                currentOdd.next = node
                node.next = temp
                currentOdd = node
                node = next
            count += 1
        return head


# My Solution
# class Node:
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#     def __str__(self):
#         return f'{self.elem} -> {self.next}'
#
# class SinglyLinkedList:
#     def __init__(self, lst=None):
#         if lst:
#             self.head = self.build_list(lst)
#         else:
#             self.head = None
#
#     def __str__(self):
#         return f'{self.head}'
#
#     def build_list(self, lst):
#         l = len(lst)
#         i = 0
#         start_node = Node(lst[i])
#         start = start_node
#         while i < l - 1:
#             i += 1
#             next = Node(lst[i])
#             start.next = next
#             start = next
#         return start_node
#
# def _odd_even(arr):
#     odd, even= [], []
#     l, i = len(arr), 0
#     while i < l - 2:
#         odd.append(i)
#         even.append(i + 1)
#         i += 2
#     if i == l - 2:
#         odd.append(i)
#         even.append(i + 1)
#     else:
#         odd.append(i)
#     odd.extend(even)
#     return [arr[i] for i in odd]
#
# def all_items(head: Node) -> list:
#     res, curr = [], head
#     while curr.next:
#         res.append(curr.elem)
#         curr = curr.next
#     res.append(curr.elem)
#     return res
#
# def odd_even(head:Node|list) -> Node:
#     if isinstance(head, Node):
#         nodes = _odd_even(all_items(head))
#         sll = SinglyLinkedList(nodes)
#         return sll
#     else:
#         return _odd_even(head)
#
#
# arr = [i for i in range(1, 6)]
# sll = SinglyLinkedList(arr)
# print(f'sll at the start: {sll}')
# print(odd_even(sll.head))
# print(odd_even(arr))










