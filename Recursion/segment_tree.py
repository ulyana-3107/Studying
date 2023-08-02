class SegmentTree:
    def __init__(self, lst):
        self.tree = [0] * (4 * len(lst))
        self.init_tree(lst, 0, len(lst) - 1, 0)

    def init_tree(self, lst, start, end, index):
        if start == end:
            self.tree[index] = lst[start]
            return

        mid = (start + end) // 2
        self.init_tree(lst, start, mid, 2 * index + 1)
        self.init_tree(lst, mid + 1, end, 2 * index + 2)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def append(self, val):
        self.append_util(val, 0, len(self.tree) // 4 - 1, 0)

    def append_util(self, val, start, end, index):
        if start == end:
            self.tree[index] += val
            return

        mid = (start + end) // 2
        if start <= val <= mid:
            self.append_util(val, start, mid, 2 * index + 1)
        else:
            self.append_util(val, mid + 1, end, 2 * index + 2)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def pop(self):
        last_index = len(self.tree) // 4 - 1
        val = self.tree[last_index]
        self.pop_util(last_index, 0, last_index - 1, 0)
        return val

    def pop_util(self, target_index, start, end, index):
        if start == end:
            self.tree[index] -= self.tree[target_index]
            return

        mid = (start + end) // 2
        if start <= target_index <= mid:
            self.pop_util(target_index, start, mid, 2 * index + 1)
        else:
            self.pop_util(target_index, mid + 1, end, 2 * index + 2)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def calculate(self, i, j):
        return self.calculate_util(0, len(self.tree) // 4 - 1, i, j, 0)

    def calculate_util(self, start, end, target_start, target_end, index):
        if target_start <= start and end <= target_end:
            return self.tree[index]

        if end < target_start or start > target_end:
            return 0

        mid = (start + end) // 2
        left_sum = self.calculate_util(start, mid, target_start, target_end, 2 * index + 1)
        right_sum = self.calculate_util(mid + 1, end, target_start, target_end, 2 * index + 2)

        return left_sum + right_sum
