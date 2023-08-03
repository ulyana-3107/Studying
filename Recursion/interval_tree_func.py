class SegmentTree:
    def __init__(self, lst, func):
        self.tree = [0] * (4 * len(lst))
        self.func = func
        self._build(lst, 0, 0, len(lst) - 1)

    def _build(self, lst, idx, left, right):
        if left == right:
            self.tree[idx] = lst[left]
        else:
            mid = (left + right) // 2
            self._build(lst, 2 * idx + 1, left, mid)
            self._build(lst, 2 * idx + 2, mid + 1, right)
            self.tree[idx] = self.func(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def append(self, val):
        lst = self._tolist()
        lst.append(val)
        self.tree = [0] * (4 * len(lst))
        self._build(lst, 0, 0, len(lst) - 1)

    def pop(self):
        lst = self._tolist()
        lst.pop()
        self.tree = [0] * (4 * len(lst))
        self._build(lst, 0, 0, len(lst) - 1)

    def calculate(self, i, j):
        return self._query(0, 0, len(self.tree) // 4 - 1, i, j)

    def _query(self, idx, left, right, i, j):
        if left >= i and right <= j:
            return self.tree[idx]
        if right < i or left > j:
            return 0
        mid = (left + right) // 2
        return self.func(self._query(2 * idx + 1, left, mid, i, j), self._query(2 * idx + 2, mid + 1, right, i, j))

    def _tolist(self):
        lst = []
        self._to_list_helper(0, 0, len(self.tree)//4 - 1, lst)
        return lst

    def _to_list_helper(self, idx, left, right, lst):
        if left == right:
            lst.append(self.tree[idx])
        else:
            mid = (left + right) // 2
            self._to_list_helper(2 * idx + 1, left, mid, lst)
            self._to_list_helper(2 * idx + 2, mid + 1, right, lst)
