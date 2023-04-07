# Дан список и цифра, верните список с удаленными этими цифрами


def remove_numbers(arr: list, num: int) -> list:
    i = 0
    while i != len(arr):
        if arr[i] == num:
            arr = arr[:i] + arr[i + 1:]
            return remove_numbers(arr, num)
        i += 1
    return arr


print(remove_numbers([2, 1, 2, 3, 4, 2, 4, 5, 9, 2], 2))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class LinkedList:
    def __init__(self, lst=None):
        if lst is not None:
            self.head = self.build_chain(lst)
        else:
            self.head = ListNode()

    def __repr__(self):
        return f'{self.head}'

    def build_chain(self, lst) -> ListNode:
        nodes = [ListNode(i) for i in lst]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    def nodes_to_list(self):
        lst = []
        start = self.head
        while start.next:
            lst.append(start.val)
            start = start.next
        lst.append(start.val)
        return lst

    def remove_nums(self, val):
        start = self.head
        while True:
            if start.next == val:
                start.next = start.next.next

    def remove_numbers(self, lst: list, num: int) -> list:
        i = 0
        while i != len(lst):
            if lst[i] == num:
                lst = lst[:i] + lst[i + 1:]
                return self.remove_numbers(lst, num)
            i += 1
        self.head = self.build_chain(lst)


ll = LinkedList([1, 2, 2, 1, 2, 2, 3, 1, 2, 3, 3, 4])
print(ll)
ll.remove_numbers(ll.nodes_to_list(), 2)
print(ll)

