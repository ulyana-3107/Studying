class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next}'


class LinkedList:
    def __init__(self, lst=None):
        if lst is not None:
            self.head = self.build_chain(lst)

    def __str__(self):
        return f'{self.head}'

    def build_chain(self, lst) -> ListNode:
        lnodes = [ListNode(i) for i in lst]
        for i in range(len(lnodes) - 1):
            lnodes[i].next = lnodes[i + 1]
        return lnodes[0]


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next