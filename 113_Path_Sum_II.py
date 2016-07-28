# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.cur = []
        self.nums = []
        self.sum = sum
        if not root:
            return []
        self.dfs(root)
        return self.nums

    def dfs(self, node):
        self.cur.append(node.val)
        left, right = False, False
        if node.left:
            left = True
            self.dfs(node.left)
        if node.right:
            right = True
            self.dfs(node.right)
        if not left and not right:
            s = sum(self.cur)
            if s == self.sum:
                self.nums.append(self.cur[:])
        self.cur.pop()