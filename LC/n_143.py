# You are given the head of a singly linked-list. The list can be represented as:


# UNDERDONE!!!!


class Node:
    def __init__(self, val):
        self.val, self.next = val, None

    def __str__(self):
        return f'{self.val} -> {self.next}'


def reorder_list1(lst: list) -> list:
    n = len(lst)
    if n < 2:
        return lst
    new = []
    for i in range(n//2):
        j = n - i - 1
        new.append(lst[i])
        new.append(lst[j])
    if n % 2:
        new.append(lst[n//2])
    return new


def reorderList(head: Node) -> None:
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    curr, prev = slow.next, None
    slow.next = None  # set the next of the slow to None to break the link
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second_half = prev

    # Step 3: Merge the first half and the reversed second half of the linked list
    first_half = head
    while first_half and second_half:
        temp1, temp2 = first_half.next, second_half.next
        first_half.next = second_half
        second_half.next = temp1
        first_half, second_half = temp1, temp2


arr1 = [1, 2, 3, 4]  # [1, 4, 2, 3]
arr2 = [1, 2, 3, 4, 5]  # [1, 5, 2, 4, 3]
arr3 = [1, 2, 3]  # 1, 3, 2
nodes2 = [Node(i) for i in arr2]
for i in range(len(nodes2) - 1):
    nodes2[i].next = nodes2[i + 1]
# print(reorder_list1(arr3))
reorderList(nodes2[0])
print(nodes2[0])
