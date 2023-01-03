class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursion(self, nums, start, end):# end = N тк это и есть количество нодов
        if start > end:
            return None
        middle = (start + end + 1) // 2 # O(1)
        root = TreeNode(nums[middle]) # O(1)
        root.left = self.recursion(nums, start, middle - 1) # O(N - 1/2) -> O(N)
        root.right = self.recursion(nums, middle + 1, end) # O(N + 1/2) -> O(N)
        return root
# высота дерева по определению - O(logN) -> общая сложность - O(N)

    def sorted_arr_to_bst(self, nums: list):
        return self.recursion(nums, 0, len(nums) - 1)